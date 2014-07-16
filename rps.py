"""
	rock-paper-scissors
	Bae_ggotgeuleegosol
"""
from random import randint, sample

class RockPaperScissors(object):
	matchCount = 0
	playerList = []
	winnerList = []

	__rpsDics = { "0":"rock", "1":"paper", "2":"scissors"}

	def playStart(self):
		memberNum = raw_input("members number : ")

		try :
			memberNum = int(memberNum)
			
			if memberNum >= 2 and memberNum <= 26 : 
				for i in range(memberNum):
					self.playerList.append(chr(65+i)) # ord('A') : 65, chr(65) : A

				randomIdxList = self.__getRandomIdxList(memberNum)

				while ( len(randomIdxList) != 1 ):
					# if len(self.winnerList) != 0 :
					# 	self.playList = copy.copy(self.winnerList)
					# 	print "30 : " + str(self.playerList)
					# 	print "31 : " + str(self.winnerList)

					self.matchCount += 1 
					self.__printMatches(randomIdxList) #match print
					self.__rpsPlay(randomIdxList) #rps play
					randomIdxList = self.__getRandomIdxList(len(self.winnerList)) # get randomIdxList again with winnerList				

				if len(randomIdxList) == 1 : # after all matches
					print "------------------------------"
					print "Final Winner : " + str(self.winnerList)
			else :
				print "Can't play with %d" % (memberNum)	
		except ValueError:
			print "Wrong type"
			print "Bye"
		
	def __getRandomIdxList(self, memberNum): # make a ramdon index list
		# between 0~(memberNum-1), the number of memberNum
		mbNumRandomIdx = sample(range(memberNum), memberNum) 
		return mbNumRandomIdx

	def __printMatches(self, randomIdxList): # print all matches
		print "---------- " + str(self.matchCount) + "round ----------"

		if len(randomIdxList) %2 != 0 : # odd
			for i in range(0, len(randomIdxList)-1, 2):
				print "( " + self.playerList[randomIdxList[i]] + "-" + self.playerList[randomIdxList[i+1]] + " )",
			print ", " + str(self.playerList[randomIdxList[len(randomIdxList)-1]])+ " won by default"
		else :	# even
			for i in range(0, len(randomIdxList), 2):
				print "( " +self.playerList[randomIdxList[i]] + "-" + self.playerList[randomIdxList[i+1]] + " )",
			print	

	def __rpsPlay(self, randomIdxList): # rps Play

		if len(self.winnerList) != 0 : # initialize the winnerList
			self.winnerList = []

		if len(randomIdxList) %2 != 0 : # odd
			self.winnerList.append(self.playerList[randomIdxList[len(randomIdxList)-1]]) # an unearned winner 

			for i in range(0, len(randomIdxList)-1,  2) :				
				result = "none"
				while ( result == "none" ):
					result = self.__checkWinner(randomIdxList[i], randomIdxList[i+1]) # parameter : players' index				
					if result != "none" :
						self.winnerList.append(result) # result -> alphabet

			print "winner list : " + str(self.winnerList)
			self.playerList = self.winnerList[ : ] # in the next match, the winnerList is to be a playerList 
		else :		# even
			for i in range(0, len(randomIdxList), 2) :
				result = "none"
				while (result == "none" ):
					result = self.__checkWinner(randomIdxList[i], randomIdxList[i+1])				
					if result != "none" :
						self.winnerList.append(result)
			print "winner list : " + str(self.winnerList)
			self.playerList = self.winnerList[ : ] # in the next match, the winnerList is to be a playerList

	def __checkWinner(self, player1, player2): # check winner with two players
		# 0 : rock, 1 : paper, 2: scissors
		player1Result = randint(0, 2)
		player2Result = randint(0, 2)

		#print "rps result : " + str(player1Result) + ", " + str(player2Result)

		if player1Result == player2Result: # tie
			return "none"
		elif player1Result == 0 :
			if player2Result == 1 : #player2 win
				print self.playerList[player2] + "(win: " + self.__rpsDics[str(player2Result)] + ") - " + self.playerList[player1] + "(lose: " + self.__rpsDics[str(player1Result)] + ")"
				return self.playerList[player2]
			else : 			   #player1 win
				print self.playerList[player1] + " (win: "+ self.__rpsDics[str(player1Result)]  +") - " + self.playerList[player2] + " (lose: " + self.__rpsDics[str(player2Result)] + ")"
				return self.playerList[player1]
		elif player1Result == 1 :
			if player2Result == 2 : #player2 win
				print self.playerList[player2] + " (win: " + self.__rpsDics[str(player2Result)] + ") - " + self.playerList[player1] + " (lose: " + self.__rpsDics[str(player1Result)] + ")"
				return 	self.playerList[player2]
			else : 			   #player1 win
				print self.playerList[player1] + " (win: "+ self.__rpsDics[str(player1Result)]  +") - " + self.playerList[player2] + " (lose: " + self.__rpsDics[str(player2Result)] + ")"
				return self.playerList[player1]	
		elif player1Result == 2 :
			if player2Result == 0 : #player2 win
				print self.playerList[player2] + " (win: " + self.__rpsDics[str(player2Result)] + ") - " + self.playerList[player1] + " (lose: " + self.__rpsDics[str(player1Result)] + ")"
				return self.playerList[player2]
			else :	                        #player1 win
				print self.playerList[player1] + " (win: "+ self.__rpsDics[str(player1Result)]  +") - " + self.playerList[player2] + " (lose: " + self.__rpsDics[str(player2Result)] + ")"
				return self.playerList[player1]					


rockPaperScissorsTest = RockPaperScissors()
rockPaperScissorsTest.playStart()
