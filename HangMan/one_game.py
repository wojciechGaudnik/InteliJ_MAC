# from HangMan.hangman_graf import Show_hangman
from hangman_graf import Show_hangman

import os
from timeit import default_timer as timer
import datetime
import pickle
from tabulate import tabulate

class One_Game(object):
	
	def __init__(self, words):
		self.added_leteres = []
		self.country = words[0]
		self.capital = list(words[1].upper())
		self.capital_buff = list(words[1].upper())
		self.capital_word = words[1].upper()
		self.dashed_capital = []
		self.lives = 5
		self.hag_graf = Show_hangman()
		self.time_start = timer()
		self.show_first = True
		self.guessing_tries = 0
		self.name = ''
		self.high_scores = pickle.load(open('hangman_scores.p', 'rb'))

		print(self.capital_word)
		input('')

		for ans in self.capital:
			if ans != ' ':
				self.dashed_capital += '_'
			else:
				self.dashed_capital += ' '
		#self.dashed_capital = list(self.dashed_capital)
		
	
	def guess_the_letter(self):
		self.guessing_tries += 1
		alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
		            'U', 'V', 'W', 'X', 'Y', 'Z')
		ans = input("letter:").capitalize()
		if len(ans) > 1:
			print('Enter one letter only')
			input('')
		else:
			if ans not in alphabet:
				print('This is not a letter, try again')
				input()
			else:
				if ans in self.added_leteres:
					self.lives -= 1
					print('You have already tried this letter, be cautious')
					input('')
				else:
					if ans in self.capital:
						while ans in self.capital:
							num = self.capital.index(ans)
							self.dashed_capital[num] = ans
							self.capital[num] = '*'
					elif ans in self.capital_buff:
						print('This letter was already guessed, press any key')
						input()
						self.lives -= 1
					else:
						self.added_leteres.append(ans)
						self.lives -= 1
			if self.lives < 1:
				self.game_over_lose()
			if '_' not in self.dashed_capital:
				self.game_over_win()
			
			
			
	def guess_the_capital(self):
		self.guessing_tries += 1
		ans = input("Capital:").upper()
		if ans == self.capital_word:
			self.game_over_win()
		else:
			print('It is not correct, press Enter')
			input()
			self.lives -= 2
	
	def show_progress_hangman(self):
		os.system('clear')
		if self.lives == 1:
			#self.show_first = False
			print('Capital of {} is ?'.format(self.country))
		else:
			print('')
		
		self.hag_graf.show_hangman(self.lives)
		print('Capital: ',' '.join(self.dashed_capital))
		print('Used letters:', ' '.join(self.added_leteres))
		print('Lives:', self.lives)
		time_now_sec = int((timer() - self.time_start) % 60)
		time_now_min = int((timer() - self.time_start) / 60)
		print('Guessing time: ', end='')
		print('{:02d}'.format(time_now_min), end='')
		print(':', end='')
		print('{:02d}'.format(time_now_sec))
		# print('You gessing: ' + str(int(time_now_min)) + ':' + str(int(time_now_sec)))
	
	def game_over_win(self):
		self.show_progress_hangman()
		self.lives = 0
		self.time_now_sec = int((timer() - self.time_start) % 60)
		self.time_now_min = int((timer() - self.time_start) / 60)
		print('You guessed the capital after {} tries. It took you {:02d}:{:02d} min:seconds'.
		      format(self.guessing_tries, self.time_now_min, self.time_now_sec))
		self.add_your_score()

	def add_your_score(self):
		self.name = input('What is your name? ')
		your_score = ['{:02d}:{:02d} min:sec'.format(self.time_now_min, self.time_now_sec), self.name, self.guessing_tries, self.capital_word, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
		high_score = self.high_scores
		high_score.append(your_score)
		high_score.sort(key = lambda x: x[0])
		pickle.dump(high_score, open('hangman_scores.p', 'wb'))
		self.display_high_score()

	def display_high_score(self):
		score_table = tabulate(self.high_scores)
		print(score_table)
		return score_table
		# print("Top Scores:")
		# for line in self.high_scores[:10]:
		# 	print((line[2] + ' - ' + '{:<15s}' + ' - ' + str(line[3]) + ' tries - ' + '{:<15s}' + ' - ' + line[1])
		# 	      .format(line[0], line[4]))

	def game_over_lose(self):
		self.show_progress_hangman()
		print('lose')
		self.display_high_score()	
	
	def print_w(self):
		print(self.lives)
		print(self.capital)
		print(self.dashed_capital)