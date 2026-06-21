import math
import pandas as pd
import frequency
import entropy
import time

frequency.check_hashes()
word_freq = frequency.get_freq()
answer_list = frequency.answer_list
test_df = pd.DataFrame(columns=['word', 'turn 1', 'turn 2', 'turn 3', 'turn 4', 'turn 5', 'turn 6', 'won'])


# Testing function to test a provided guess list that provides percent updates, average score,
#       number of words left at failure, and total testing time
def test_bot(guess_list):
    accuracy = 0
    missed = 0
    missed_list = []
    feedback = ''
    words_left = 0
    start = time.time()

    print('-' * 50)
    print("             Testing Westley's Wordle Bot")
    print('-' * 50)

    for i, secret in enumerate(guess_list):
        guesses_list = guess_list.copy()
        guess = 1

        #  Percent printing code block
        if (i + 1) % (math.ceil(len(guess_list) * .05)) == 0 and i != 0:
            perc = (i + 1) / len(guess_list) * 100
            print(f'Testing: {perc:.2f}% | Average Score: ' + str(
                round(accuracy / (i + 1), 2)) + f' - # of Missed Words: {missed}')
        word_info = [secret]
        word = None

        while True:
            if guess == 1:
                word = 'crane'
            elif guess == 2:
                word = frequency.explorer_lookup[feedback]
            elif guess == 7:
                accuracy += 8
                missed += 1
                missed_list.append(secret)
                words_left += len(guesses_list)
                word_info.append(False)
                test_df.loc[len(test_df)] = word_info
                break
            elif guess == 4 and len(guesses_list) > 5:
                word = entropy.sacrifice_word(word, feedback, guesses_list)
            elif guess == 5 and len(guesses_list) > 2:
                word = entropy.sacrifice_word(word, feedback, guesses_list)
            else:
                word = entropy.tot_guess_eval(guesses_list)

            feedback = entropy.get_feedback(word, secret)
            if feedback == '22222':
                accuracy += guess
                for w in range(7 - guess):
                    word_info.append(0)
                word_info.append(True)
                test_df.loc[len(test_df)] = word_info
                break

            guesses_list = entropy.redefine_list(word, guesses_list, feedback)
            word_info.append(len(guesses_list))
            guess += 1

    test_df.to_csv('test_results.csv', index=False)

    fin_accuracy = accuracy / len(guess_list)
    print(f'Final average score: {fin_accuracy:.3f}')
    if missed != 0:
        avg_words_left = words_left / missed
        print(f"Avg # of words left upon failure: {avg_words_left:.2f}")

    end = time.time()
    tot_time = end - start
    print(f"Total Testing Time: {tot_time / 60:.2f} minutes")


test_bot(frequency.legal_guesses)
