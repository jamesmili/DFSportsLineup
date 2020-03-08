import csv
from collections import OrderedDict

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
        if player[0] in self.PLAYERS:
            self.PLAYERS[player[0]]['frequency'] += 1
        else:
            self.PLAYERS[player[0]] = { 
                                        'frequency': 0,
                                        'pos': player[1],
                                        'drafted': player[2],
                                        'total_points': player[3]
                                    }

    def read(self):
        with open('contest-standings-86385131.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            #skips header line
            csv_reader.__next__()
            counter = 1
            for row in csv_reader:
                players = row[7::]
                lineup = row[5]
                if '' not in players:
                    self.addPlayer(players)
                if counter is not self.PLACEMENTS:
                    self.LINEUPS.append(self.filterLineup(lineup))
                    counter += 1
        self.TOPPLAYERS = self.PLAYERS
        
    def calculate(self, num=None):
        print(num)
        self.TOPPLAYERS = self.PLAYERS
        if num is not None:
            lineups = self.LINEUPS[num-1]
        else:
            lineups = self.LINEUPS
        for lineup in lineups:
            for player in lineup:
                self.TOPPLAYERS[player]['frequency'] += 1

    def getPlayers(self):
        return self.TOPPLAYERS

    def getLineups(self):
        return self.LINEUPS
    
    def getFrequentPlayers(self):
        return {k: v for k, v in sorted(self.TOPPLAYERS.items(), key=lambda item: item[1]['frequency'], reverse=True)}


if __name__ == "__main__":
    f = Frequency(10)
    f.read()
    f.calculate()
    print(f.getFrequentPlayers())
