import pickle
from tabulate import tabulate

# table= pickle.load(open('/home/marek/Dokumenty/Codecool/WG repo/CodeCoolPython/HangMan/hangman_scores_old.p', 'rb'))
table= pickle.load(open('hangman_scores_old.p', 'rb'))

print(table)

print(tabulate(table))

table2 = tabulate(table)

print(table2)