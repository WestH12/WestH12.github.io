import frequency
from math import log2

word_freq = frequency.get_freq()
legal_guesses = frequency.check_hashes()


def get_entropy(prob):
    return -prob * log2(prob)


def get_feedback(candidate, word):
    answer = [0] * 5
    word = list(word)
    candidate = list(candidate)

    for i in range(5):
        if candidate[i] == word[i]:
            answer[i] = '2'
            word[i] = None
            candidate[i] = None

    for i in range(5):
        if candidate[i] is not None:
            if candidate[i] in word:
                answer[i] = '1'
                word[word.index(candidate[i])] = None

    return "".join(map(str, answer))


def redefine_list(guess, guess_list, feedback):
    return [word for word in guess_list if get_feedback(guess, word) == feedback]


def guess_eval(guess, guess_list):
    buckets = {}
    tot_weight = 0
    for word in guess_list:
        tot_weight += word_freq[word]

    for word in guess_list:
        answer = get_feedback(guess, word)
        if answer not in buckets.keys():
            buckets[answer] = word_freq[word]
        else:
            buckets[answer] += word_freq[word]

    tot_entropy = 0
    for pattern in buckets.keys():
        tot_entropy += get_entropy(buckets[pattern] / tot_weight)

    return tot_entropy


def tot_guess_eval(guess_list):
    best_guess = ''
    best_entropy = -1

    for word in guess_list:

        temp = guess_eval(word, guess_list) + log2((word_freq[word] * 10) + 1)
        if best_entropy < temp:
            best_guess = word
            best_entropy = temp

    return best_guess

