import csv

class Frequency:
    def __init__(self, placements):
        self.PLACEMENTS  = 10
        self.PLAYERS = dict()
        self.LINEUPS = []

    def filterLineup(self, lineup):
        split_lineup = lineup.split()
        pos = 2
        # removes PG SG SF PF C G F UTIL from list
        positions = ["PG", "SG", "SF", "PF", "C", "G" , "F", "UTIL"]
        for pos in positions:
            index = split_lineup.index(pos)
            del split_lineup[index]
        return split_lineup

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
            counter = 0
            for row in csv_reader:
                players = row[7::]
                lineup = row[5]
                if len(players) > 2:
                    self.addPlayer(players)
                if counter is not self.PLACEMENTS:
                    self.LINEUPS.append(self.filterLineup(lineup))
                    counter += 1
                else:
                    break

    def getPlayers(self):
        return self.PLAYERS

    def getLineups(self):
        return self.LINEUPS

if __name__ == "__main__":
    f = Frequency(10)
    f.read()
    f.getPlayers()
    f.getLineups()