import random

#this function returns a random hand for either the dealer or player, x is how many cards are needed
class cards:
	
	def __init__(self):
		deck=[]

	def shuffled_deck(self):
		deck = []
		for suit in ['Clubs','Diamonds','Hearts','Spades']:
			for num in range(2, 15):
				deck.append([num, suit])
		
		random.shuffle(deck)
		return deck
			
	def Deal(self,x,y): 
			deck = x
			#cards = 1
			players = (y*2)-1 
			count = 0
			playhand = []
			househand = []
			ucards=[]
			hand = []
			print(len(deck))
			while count <= players:
				card = random.randint(0,51)
				if card not in ucards: 
					playhand.append(deck[card])
					count +=1
					ucards.append(card)
					print(card)
				else :
					count = count
					#the two lines were used to test and insure it was kicking out duplicate cards
					#print(card)
					#print("Caught one!")
					
			count=0
			while count <= 2:
				card = random.randint(0,51)
				if card not in ucards: 
					househand.append(deck[card])
					count +=1
					ucards.append(card)
				else :
					count = count
					#the two lines were used to test and insure it was kicking out duplicate cards
					#print(card)
					#print("Caught one!")
					
			hand = playhand + househand
			return hand

def startgame(players):
	rank = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack",12:"Queen",13:"King",14:"Ace"}
	x = cards()
	deck = x.shuffled_deck()
	dealed = x.Deal(deck,players)
	
	topend=(players*2)-1
	
	count =0
	playerbet=[] #should be a global variable, since this will need to be accessed by many parts
	for i in range(0,players):
		
		player=str(i+1)
		print("Player " + player + " Your cards are: \n")
		
		for ii in range(count,(count+2)):
			print(rank[dealed[ii][0]]+" of "+dealed[ii][1])
			count+=1
		answer = "sure"
		ante = str(raw_input("Player"+player+" Would you like to ante?"))
		if ante == answer:
			
			playerbet.append(int(raw_input("What would you like to bet? (5, 10, or  15)")))
			print(playerbet)
		else:
			print("Thanks for playing!")
	
	
	print(dealed)			
			
startgame(2)