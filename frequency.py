import csv, sys, os

class Frequency:
    def __init__(self, placements):
        self.PLACEMENTS  = placements
        self.PLAYERS = dict()
        self.LINEUPS = []
        self.TOPPLAYERS = dict()

    def filterLineup(self, lineup):
        split_lineup = lineup.split()
        pos = 2
        indeces = []
        # removes PG SG SF PF C G F UTIL from list
        positions = ["PG", "SG", "SF", "PF", "C", "G" , "F", "UTIL"]
        for pos in positions:
            index = split_lineup.index(pos)
            indeces.append(index)
        indeces = sorted(indeces)
        players = []
        for i in range(len(indeces)-2):
            players.append(split_lineup[indeces[i]+1] + " " + split_lineup[indeces[i+1]-1])
        players.append(split_lineup[indeces[-1]+1] + " " + split_lineup[-1]) 
        return players

    def addPlayer(self, player):
        if player[0] not in self.PLAYERS:
            self.PLAYERS[player[0]] =   { 
                                            'frequency': 0,
                                            'drafted': player[2],
                                            'average_points': float(player[3])
                                        }
        else:
            average_points = round((self.PLAYERS[player[0]]['average_points'] + float(player[3])) / 2, 2)
            self.PLAYERS[player[0]]['average_points'] = average_points

    def addPlayerFrequency(self, player):
        if player in self.TOPPLAYERS:
            self.TOPPLAYERS[player]['frequency'] += 1

    def read(self, path):
        print("reading files from: " + path)
        self.LINEUPS=[]
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            #skips header line
            csv_reader.__next__()
            for row in csv_reader:
                players = row[7::]
                lineup = row[5]
                if '' not in players:
                    self.addPlayer(players)
                if len(lineup) is not 0:
                    self.LINEUPS.append(self.filterLineup(lineup))
                else: break
        self.TOPPLAYERS = self.PLAYERS
        self.calculate()
        
    def calculate(self):
        self.TOPPLAYERS = self.PLAYERS
        if self.PLACEMENTS is not 0:
            lineups = self.LINEUPS[0:self.PLACEMENTS]
        else:
            lineups = self.LINEUPS
        for lineup in lineups:
            for player in lineup:
                self.addPlayerFrequency(player)

    def getPlayers(self):
        return self.TOPPLAYERS

    def getLineups(self):
        return self.LINEUPS
    
    def getFrequentPlayers(self):
        return {k: v for k, v in sorted(self.TOPPLAYERS.items(), key=lambda item: item[1]['frequency'], reverse=True) if v['frequency'] is not 0}


if __name__ == "__main__":
    path = sys.argv[1]
    placements = int(sys.argv[2])
    f = Frequency(placements)
    for files in os.listdir(path):
        f.read(path+"/"+files)
    print(f.getFrequentPlayers())
