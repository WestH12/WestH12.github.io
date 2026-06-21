import requests
from pathlib import Path
import hashlib
import pandas as pd
import math
import gc
import json

word_freq = {}
all_guesses = [word.strip().lower() for word in Path('files/valid-wordle-words.txt').read_text().splitlines()]
offensive_words = Path('files/badwords.txt').read_text().splitlines()
answer_list = [word.strip().lower() for word in Path('files/wordle-answers-alphabetical.txt').read_text().splitlines()]
legal_guesses = []
explorer_lookup = {}
test_env = False


def check_hashes():
    global offensive_words, legal_guesses
    if test_env:  # For a testing environment to avoid useless api calls
        offensive_url = ('https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/badwordslist'
                         '/badwords.txt')
        online = str(requests.get(offensive_url).text.splitlines())
        online_hash = hashlib.sha256(online.encode())
        local_hash = hashlib.sha256(str(offensive_words).encode())
        if local_hash.hexdigest() == online_hash.hexdigest():
            print('Offensive words up-to-date.')
            legal_guesses = list(set(all_guesses) - set(offensive_words))
            return True
        else:
            offensive_words = list(online)
            print('Offensive words updated.')
            legal_guesses = list(set(all_guesses) - set(offensive_words))
            return False
    else:
        legal_guesses = list(set(all_guesses) - set(offensive_words))


def load_explorer_lookup():  # Loads in the explorer_lookup data from files
    global explorer_lookup
    lookup = pd.read_csv('files/explorer_lookup.csv', index_col='feedback', dtype={'feedback': 'str'})
    explorer_lookup = lookup.drop(columns='info gain')['best word'].to_dict()


def write_freq(new_freq):  # Writes a new word_freq dict to a json file
    with open('files/word_frequency.json', 'w') as file:
        json.dump(new_freq, file)


def load_freq():  # Loads in the word_dict from files and returns it as a dictionary
    return pd.read_json('files/word_frequency.json', typ='series').to_dict()


def get_freq():
    try:  # Loading in word_freq list from files
        return load_freq()
    except:  # If no word_freq file, generate the frequency list and save
        return generate_frequency()


def generate_frequency():
    freq_list_df = pd.read_csv('files/unigram_freq.csv', header=0, index_col='word')
    freq_list_df['count'] = freq_list_df['count'].astype(float)
    freq_list = freq_list_df[freq_list_df.index.str.len() == 5]['count'].to_dict()
    for word in legal_guesses:
        word_freq[word] = freq_list.get(word, min(freq_list.values()))

    log_freq = {word: math.log(freq) for word, freq in word_freq.items()}
    # Calculating min and max log freq values
    min_log = min(log_freq.values())
    max_log = max(log_freq.values())
    epsilon = 1e-4
    for word in log_freq:
        # Normalizing log freq values
        normalized = (log_freq[word] - min_log) / (max_log + .01 - min_log)
        # Overwriting previous freq to new log normalized values
        word_freq[word] = epsilon + (1 - epsilon) * normalized
    del freq_list_df
    gc.collect()

    write_freq(word_freq)

    return word_freq


#  Performs required initialization to populate word_freq and legal_guesses variables
check_hashes()
load_explorer_lookup()
