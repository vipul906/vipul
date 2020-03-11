import sys
import re

class  BattalionRanked:
    def __init__(self,name):
        self.lowestRank = 9999
        self.rank = self.getRank(name)
        self.highestRank = -1

    def getRank(self,name):
        nameViseRankDict = {'H': 1, 'E': 2, 'AT':3, 'SG':4}
        rank = rank_vise_name.get(name,-1)
        return rank

    def getName(self,rank):
        rankViseNameDict = {1: 'H', 2: 'E', 3: 'AT', 4: 'SG'}
        return rankViseNameDict.get(rank,'')

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
        defender_army_dict = dict(zip(battalion_type,lengaburu_battalion_count))
        self.lengaburu_battalion = Battalions(defender_army_dict)
        self.falicornia_battalion = Battalions(battalion)
        self.battalionPowerFactor = 2.0
        self.Rules = WarRules()
    
    def removeAlpha(self, army):
        battalion = map(lambda x:re.findall(r'(\d+)([A-Z]+)',x)[0][::-1],army)
        battalion = dict(battalion)
        return battalion       
    
    def is_Win(self):
        print (self.falicornia_battalion) 
        print (self.lengaburu_battalion)
        result = self.Rules.getResult(self.falicornia_battalion,self.lengaburu_battalion,self.battalionPowerFactor)

class Battalions:
    def __init__(self,army_dict={}):
        self.set_army(army_dict)

    def set_army(self,army_dict):
        for armytype,count in army_dict.items():
            if armytype in ('E','Elephants'):
                self.Elephants = count
            elif armytype in ('H','Horses'):
                self.Horses = count
            elif armytype in ('AT','Armoureds'):
                self.Armoureds = count
            elif armytype in ('SG','SlingGuns'):
                self.SlingGuns = count

    def setNumberOfHorses(self,Horses):
        self.Horses = Horses

    def setNumberOfElephants(self,Elephants):
        self.Elephants = Elephants

    def setNumberOfArmoured(self, Armoureds):
        self.Armoureds = Armoureds

    def setNumberOfSlingGuns(self, SlingGuns):
        self.SlingGuns = SlingGuns
        
class SubstitutionRule:
    def __init__(self):
        self.H = BattalionRanked('H')
	self.E = BattalionRanked('E')
	self.AT = BattalionRanked('AT')
	self.SG = BattalionRanked('SG')
        self.run()

    def run(self):
        self.SubstitutionRuleMap = {}
        #Map<Integer,Integer> temp1 = new HashMap<>();
        temp1 = {}
        temp2 = {}
        temp3 = {}
        temp4 = {}
	#	Map<Integer,Integer> temp2 = new HashMap<>();
	#	Map<Integer,Integer> temp3 = new HashMap<>();
        #	Map<Integer,Integer> temp4 = new HashMap<>();
	#temp1.put(E.getRank(),2);
        temp1[self.E.rank] = 2
        #SubstitutionRuleMap.put(H.getRank(),temp1);
        self.SubstitutionRuleMap[self.H.rank] = temp1
        temp2[self.H.rank] = 2
        temp2[self.AT.rank] = 2
        Self.SubstitutionRuleMap[self.E] = temp2]

	#	temp2.put(H.getRank(),2);
        #	temp2.put(AT.getRank(),2);
	#	SubstitutionRuleMap.put(E.getRank(),temp2);

	#	temp3.put(E.getRank(),2);
        #		temp3.put(SG.getRank(),2);
	#	SubstitutionRuleMap.put(AT.getRank(),temp3);

        temp3[self.E.rank] = 2
        temp3[self.SG.rank] = 2
        self.SubstitutionRuleMap[self.AT.rank]=temp3


	#	temp4.put(AT.getRank(),2);
	#	SubstitutionRuleMap.put(SG.getRank(),temp4);

        temp4[self.AT.rank] = 2
        self.SubstitutionRuleMap[self.SG.rank] = temp4

    def getSubstitutionRules(self):
        return SubstitutionRuleMap

class WarRules:
    def __init__(self):
        pass

    def setAfterSubstitutionDefenderBattalionsRequired(self, afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, rankOfBattalion):
        substitutionRequiredForBattalionName = BattalionRanked('').getName(rankOfBattalion)
        #BattalionRanked substitutionRequiredBattalion = null;
        
        if substitutionRequiredForBattalionName == 'H':
            afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(availableDefenders.Horses)
            substitutionRequiredBattalion = BattalionRanked('H')
        
        elif substitutionRequiredForBattalionName == "E":
            afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(availableDefenders.Elephants)
            substitutionRequiredBattalion = BattalionRanked('E')

        elif substitutionRequiredForBattalionName == "AT":
            afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(availableDefenders.Armoured)
            substitutionRequiredBattalion = BattalionRanked('AT')
            
        elif substitutionRequiredForBattalionName == "SG":
            afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(availableDefenders.SlingGuns)
            substitutionRequiredBattalion = BattalionRanked("SG")
            
            
        #Map<Integer,Integer> temp =new TreeMap<Integer,Integer>( SubstitutionRule.getSubstitutionRules().get(rankOfBattalion));
        temp = SubstitutionRule().getSubstitutionRules().get(rankOfBattalion)
	#	for (Map.Entry<Integer, Integer> entry : temp.entrySet())  {

        for entry, values in temp.items():
            substituteBattalionName = BattalionRanked('').getName(int(entry))
            #substituteBattalion = BattalionRanked('H')
	    #		switch (substituteBattalionName) {
            if substituteBattalionName == 'H':
                #case "H" : {
		substituteBattalion = BattalionRanked('H')
                #switch (substitutionRequiredForBattalionName) {
                if substitutionRequiredForBattalionName == 'H':
                    #case "H" : {
#//		    substitutionRequiredBattalion = BattalionRanked('H')
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Horses - availableDefenders.Horses
                    if (afterSubstitutionDefenderBattalionsRequired.Horses < availableDefenders.Horses):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if(((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= numberOfSubstitutionRequired * (int(value)))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + numberOfSubstitutionRequired * int(value))
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses - numberOfSubstitutionRequired)
                             else:
                                 tempNumber = int(Math.floor((availableDefenders.Horses - afterSubstitutionDefenderBattalionsRequired.Horses)/int(value)))
                                 actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses - tempNumber)
                                 afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + tempNumber * (int(value)))
                        else:
                            if(((availableDefenders.Horses - afterSubstitutionDefenderBattalionsRequired.Horses) >= int(Math.ceil((double)numberOfSubstitutionRequired / (int(value)))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses - tempNumber * (int(value)))
                                
                elif  substitutionRequiredForBattalionName == 'E':
                    #substitutionRequiredBattalion = BattalionRanked.E;
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Elephants - availableDefenders.Elephants
                    if (afterSubstitutionDefenderBattalionsRequired.Horses < availableDefenders.Horses):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + numberOfSubstitutionRequired * int(entry.getValue))
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.getNumberOfHorses() - afterSubstitutionDefenderBattalionsRequired.getNumberOfHorses())/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + tempNumber * (int(value)))
                        else:
                            if((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants - tempNumber * (int(value)))
				
                elif substitutionRequiredForBattalionName == "AT" :
                    #substitutionRequiredBattalion = BattalionRanked.AT;
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Armoured - availableDefenders.Armoured
                    if (afterSubstitutionDefenderBattalionsRequired.Horses < availableDefenders.Horses):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + numberOfSubstitutionRequired * int(value))
                                actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoured - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.Horses - afterSubstitutionDefenderBattalionsRequired.Horses)/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoured - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + tempNumber * (int(value)))
                        else:
                            if ((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoured - numberOfSubstitutionRequired); // need for recheck
                             else:
                                 tempNumber = availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses
                                 actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses + tempNumber)
                                 afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.Armoured - tempNumber * (int(value)))
                
                elif substitutionRequiredForBattalionName == "SG" :
                    #BattalionRanked substitutionRequiredBattalion = BattalionRanked.SG;
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.SlingGuns - availableDefenders.SlingGuns
                    if (afterSubstitutionDefenderBattalionsRequired.Horses < availableDefenders.Horses):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + numberOfSubstitutionRequired * (int(value)))
                                actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.Horses - afterSubstitutionDefenderBattalionsRequired.Horses)/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + tempNumber * (int(value)))

                        else:
                            if ((availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Horses-afterSubstitutionDefenderBattalionsRequired.Horses
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.SlingGuns - tempNumber * (int(value)))

            elif substituteBattalionName == "E" :
                substituteBattalion = BattalionRanked('E')
                
                if substitutionRequiredForBattalionName == "H" :
                    #attalionRanked substitutionRequiredBattalion = BattalionRanked.H;
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Horses - availableDefenders.Horses
                    if (afterSubstitutionDefenderBattalionsRequired.Elephants < availableDefenders.Elephants):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + numberOfSubstitutionRequired * int(value))
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.Elephants - afterSubstitutionDefenderBattalionsRequired.Elephants)/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + tempNumber * (int(value)))

                        else:
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.Horses - tempNumber * (int(value)))

                elif substitutionRequiredForBattalionName == "E":
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Elephants - availableDefenders.Elephants
                    if (afterSubstitutionDefenderBattalionsRequired.Elephants < availableDefenders.Elephants):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + numberOfSubstitutionRequired * int(value))
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.Elephants - afterSubstitutionDefenderBattalionsRequired.Elephants)/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + tempNumber * (int(value)))
                        else:
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants - tempNumber * (int(value)))
                                
                elif substitutionRequiredForBattalionName == "AT":
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Armoured - availableDefenders.Armoured
                    if (afterSubstitutionDefenderBattalionsRequired.Elephants < availableDefenders.Elephants):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + numberOfSubstitutionRequired * int(value))
                                actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoured - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.Elephants - afterSubstitutionDefenderBattalionsRequired.Elephants)/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoured - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + tempNumber * (int(value)))
                        else:
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoured - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.Armoured - tempNumber * (int(value)))

                elif substitutionRequiredForBattalionName == "SG" :
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.SlingGuns - availableDefenders.SlingGuns
                    if (afterSubstitutionDefenderBattalionsRequired.Elephants < availableDefenders.Elephants):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + numberOfSubstitutionRequired * int(value))
                                actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns - numberOfSubstitutionRequired)
                            else:
                                tempNumber = int(Math.floor((availableDefenders.Elephants - afterSubstitutionDefenderBattalionsRequired.Elephants)/(int(value))))
                                actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns - tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + tempNumber * (int(value)))
                        else:
                            if ((availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants) >= int(Math.ceil(numberOfSubstitutionRequired / (int(value))))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.Elephants + int(Math.ceil(numberOfSubstitutionRequired / (int(value)))))
                                actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns - numberOfSubstitutionRequired) // need for recheck
                            else:
                                tempNumber = availableDefenders.Elephants-afterSubstitutionDefenderBattalionsRequired.Elephants
                                actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants + tempNumber)
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.SlingGuns - tempNumber * (int(value)))
                                
            elif substituteBattalionName == "AT":
                substituteBattalion = BattalionRanked('AT')

                if substitutionRequiredForBattalionName == "H" :
                    numberOfSubstitutionRequired = actualDefendesBattalionsRequired.Horses - availableDefenders.Horses
                    if (afterSubstitutionDefenderBattalionsRequired.Armoured < availableDefenders.Armoured):
                        if (substituteBattalion.rank < substitutionRequiredBattalion.rank):
                            if ((availableDefenders.Armoured-afterSubstitutionDefenderBattalionsRequired.Armoured) >= numberOfSubstitutionRequired * (int(value))):
                                afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfArmoured() - afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured();
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.getNumberOfHorses() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				case "E" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.E;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfElephants() - availableDefenders.getNumberOfElephants();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() < availableDefenders.getNumberOfArmoured()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfArmoured() - afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured();
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.getNumberOfElephants() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				case "AT" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.AT;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfArmoured() - availableDefenders.getNumberOfArmoured();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() < availableDefenders.getNumberOfArmoured()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfArmoured() - afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured();
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				case "SG" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.SG;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfSlingGuns() - availableDefenders.getNumberOfSlingGuns();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() < availableDefenders.getNumberOfArmoured()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfArmoured() - afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfArmoured()-afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured();
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				}
			}
			break;
			case "SG" : {
				BattalionRanked substituteBattalion = BattalionRanked.SG;


				switch (substitutionRequiredForBattalionName) {
				case "H" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.H;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfHorses() - availableDefenders.getNumberOfHorses();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() < availableDefenders.getNumberOfSlingGuns()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfSlingGuns() - afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.getNumberOfHorses() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns();
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(afterSubstitutionDefenderBattalionsRequired.getNumberOfHorses() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				case "E" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.E;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfElephants() - availableDefenders.getNumberOfElephants();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() < availableDefenders.getNumberOfSlingGuns()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfSlingGuns() - afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.getNumberOfElephants() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns();
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(afterSubstitutionDefenderBattalionsRequired.getNumberOfElephants() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				case "AT" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.AT;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfArmoured() - availableDefenders.getNumberOfArmoured();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() < availableDefenders.getNumberOfSlingGuns()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfSlingGuns() - afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.getNumberOfArmoured() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns();
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(afterSubstitutionDefenderBattalionsRequired.getNumberOfArmoured() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				case "SG" : {
//					BattalionRanked substitutionRequiredBattalion = BattalionRanked.SG;
					int numberOfSubstitutionRequired = actualDefendesBattalionsRequired.getNumberOfSlingGuns() - availableDefenders.getNumberOfSlingGuns();
					if (afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() < availableDefenders.getNumberOfSlingGuns()) {
						if (substituteBattalion.getRank() < substitutionRequiredBattalion.getRank()) {

							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= numberOfSubstitutionRequired * ((int) entry.getValue()))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + numberOfSubstitutionRequired * (int) entry.getValue());
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() - numberOfSubstitutionRequired);
							} else {
								int tempNumber = (int) Math.floor((availableDefenders.getNumberOfSlingGuns() - afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns())/((int) entry.getValue()));
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() - tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + tempNumber * ((int) entry.getValue()));

							}
						} else {
							if(((availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns()) >= (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())))) {
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() + (int) Math.ceil((double)numberOfSubstitutionRequired / ((int) entry.getValue())));
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() - numberOfSubstitutionRequired); // need for recheck
							} else {
								int tempNumber = availableDefenders.getNumberOfSlingGuns()-afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns();
								actualDefendesBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.getNumberOfSlingGuns() + tempNumber);
								afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(afterSubstitutionDefenderBattalionsRequired.getNumberOfSlingGuns() - tempNumber * ((int) entry.getValue()));

							}
						}
					}
				}
				break;
				}
			}
			}
		}

	}
}

SSSSSSSSSSSSSSSSSSS
    def getActualDefendesBattalionsRequired(self, attackers, double defenders_army_strongness_factor):
        acualDefendesBattalionsRequired = Battalions()
        #int temp;
        temp = int(Math.ceil(attackers.getNumberOfHorses() / defenders_army_strongness_factor))
        acualDefendesBattalionsRequired.setNumberOfHorses(temp)

        temp = int(Math.ceil(attackers.getNumberOfElephants() / defenders_army_strongness_factor))
        acualDefendesBattalionsRequired.setNumberOfElephants(temp)
		
	temp = int(Math.ceil(attackers.getNumberOfArmoured() / defenders_army_strongness_factor))
        acualDefendesBattalionsRequired.setNumberOfArmoured(temp)

        temp = int(Math.ceil(attackers.getNumberOfSlingGuns() / defenders_army_strongness_factor))
	acualDefendesBattalionsRequired.setNumberOfSlingGuns(temp);
	return acualDefendesBattalionsRequired
    
    def getAfterSubstitutionDefenderBattalionsRequired (self, availableDefenders, actualDefendesBattalionsRequired):
        afterSubstitutionDefenderBattalionsRequired = Battalions()
        afterSubstitutionDefenderBattalionsRequired.setNumberOfHorses(actualDefendesBattalionsRequired.Horses)
        afterSubstitutionDefenderBattalionsRequired.setNumberOfElephants(actualDefendesBattalionsRequired.Elephants)
        afterSubstitutionDefenderBattalionsRequired.setNumberOfArmoured(actualDefendesBattalionsRequired.Armoureds)
        afterSubstitutionDefenderBattalionsRequired.setNumberOfSlingGuns(actualDefendesBattalionsRequired.SlingGuns)
        if (availableDefenders.Hor9ses < actualDefendesBattalionsRequired.Horses):
            #BattalionRanked temp = BattalionRanked.H;
            temp = BattalionRanked('H')
            self.setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.rank)
        if (availableDefenders.Elephants < actualDefendesBattalionsRequired.Elephants):
            #BattalionRanked temp = BattalionRanked.E
            temp = BattalionRanked('E')
            self.setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.rank)
        if (availableDefenders.Armoured < actualDefendesBattalionsRequired.Armoured):
            #BattalionRanked temp = BattalionRanked.AT;
            temp = BattalionRanked('AT')
	    setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.rank)
        if (availableDefenders.SlingGuns < actualDefendesBattalionsRequired.SlingGuns):
            #BattalionRanked temp = BattalionRanked.SG;
            temp = BattalionRanked('SG')
            setAfterSubstitutionDefenderBattalionsRequired(afterSubstitutionDefenderBattalionsRequired, availableDefenders, actualDefendesBattalionsRequired, temp.rank)
        return afterSubstitutionDefenderBattalionsRequired
    	
    def isSubstitutionBattalionsRequired (self, availableDefenders, actualDefendesBattalionsRequired):
        if ((availableDefenders.Horses >= actualDefendesBattalionsRequired.Horses) and (availableDefenders.Elephants >= actualDefendesBattalionsRequired.Elephants) and (availableDefenders.Armoured >= actualDefendesBattalionsRequired.Armoured) and  (availableDefenders.SlingGuns >= actualDefendesBattalionsRequired.SlingGuns)):
            return false
        return true

    def calculateDefendersBattalionsRequired(self, attackers, availableDefenders, defenders_army_strongness_factor):
        actualDefendesBattalionsRequired = self.getActualDefendesBattalionsRequired(attackers, defenders_army_strongness_factor)
        if self.isSubstitutionBattalionsRequired(availableDefenders, actualDefendesBattalionsRequired):
            return self.getAfterSubstitutionDefenderBattalionsRequired(availableDefenders, actualDefendesBattalionsRequired)
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
