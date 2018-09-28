from timeit import default_timer as timer
import datetime, pickle, pygame, time
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
		self.time_start = timer()
		self.show_first = True
		self.guessing_tries = 0
		self.name = ''
		
		
			
		try:
			with open('Data/hangman_scores.p', 'rb') as f:
				self.high_scores = pickle.load(f)
				f.close()
		except:
			with open('Data/hangman_scores.p', 'wb') as f:
				pickle.dump([], f, protocol=pickle.HIGHEST_PROTOCOL)
				f.close()
				
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
			self.__play_klick_ok()
			while ans in self.capital:
				num = self.capital.index(ans)
				self.dashed_capital[num] = ans
				self.capital[num] = '*'
			self.added_leteres.append(ans)
		else:
			self.__play_klick_wrong()
			self.added_leteres.append(ans)
			self.lives -= 1
		if self.lives < 1:
			return 'lose'
		elif '_' not in self.dashed_capital:
			self.time_now_sec = int((timer() - self.time_start) % 60)
			self.time_now_min = int((timer() - self.time_start) / 60)
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
		return show_progress


	def add_your_score(self, name):
		self.name = name
		your_score = ['{:02d}:{:02d} min:sec'.format(self.time_now_min, self.time_now_sec), self.name, self.guessing_tries, self.capital_word, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
		high_score = self.high_scores
		high_score.append(your_score)
		high_score.sort(key = lambda x: x[0])
		f = open('Data/hangman_scores.p', 'wb')
		pickle.dump(high_score, f)
		f.close()
		self.display_high_score()
	
		
	def display_high_score(self):
		score_table = tabulate(self.high_scores[:10], headers=['TIME', 'PLAYER', 'TRIES', 'CAPITAL', 'DATE'],
		                       tablefmt='grid')
		score_table = score_table.split('\n')
		return score_table
	
	
	def __play_klick_wrong(self, sound='Sounds/start.wav'):
		play_sound = pygame.mixer.Sound(sound)
		play_sound.play()
		time.sleep(0.3)
		play_sound.stop()
	
	
	def __play_klick_ok(self, sound='Sounds/ok.wav'):
		play_sound = pygame.mixer.Sound(sound)
		play_sound.play()
		time.sleep(0.3)
		play_sound.stop()
