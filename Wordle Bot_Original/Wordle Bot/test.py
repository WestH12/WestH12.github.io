import math
import frequency
import entropy
import time

frequency.check_hashes()
word_freq = frequency.get_freq()


def test_bot(legal_guesses):
    accuracy = 0
    missed = 0
    missed_list = []

    print('-' * 50)
    print("             Testing Westley's Wordle Bot")
    print('-' * 50)

    for i, secret in enumerate(legal_guesses):
        guesses_list = legal_guesses
        guess = 1
        if (i + 1) % (math.floor(len(legal_guesses) * .05)) == 0 and i != 0:
            perc = (i + 1) / len(legal_guesses) * 100
            print(f'Testing: {perc:.2f}% | Average Score: ' + str(
                round(accuracy / (i + 1), 2)) + f' - # of Missed Words: {missed}')

        while True:
            if guess == 1:
                word = 'crane'
            elif guess == 7:
                accuracy += 8
                missed += 1
                missed_list.append(secret)
                break
            else:
                word = entropy.tot_guess_eval(guesses_list)

            feedback = entropy.get_feedback(word, secret)
            if feedback == '22222':
                accuracy += guess
                break

            guesses_list = entropy.redefine_list(word, guesses_list, feedback)
            guess += 1

    fin_accuracy = accuracy / len(legal_guesses)
    print(f'Final average score: {fin_accuracy}')
    print("Missed Words:")
    for word in missed_list:
        print(word)


start = time.time()
test_bot(frequency.legal_guesses)
end = time.time()
tot_time = end - start
print(f"Total Testing Time: {tot_time/3600} hours")
