import math
import frequency
from math import log2
import pandas as pd

#  Grab required variables from the frequency file
word_freq = frequency.get_freq()
legal_guesses = frequency.legal_guesses


# Basic entropy formula
def get_entropy(prob):
    return -prob * log2(prob)


# Generates the feedback string with candidate and word
def get_feedback(candidate, word):
    answer = [0] * 5  # Default to the letter not being in the secret
    word = list(word)
    candidate = list(candidate)

    # First pass to grab all green/2 letters and voids the according letter in both the candidate and word
    for i in range(5):
        if candidate[i] == word[i]:
            answer[i] = '2'
            word[i] = None
            candidate[i] = None

    # Second pass to grab all yellow/1 letters
    for i in range(5):
        if candidate[i] is not None:
            if candidate[i] in word:
                answer[i] = '1'
                word[word.index(candidate[i])] = None

    # Joins all 2, 1, and 0s together to get the final feedback
    return "".join(map(str, answer))


# Narrows guess list upon guess feedback
def redefine_list(guess, guess_list, feedback):
    return [word for word in guess_list if get_feedback(guess, word) == feedback]


# Determines how much information gain a word will provide against a guess list
def guess_eval(guess, guess_list):
    buckets = {}
    tot_weight = 0
    for word in guess_list:
        tot_weight += word_freq.get(word, 1)

    for word in guess_list:
        answer = get_feedback(guess, word)
        if answer not in buckets.keys():
            buckets[answer] = word_freq.get(word, 1)
        else:
            buckets[answer] += word_freq.get(word, 1)

    tot_entropy = 0
    for pattern in buckets.keys():
        tot_entropy += get_entropy(buckets[pattern] / tot_weight)

    return tot_entropy


# Determines the best guess out of the guess list
def tot_guess_eval(guess_list):
    best_guess = ''
    best_entropy = -1

    for word in guess_list:

        temp = guess_eval(word, guess_list) + log2((word_freq.get(word, 1) * 10) + 1)
        if best_entropy < temp:
            best_guess = word
            best_entropy = temp

    return best_guess


# Determines the best guesses out of the guess list and provides according information gain
def tot_guess_eval_detailed(guess_list):
    best_guess_list = {}

    for word in guess_list:
        best_guess_list[word] = guess_eval(word, guess_list) + log2((word_freq[word] * 10) + 1)

    best_guess_list = pd.Series(best_guess_list)

    # Returns top 5 guess suggestions with info gain score
    return best_guess_list.sort_values(ascending=False).head(5)


# Generates the feedback pattern for the explorer guess
def explore_feedback(candidate, guess_list, feedback):
    elim_letters = set()
    for i in range(5):
        if feedback[i] == '0':
            elim_letters.add(candidate[i])

    explore_list = guess_list

    for letter in elim_letters:
        explore_list = [word for word in explore_list if letter not in word]

    return explore_list


# All encompassing method to create, determine, and write a csv of the best guess for each feedback pattern
def create_explorer_lookup(first_guess, legal_words):
    explorer_info = []

    buckets = []
    for word in legal_guesses:
        feedback = get_feedback(first_guess, word)
        if feedback not in buckets:
            buckets.append(feedback)

    i = 1

    for bucket in buckets:
        words = explore_feedback(first_guess, legal_words, bucket)

        best_guess_series = tot_guess_eval_detailed(words)

        best_word = best_guess_series.index[0]
        info_gain = best_guess_series.iloc[0]

        explorer_info.append({'feedback': bucket,
                              'best word': best_word,
                              'info gain': info_gain})

        if i % (math.floor(len(buckets) * .05)) == 0:
            print(str(round(i / len(buckets) * 100, 2)) + '%')
        i += 1

    explorer_df = pd.DataFrame(explorer_info)
    explorer_df.to_csv("explorer_lookup.csv", index=False)


# Unique evaluation method to eliminate additional guesses to escape word traps
def sacrifice_word(guess, feedback, guess_list):
    greens_positions = {i: guess[i] for i in range(len(feedback)) if feedback[i] == '2'}
    green_letters = set(greens_positions.values())

    letter_counts = {}
    for word in guess_list:
        unique_word_letters = set()
        for i, letter in enumerate(word):
            if letter in green_letters and greens_positions.get(i) == letter:
                continue
            unique_word_letters.add(letter)

        for letter in unique_word_letters:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

    best_word = None
    best_score = -float('inf')
    total_remaining_words = len(guess_list)

    for word in frequency.legal_guesses:
        word_letters = set(word)
        score = 0

        for letter in word_letters:
            if letter in letter_counts:
                freq = letter_counts[letter]
                score += freq * (total_remaining_words - freq)

        penalty = len(word_letters.intersection(green_letters))

        final_score = score - (penalty * 1.5)
        if final_score > best_score:
            best_word = word
            best_score = final_score

    return best_word if best_word else tot_guess_eval(guess_list)

