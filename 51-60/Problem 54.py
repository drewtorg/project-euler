import operator

class Card:

	def __init__(self, rank, suit):

		self.rank = 0
		self.suit = ''

		#convert the rank to an integer
		if rank == 'A':
			self.rank = 14
		elif rank == 'K':
			self.rank = 13
		elif rank == 'Q':
			self.rank = 12
		elif rank == 'J':
			self.rank = 11
		elif rank == 'T':
			self.rank = 10
		else:
			self.rank = int(rank)

		#convert the suit to a word so it's easier to read
		if suit == 'H':
			self.suit = 'Hearts'
		elif suit == 'S':
			self.suit = 'Spades'
		elif suit == 'C':
			self.suit = 'Clubs'
		else:
			self.suit = 'Diamonds'

class Poker:

	def __init__(self,cardList):
		self.cards = []

		self.cards.extend(cardList.pop(0).split())
		self.hand1 = []
		self.hand2 = []

		for i in xrange(0, 5):
			self.hand1.append(Card(self.cards[i][0],self.cards[i][1]))
			self.hand2.append(Card(self.cards[i+5][0],self.cards[i+5][1]))

	def play_round(self):
		if self.get_score(self.hand1) > self.get_score(self.hand2):
			return True
		return False

	def get_score(self, hand):
		#make a dictionary containing the count of each each
		cardCount = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}

		for card in hand:
			cardCount[card.rank] += 1

		#count number of unique cards
		uniqueCount = 0
		for rankCount in cardCount.values():
			if rankCount > 0:
				uniqueCount += 1

		straight = self.is_straight(hand)
		flush = self.is_flush(hand)

		points = 0
		if uniqueCount == 2:
			if max(cardCount.values()) == 4:
				points = 8 #four of a kind (2 uniques and 4 are the same)
			elif max(cardCount.values()) == 3:
				points = 7 #full house (2 unique and 3 are the same)

		elif uniqueCount == 3:
			if max(cardCount.values()) == 3:
				points = 4 #three of a kind (3 unique and 3 are the same)
			elif max(cardCount.values()) == 2:
				points = 3 #two pair (3 uniques and 2 are the same)

		elif uniqueCount == 4:
			if max(cardCount.values()) == 2:
				points = 2 #one pair (4 uniques and 2 are the same)

		elif uniqueCount == 5:
			points = 1 #high card 

		if straight and flush:
			points = max(points, 9) #straight flush
		elif flush and not straight:
			points = max(points, 6) #flush
		elif not flush and straight:
			points = max(points, 5) #straight

		sorted_cardCount = sorted(cardCount.iteritems(), key=operator.itemgetter(1,0), reverse=True)
		for keyval in sorted_cardCount:
			if keyval[1] != 0:
				points = int(str(points) + (keyval[1] * str(keyval[0]).zfill(2)))

		return points


	def is_straight(self,hand):
		values = []
		for card in hand:
			values.append(card.rank)

		values.sort()
		min = values[0]
		for i in xrange(1,6):
			if min + 1 != values[i]:
				return False
		return True

	def is_flush(self,hand):
		suit = hand[0].suit
		for card in hand:
			if card.suit != suit:
				return False
		return True

def play_many_rounds(limit):

	f = open("poker.txt")
	cardList = list(f)

	player1_score = 0
	player2_score = 0

	for i in xrange(0, limit):
		round = Poker(cardList)
		if round.play_round() == True:
			player1_score += 1
		else:
			player2_score += 1

	print 'Player 1 won ' + str(player1_score) + ' rounds'
	print 'Player 2 won ' + str(player2_score) + ' rounds'

play_many_rounds(1000)