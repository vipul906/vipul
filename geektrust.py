import sys
import re

class  BattalionRanked:
    def __init__(self):
        self.rank_vise_name = {1:'H' ,2: 'E', 3: 'AT', 4:'SG'}
        self.lowestRank = 9999
        self.rank = 0
        self.highestRank = -1

    def battalionRanked(self, rank):
        self.rank = rank

    def getRank(self):
        return self.rank

    def determinLowesAndHighesttRank(self):
        for val in self.rank_vise_name.valuews():
            if self.rank <self.lowestRank:
                self.lowestRank = self.rank
            if self.rank > self.highestRank:
                self.highestRank = self.rank

    def lowestRank(self):
        if self.lowestRank == 9999:
            self.determinLowesAndHighesttRank()	
	
	def highestRank(self):
		if self.highestRank == -1:
			self.determinLowesAndHighesttRank()

class WarResult:
    def __init__(self, army):
        battalion = self.removeAlpha(army)
        battalion_type = ['Horses', 'Elephants', 'Armoured', 'SlingGuns']
        lengaburu_battalion_count = [100, 50, 10, 5]
        self.lengaburu_battalion = dict(zip(battalion_type,lengaburu_battalion_count))
        self.falicornia_battalion = dict(zip(battalion_type,battalion))
        self.battalionPowerFactor = 2.0
        self.Rules = WarRules()
    
    def removeAlpha(self, army):
        battalion = map(lambda x:re.search(r'\d+',x).group(),army)
        battalion = map(int,battalion)
        return battalion       

    
    def is_Win(self):
        print (self.falicornia_battalion) 
        print (self.lengaburu_battalion)
        result = self.Rules.getResult(self.falicornia_battalion,self.lengaburu_battalion,self.battalionPowerFactor)

class Battalions:
    def __init__(self):
        pass

class SubstitutionRules:
    def __init__(self):
        pass

class WarRules:
    def __init__(self):
        pass

    def isSubstitutionBattalionsRequired (self, availableDefenders, actualDefendesBattalionsRequired):
        if (availableDefenders.get('Horses',0) >= actualDefendesBattalionsRequired.get('Horses',0) and (availableDefenders.get('Elephants',0) >= actualDefendesBattalionsRequired.getNumberOfElephants()) and (availableDefenders.getNumberOfArmoured() >= actualDefendesBattalionsRequired.getNumberOfArmoured()) and (availableDefenders.get('lingGuns() >= actualDefendesBattalionsRequired.get('SlingGuns',0)):
            return False
        return True
    
    def getAfterSubstitutionDefenderBattalionsRequired (availableDefenders, actualDefendesBattalionsRequired):
		afterSubstitutionDefenderBattalionsRequired = Battalions()
		afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses());
		afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants());
		afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured());
		afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns());
		if (availableDefenders.getNumberOfHorses() < actualDefendesBattalionsRequired.getNumberOfHorses()) {
			BattalionRanked temp = BattalionRanked.H;
			setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.getRank());
		}
		if (availableDefenders.getNumberOfElephants() < actualDefendesBattalionsRequired.getNumberOfElephants()) {
			BattalionRanked temp = BattalionRanked.E;
			setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.getRank());
		}
		if (availableDefenders.getNumberOfArmoured() < actualDefendesBattalionsRequired.getNumberOfArmoured()) {
			BattalionRanked temp = BattalionRanked.AT;
			setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.getRank());
		}
		if (availableDefenders.getNumberOfSlingGuns() < actualDefendesBattalionsRequired.getNumberOfSlingGuns()) {
			BattalionRanked temp = BattalionRanked.SG;
			setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.getRank());
		}
		return afterSubstitutionDefenderBattalionsRequired;
	}
    
    def calculateDefendersBattalionsRequired(self, attackers, availableDefenders, defenders_army_strongness_factor):
        actualDefendesBattalionsRequired = self.getActualDefendesBattalionsRequired(attackers, defenders_army_strongness_factor)
        if self.isSubstitutionBattalionsRequired(availableDefenders, actualDefendesBattalionsRequired):
            return getAfterSubstitutionDefenderBattalionsRequired(availableDefenders, actualDefendesBattalionsRequired)
        return actualDefendesBattalionsRequired

     def getResult(self, attackers, defenders, defenders_army_strongness_factor):
        requiredBattalionUnits = self.calculateDefendersBattalionsRequired(attackers, defenders, defenders_army_strongness_factor)
        return requiredBattalionUnits   



if __name__ == "__main__":
    filepath = sys.argv[1]
    f = open(filepath)
    input_data = f.read().split()
    battalion ,battalion_army = input_data[0],input_data[1:]
    obj = WarResult(battalion_army)
    obj.is_Win()

    

