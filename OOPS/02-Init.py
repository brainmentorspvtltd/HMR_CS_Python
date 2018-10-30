class Player():

    def  __init__(self):

        self.playerName = None
        self.playerHealth = None
        self.playerPower = None
        self.playerData = []

    def showPlayer(self):
        self.playerData.append([self.playerName,
                                self.playerHealth,
                                self.playerPower])
        print(self.playerData)

p_1 = Player()
p_1.playerName = 'Hulk'
p_1.playerHealth = 80
p_1.playerPower = 'Smash'
p_1.showPlayer()

p_2 = Player()
p_2.playerName = 'Thor'
p_2.playerHealth = 90
p_2.playerPower = 'Light'
p_2.showPlayer()