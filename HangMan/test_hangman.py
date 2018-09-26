import pickle

#from from_file import random_words

import os

# os.system('clear')

def display_high_score():
    print("Top Scores:")
    for line in pickle.load(open('hangman_scores.p', 'rb'))[:10]:
        print((line[2] + ' - ' + '{:<10s}' + ' - ' + str(line[3]) + ' - ' + '{:<15s}' + ' - ' + line[1]).format(line[0], line[4]))
        # print('{:<10s}'.format(line[0]))



display_high_score()



# 00:16 min:sec - Mare - 6 - KABUL - 2018-09-26 13:27:12