import random

def log(s):
    if DEBUG:
        print(s)

DEBUG = False
mulligan_to = 1
max_mulls = 7 - mulligan_to    
num_iterations = 10 ** 5
on_draw =False

for mull_style in ['London']:
	print("----> We run the numbers for the London mulligan.")
	count_bazaar = 0
	cards_in_hand_when_keep = 0
	count_dredger_in_opener = 0
	count_hollow_in_opener = 0
	count_dredger_and_hollow_in_opener = 0
	count_hollow = 0
	count_hollow_multi = 0
	count_dredger = 0
	count_dredger_and_hollow = 0
	count_bazaar_multi = 0
	count_once = 0
	count_once_hollowbazaarfield = 0
	count_secondbazaarorfield = 0

	for iteration in range(num_iterations):
		log("==========================")
		if(iteration % 10000 == 0 and iteration>0):
			print ("Iteration number "+str(iteration)+". Current prob: "+ str(round(100 * count_bazaar / iteration,2))+"%")
		decklist = {
			'Bazaar': 4, 
			'Powder': 4, 
			'Hollow': 4,
			'Dredger': 12,
			'Other': 28,
			'Once': 4,
			'Field': 4,
		}
		number_mulls = 0
		mull_type = 'Regular'

		while True:
			cards_in_hand = {
				'Bazaar': 0, 
				'Powder': 0, 
				'Hollow': 0,
				'Dredger': 0,
				'Other': 0,
				'Once': 0,
				'Field': 0,
			}
			if (mull_type == 'Regular'):
				we_need_to_put_cards_on_bottom = True
				deck = []
				for card in decklist.keys():
					deck += [card] * decklist[card]
				random.shuffle(deck)
				number_cards_to_draw = 7

			elif (mull_type == 'Via Powder'):
				number_cards_to_draw = 7 - number_mulls
				we_need_to_put_cards_on_bottom = False
		
			#log(deck)
			for _ in range(number_cards_to_draw):
				cards_in_hand[deck.pop(0)] += 1
			description = str(cards_in_hand['Bazaar']) + " Bazaar, " + str(cards_in_hand['Powder']) + " Powder, " + str(cards_in_hand['Hollow']) + " Hollow, "
			description += str(cards_in_hand['Dredger']) + " Dredger, " + str(cards_in_hand['Once']) + " Once, and " + str(cards_in_hand['Other']) + " Other."
			log("We have an opening hand with " + description)
			if (number_mulls >= 7):
				log("Stop!")
				break
			elif (cards_in_hand['Bazaar'] >= 1):
				count_bazaar += 1
				log("Bazaar!")
				cards_in_hand_when_keep += 7 - number_mulls
				if (we_need_to_put_cards_on_bottom):
					if(number_mulls == 0):
						log("keeping 7")
					else:
						log("keeping less than 7, make decision here")
						put_on_bottom = {
							'Bazaar': 0,
							'Powder': 0, 
							'Hollow': 0,
							'Dredger': 0,
							'Other': 0,
							'Once': 0,
                                                	'Field': 0,
						}
						bottomed_so_far = 0
						put_on_bottom['Powder'] = min(number_mulls, cards_in_hand['Powder'])
						bottomed_so_far += put_on_bottom['Powder']
						put_on_bottom['Other'] = min(number_mulls - bottomed_so_far, cards_in_hand['Other'])
						bottomed_so_far += put_on_bottom['Other']
						put_on_bottom['Dredger'] = min(number_mulls - bottomed_so_far, cards_in_hand['Dredger'])
						bottomed_so_far += put_on_bottom['Dredger']
						put_on_bottom['Once'] = min(number_mulls - bottomed_so_far, cards_in_hand['Once'])
						bottomed_so_far += put_on_bottom['Once']
						put_on_bottom['Hollow'] = min(number_mulls - bottomed_so_far, cards_in_hand['Hollow'])
						bottomed_so_far += put_on_bottom['Hollow']
						put_on_bottom['Field'] = min(number_mulls - bottomed_so_far, cards_in_hand['Field'])
						bottomed_so_far += put_on_bottom['Field']
						put_on_bottom['Bazaar'] =  min(number_mulls - bottomed_so_far, cards_in_hand['Bazaar'])
						description = "We bottomed " + str(number_mulls) + " cards: " + str(put_on_bottom['Powder']) + " Powders,"+ str(put_on_bottom['Dredger']) + " Dredgers, "
						description += str(put_on_bottom['Once']) + " Once Upon a Times, " + str(put_on_bottom['Hollow']) + " Hollows, and " + str(put_on_bottom['Other']) + " other cards."
						log(description)
						#log(cards_in_hand)
						#log(put_on_bottom)
						cards_in_hand['Bazaar'] -= put_on_bottom['Bazaar']
						cards_in_hand['Powder'] -= put_on_bottom['Powder']
						cards_in_hand['Hollow'] -= put_on_bottom['Hollow']
						cards_in_hand['Dredger'] -= put_on_bottom['Dredger']
						cards_in_hand['Other'] -= put_on_bottom['Other']
						cards_in_hand['Once'] -= put_on_bottom['Once']
						cards_in_hand['Field'] -= put_on_bottom['Field']
						#log(cards_in_hand)
                                
				else:
					log("powdered into this, no decisions")
				if (cards_in_hand['Dredger'] >0):
					count_dredger_in_opener += 1
				if (cards_in_hand['Hollow'] >0 and number_mulls <5):
					count_hollow_in_opener += 1
				if (cards_in_hand['Hollow'] >0 and cards_in_hand['Dredger'] >0 and number_mulls <5):
					count_dredger_and_hollow_in_opener += 1
					#now time for drawing for turn, activating bazaar, and potential once upon a time
				#log(cards_in_hand)#after mulligan before game starts
				handsize = 7 - number_mulls
				for _ in range(2):
					cards_in_hand[deck.pop(0)] += 1
					handsize += 1
				if (on_draw):
					cards_in_hand[deck.pop(0)] += 1
					handsize += 1
				log(cards_in_hand)
				handsize -= cards_in_hand['Hollow'] + cards_in_hand['Bazaar'] + 3
				if (cards_in_hand['Once'] >0 and number_mulls < 5):
					count_once += 1
					cards_in_once = {
							'Bazaar': 0,
							'Powder': 0, 
							'Hollow': 0,
							'Dredger': 0,
							'Other': 0,
							'Once': 0,
							'Field': 0,
					}
					for _ in range(5):
						cards_in_once[deck.pop(0)] += 1
					log('OUAT, we see')
					log(cards_in_once)
					if (cards_in_once['Bazaar'] >= 1):
						cards_in_hand['Bazaar'] += 1
						count_once_hollowbazaarfield += 1
					elif (cards_in_once['Field'] >= 1):
						cards_in_hand['Field'] += 1
						count_once_hollowbazaarfield += 1
					elif (cards_in_once['Hollow'] >= 1):
						cards_in_hand['Hollow'] += 1
						count_once_hollowbazaarfield += 1
					elif(cards_in_once['Dredger'] >= 1):
						cards_in_hand['Dredger'] += 1
					log(cards_in_hand)
				if (cards_in_hand['Dredger'] >0):
					count_dredger += 1
				if (cards_in_hand['Hollow'] >0 and cards_in_hand['Dredger'] >0 and number_mulls < 5):
					count_dredger_and_hollow += 1
				if (cards_in_hand['Hollow'] >0 and number_mulls < 5):
					count_hollow += 1
				if (cards_in_hand['Hollow'] >1 and number_mulls < 4):
					count_hollow_multi += 1
				if (cards_in_hand['Bazaar'] > 1):
					count_bazaar_multi += 1
				if (cards_in_hand['Bazaar'] > 1 or cards_in_hand['Field'] > 0):
					count_secondbazaarorfield += 1
				
				
				break
			elif (cards_in_hand['Bazaar'] == 0 and cards_in_hand['Powder'] == 0 and number_mulls < max_mulls):
				number_mulls += 1
				mull_type = 'Regular'
				log("Reg mull! number_mulls: "+str(number_mulls))
			elif (cards_in_hand['Bazaar'] == 0 and cards_in_hand['Powder'] == 0 and number_mulls >= max_mulls):
				cards_in_hand_when_keep += 7 - number_mulls
				log("Stop!")
				break
			elif (cards_in_hand['Bazaar'] == 0 and cards_in_hand['Powder'] > 0):
				mull_type = 'Via Powder'
				put_on_bottom = {
					'Bazaar': 0,
					'Powder': 0, 
					'Hollow': 0,
					'Dredger': 0,
					'Other': 0,
                                        'Once': 0,
                                        'Field': 0,
				}
				if (we_need_to_put_cards_on_bottom):
					bottomed_so_far = 0
					put_on_bottom['Bazaar'] =  0 
					put_on_bottom['Field'] = min(number_mulls - bottomed_so_far, cards_in_hand['Field'])
					bottomed_so_far += put_on_bottom['Field']
					put_on_bottom['Powder'] = min(number_mulls - bottomed_so_far, cards_in_hand['Powder'] - 1)
					bottomed_so_far += put_on_bottom['Powder']
					put_on_bottom['Once'] = min(number_mulls - bottomed_so_far, cards_in_hand['Once'])
					bottomed_so_far += put_on_bottom['Once']
					put_on_bottom['Dredger'] = min(number_mulls - bottomed_so_far, cards_in_hand['Dredger'])
					bottomed_so_far += put_on_bottom['Dredger']
					put_on_bottom['Hollow'] = min(number_mulls - bottomed_so_far, cards_in_hand['Hollow'])
					bottomed_so_far += put_on_bottom['Hollow']
					put_on_bottom['Other'] = number_mulls - bottomed_so_far
				for card in decklist.keys():
					deck += [card] * put_on_bottom[card]
					decklist[card] -= cards_in_hand[card] - put_on_bottom[card]
				description = "We bottomed " + str(number_mulls) + " cards: " + str(put_on_bottom['Powder']) + " Powders, "+ str(put_on_bottom['Dredger']) + " Dredgers, "
				description += str(put_on_bottom['Once']) + " Once Upon a Times, " + str(put_on_bottom['Field']) + " Fields, "+ str(put_on_bottom['Hollow']) + " Hollows, and " + str(put_on_bottom['Other']) + " other cards." 
				log("Powder mull! " + description)
				description = "We exiled "+ str(7 - number_mulls) + " cards: " + str(cards_in_hand['Powder'] - put_on_bottom['Powder']) + " Powders, "
				description += str(cards_in_hand['Dredger'] - put_on_bottom['Dredger']) + " Dredgers, "+ str(cards_in_hand['Once'] - put_on_bottom['Once']) + " Once Upon a Times, "
				description += str(cards_in_hand['Field'] - put_on_bottom['Field']) + " Fields, " + str(cards_in_hand['Other'] - put_on_bottom['Other']) + " other cards, and "+ str(cards_in_hand['Hollow'] - put_on_bottom['Hollow']) + " Hollows."
				log(description)
									
	print('Probability to keep at least one Bazaar of Baghdad: ' + str(round(100 * count_bazaar / num_iterations,2))+"%")
	print('Expected number of cards in hand when keeping: ' + str(round(cards_in_hand_when_keep / num_iterations,2)))
	print('Probability to keep at least one dredger: ' + str(round(100 * count_dredger_in_opener / num_iterations,2))+"%")
	print('Probability to keep at least one Hollow One: ' + str(round(100 * count_hollow_in_opener / num_iterations,2))+"%")
	print('Probability to keep at least one Hollow One and one dredger: ' + str(round(100 * count_dredger_and_hollow_in_opener / num_iterations,2))+"%")
	print('Probability to find at least one Once Upon a Time: ' + str(round(100 * count_once / num_iterations,2))+"%")
	if (count_once > 0):
		print('Probability to find Bazaar, Field or Hollow one, given Once Upon a Time: ' + str(round(100 * count_once_hollowbazaarfield / count_once,2))+"%")
	print('Probability to find at least one dredger: ' + str(round(100 * count_dredger / num_iterations,2))+"%")
	print('Probability to find at least one Hollow One: ' + str(round(100 * count_hollow / num_iterations,2))+"%")
	print('Probability to find at least one Hollow One and one dredger: ' + str(round(100 * count_dredger_and_hollow / num_iterations,2))+"%")
	print('Probability to find at least two Hollow Ones: ' + str(round(100 * count_hollow_multi / num_iterations,2))+"%")
	print('Probability to find at least two Bazaars: ' + str(round(100 * count_bazaar_multi / num_iterations,2))+"%")
	print('Probability to find at least two Bazaars or a Bazaar and a Field: ' + str(round(100 * count_secondbazaarorfield / num_iterations,2))+"%")
