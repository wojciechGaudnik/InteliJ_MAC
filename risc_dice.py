from random import randrange

attacker = []
defender = []
lost_att = 0
lost_def = 0
min_len_of_dices = 0

for i in range(3):
	attacker.insert(i, randrange(1, 7))
	
for i in range(2):
	defender.insert(i, randrange(1, 7))
	
attacker.sort(reverse=True)
defender.sort(reverse=True)

print('Dice:')
print('     Attacker: ',end='')
for att in attacker:
	print(str(att) + '-', end='')
print('\b')
print('     Defender: ',end='')
for de in defender:
	print(str(de) + '-', end='')
print('\b')

if len(attacker) <= len(defender):
	min_len_of_dices = len(attacker)
else:
	min_len_of_dices = len(defender)

for i in range(min_len_of_dices):
	if attacker[i] <= defender[i]:
		lost_att += 1
	else:
		lost_def += 1


unit = 'units' if lost_att > 1 else 'unit'
print('Outcome:')
print('     Attacker: Lost', lost_att, unit)
unit = 'units' if lost_def > 1 else 'unit'
print('     Defender: Lost', lost_def, unit)

