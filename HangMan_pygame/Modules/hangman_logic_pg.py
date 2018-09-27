from timeit import default_timer as timer
import datetime
import pickle

class One_Game(object):
	
	def __init__(self, words):
		self.added_leteres = []
		self.country = words[0]
		self.capital = list(words[1].upper())
		self.capital_buff = list(words[1].upper())
		self.capital_word = words[1].upper()
		self.dashed_capital = []
		self.lives = 5
		self.time_start = timer()
		self.show_first = True
		self.guessing_tries = 0
		self.name = ''
		self.high_scores = pickle.load(open('hangman_scores.p', 'rb'))
		
		print(self.capital_word)
		
		for ans in self.capital:
			if ans != ' ':
				self.dashed_capital += '_'
			else:
				self.dashed_capital += ' '
		self.dashed_capital = list(self.dashed_capital)
		
	
	def guess_the_letter(self, ans):
		self.guessing_tries += 1
		if ans in self.capital:
			while ans in self.capital:
				num = self.capital.index(ans)
				self.dashed_capital[num] = ans
				self.capital[num] = '*'
			self.added_leteres.append(ans)
		else:
			self.added_leteres.append(ans)
			self.lives -= 1
		if self.lives < 1:
			return 'lose'
		elif '_' not in self.dashed_capital:
			return 'win'
		else:
			return 'ask_w_l'
			
			
	def guess_the_capital(self, word):
		self.guessing_tries += 1
		if word == self.capital_word:
			self.time_now_sec = int((timer() - self.time_start) % 60)
			self.time_now_min = int((timer() - self.time_start) / 60)
			return 'win'
		else:
			self.lives -= 2
			
			if self.lives < 1:
				return 'lose'
			else:
				return  'ask_w_l'
	
	
	def show_progress_hangman(self):
		time_now_sec = int((timer() - self.time_start) % 60)
		time_now_min = int((timer() - self.time_start) / 60)
		
		show_progress = []
		show_progress.append('Capital: ' + ''.join(self.dashed_capital))
		show_progress.append('Guessing_tries:' + str(self.guessing_tries))
		show_progress.append(''.join('Guessing time: {:02d} : {:02d}'.format(time_now_min, time_now_sec)))
		show_progress.append('Answer is: ' + self.capital_word)
		# show_progress.append(self.high_scores)
		return show_progress
	
	
	def game_over_win(self):
		self.show_progress_hangman()
		self.lives = 0
		self.time_now_sec = int((timer() - self.time_start) % 60)
		self.time_now_min = int((timer() - self.time_start) / 60)
		print('You guessed the capital after {} tries. It took you {:02d}:{:02d} min:seconds'.
		      format(self.guessing_tries, self.time_now_min, self.time_now_sec))
		self.add_your_score()


	def add_your_score(self, name):
		# self.name = input('What is your name? ')
		self.name = name
		print(self.name)
		your_score = [self.name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '{:02d}:{:02d} min:sec'.format(self.time_now_min, self.time_now_sec), self.guessing_tries, self.capital_word]
		high_score = self.high_scores
		high_score.append(your_score)
		high_score.sort(key = lambda x: x[2])
		pickle.dump(high_score, open('hangman_scores.p', 'wb'))
		print('end add score')
		# self.display_high_score()


	# def display_high_score(self):
	# 	print("Top Scores:")
	# 	for line in self.high_scores[:10]:
	# 		print((line[2] + ' - ' + line[0] + ' - ' + str(line[3]) + ' - ' + line[4] + ' - ' + line[1]))
			
	def display_high_score(self):
		high_score = []
		high_score.append("Top Scores:")
		for line in self.high_scores[:3]: #todo <----------------------- dodaj limit wyświetlanych wynikóœ
			high_score.append(line)
		print('end display high score')
		return high_score
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