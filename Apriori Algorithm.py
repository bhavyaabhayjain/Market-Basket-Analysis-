
import time as tm
import pandas as pd

filePath = input("Please specify the file's location: ")
minSupport = input('Add the bare minimum of support: ')
minConfidence = input('Add the bare maximum of support: ')
pd.set_option('display.max_columns', None)

s_t = tm.time()

minSupport = int(minSupport)
minConfidence = int(minConfidence)
print("\n")

file = open(filePath, 'r')

with open(filePath, 'r') as fp:
    lines = fp.readlines()

dataset = []

for line in lines:
    line = line.rstrip()
    dataset.append(line.split(","))


def firstpass(dataset):
    items = {}
    itemlist = []
    for data in dataset:
        for item in data:
            if item not in items:
                items[item] = 1
            else:
                items[item] = items[item] + 1
    for key in items:
        temp = []
        temp.append(key)
        itemlist.append(temp)
        itemlist.append(items[key])
        temp = []
    return itemlist


DeletedItems = []
MainFrequent = []


def FrequentItems(CandidateList, TotalTransactions, minSupport, dataset, MainFrequent):
    frequentItems = []
    for i in range(len(CandidateList)):
        if i % 2 != 0:
            if ((CandidateList[i] * 1.0 / TotalTransactions) * 100) >= minSupport:
                frequentItems.append(CandidateList[i - 1])
                frequentItems.append(CandidateList[i])
            else:
                DeletedItems.append(CandidateList[i - 1])
            print("\n" + str(CandidateList) + "\n")

    for k in frequentItems:
        MainFrequent.append(k)

    if len(frequentItems) == 2 or len(frequentItems) == 0:
        returnArray = MainFrequent
        return returnArray
    else:
        NewCandidateSets(dataset, DeletedItems, frequentItems, TotalTransactions, minSupport)


def NewCandidateSets(dataset, DeletedItems, frequentItems, TotalTransactions, minSupport):
    Elements = []
    CombinedSets = []
    candidateSet = []
    for i in range(len(frequentItems)):
        if i % 2 == 0:
            Elements.append(frequentItems[i])
    for item in Elements:
        tempCombo = []
        k = Elements.index(item)
        for i in range(k + 1, len(Elements)):
            for j in item:
                if j not in tempCombo:
                    tempCombo.append(j)
            for m in Elements[i]:
                if m not in tempCombo:
                    tempCombo.append(m)
            CombinedSets.append(tempCombo)
            tempCombo = []
    sortedCombo = []
    uniqueCombo = []
    for i in CombinedSets:
        sortedCombo.append(sorted(i))
    for i in sortedCombo:
        if i not in uniqueCombo:
            uniqueCombo.append(i)
    CombinedSets = uniqueCombo
    for item in CombinedSets:
        count = 0
        for transaction in dataset:
            if set(item).issubset(set(transaction)):
                count = count + 1
        if count != 0:
            candidateSet.append(item)
            candidateSet.append(count)
    FrequentItems(candidateSet, TotalTransactions, minSupport, dataset, MainFrequent)


def AssociationRules(freqSet):
    associationRule = []
    import itertools
    for item in freqSet:
        if isinstance(item, list):
            if len(item) != 0:
                length = len(item) - 1
                while length > 0:
                    combinations = list(itertools.combinations(item, length))
                    temp = []
                    LHS = []
                    for RHS in combinations:
                        LHS = set(item) - set(RHS)
                        temp.append(list(LHS))
                        temp.append(list(RHS))
                        associationRule.append(temp)
                        temp = []
                    length = length - 1
    return associationRule


TotalTransactions = len(dataset)
print("The number of transactions in this file as a whole is {}\n".format(TotalTransactions))


def AprioriAlgorithm(rules, dataset, minSupport, minConfidence):
    returnAprioriAlgorithm = []
    for rule in rules:
        supportOfX = 0
        supportOfXinPercent = 0
        supportOfXandY = 0
        supportOfXandYinPercent = 0
        for transaction in dataset:
            if set(rule[0]).issubset(set(transaction)):
                supportOfX = supportOfX + 1
            if set(rule[0] + rule[1]).issubset(set(transaction)):
                supportOfXandY = supportOfXandY + 1
        supportOfXinPercent = (supportOfX * 1.0 / TotalTransactions) * 100
        supportOfXandYinPercent = (supportOfXandY * 1.0 / TotalTransactions) * 100
        confidence = (supportOfXandYinPercent / supportOfXinPercent) * 100
        if confidence >= minConfidence:
            supportOfXAppendString = "Support Of X is: " + str(round(supportOfXinPercent, 2))
            supportOfXandYAppendString = "\nSupport of X & Y is: " + str(round(supportOfXandYinPercent))
            confidenceAppendString = "\nConfidence is: " + str(round(confidence))

            returnAprioriAlgorithm.append(supportOfXAppendString)
            returnAprioriAlgorithm.append(supportOfXandYAppendString)
            returnAprioriAlgorithm.append(confidenceAppendString)
            returnAprioriAlgorithm.append(rule)

    return returnAprioriAlgorithm


firstCandidateSet = firstpass(dataset)
frequentItemSet = FrequentItems(firstCandidateSet, TotalTransactions, minSupport, dataset, MainFrequent)
associationRules = AssociationRules(MainFrequent)
AprioriAlgorithm = AprioriAlgorithm(associationRules, dataset, minSupport, minConfidence)

counter = 1
if len(AprioriAlgorithm) == 0:
    print("Any association's support and confidence norms couldn't be applied in this")
else:
    for i in AprioriAlgorithm:
        if counter == 4:
            print("\n" + str(i[0]) + "------->" + str(i[1]) + "\n")
            counter = 0
        else:
            print(i, end='  ')
        counter = counter + 1

print("--- %s seconds ---" % (tm.time() - s_t))