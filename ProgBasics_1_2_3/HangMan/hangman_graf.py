class Show_hangman(object):
    def show_hangman(self, lives):
        if lives == 5: self.__show_hangman5()
        if lives == 4: self.__show_hangman4()
        if lives == 3: self.__show_hangman3()
        if lives == 2: self.__show_hangman2()
        if lives == 1: self.__show_hangman1()
        if lives == 0: self.__show_hangman0()
        
    def __show_hangman5(self):
        print('\n\n\n\n\n\n\n')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    def __show_hangman4(self):
        print('\n\n\n\n')
        print('   |  ')
        print(' __|_ ')
        print('/||||\\')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

    def __show_hangman3(self):
        print('   ________')
        print('   | / ')
        print('   |/')
        print('   | ')
        print('   | ')
        print('   | ')
        print(' __|_')
        print('/||||\\')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
    def __show_hangman2(self):
        print('   ________')
        print('   | /     |')
        print('   |/      O')
        print('   | ')
        print('   | ')
        print('   | ')
        print(' __|_')
        print('/||||\\')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
    def __show_hangman1(self):
        print('   ________')
        print('   | /     |')
        print('   |/      O')
        print('   |      /|\\')
        print('   |       |')
        print('   | ')
        print(' __|_')
        print('/||||\\')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
    def __show_hangman0(self):
        print('   ________')
        print('   | /     |')
        print('   |/      O')
        print('   |      /|\\')
        print('   |       |')
        print('   |      / \\')
        print(' __|_')
        print('/||||\\')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
#    ________
#    | /     |
#    |/      O
#    |      /|\
#    |       |
#    |      / \
#  __|_
# /||||\