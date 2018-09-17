from random import randrange

attacker = []
defender = []
qua_att = 0
qua_def = 0
lost_att = 0
lost_def = 0
min_len_of_dices = 0

while not attacker:
	try:
		qua_att = int(input('How many units attack:'))
		if qua_att == 0:
			qua_att /= 0
		for i in range(qua_att):
			attacker.insert(i, randrange(1, 7))
	except:
		qua_att = 0
		
while not defender:
	try:
		qua_def = int(input('How many units defend:'))
		if qua_def == 0:
			qua_def /= 0
		for i in range(qua_def):
			defender.insert(i, randrange(1, 7))
	except:
		qua_def = 0

	
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

