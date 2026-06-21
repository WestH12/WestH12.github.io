import frequency
import entropy

# Generating all legal guesses
frequency.check_hashes()

# Capturing the word frequency list for all legal guesses
word_freq = frequency.get_freq()

guess = 1  # Init the guess variable
legal_guesses = frequency.legal_guesses  # Capturing the guess list
print("Welcome to Westley's Wordle Bot!")
while True:  # Main event loop that run
    if guess == 1:
        print('Best guess: crane')
        word = 'crane'
    elif guess == 7:  # Ends program due to guess limit reached
        print('GAME OVER \nThe secret word was not guessed!')
        break
    else:
        word = entropy.tot_guess_eval(legal_guesses)
        print(f'Best guess: {word}')

    feedback = input('Feedback: ').strip()
    if feedback == '22222':
        print(f"Congratulations on guessing the word in {guess} turn")
        again = input("Do you want to play again? ").lower()
        if again == 'yes':
            legal_guesses = frequency.legal_guesses
            guess = 1
            print("\nWelcome to Westley's Wordle Bot!")
            print('Try the first guess of: crane')
        else:
            break
    else:
        legal_guesses = entropy.redefine_list(word, legal_guesses, feedback)
        guess += 1
