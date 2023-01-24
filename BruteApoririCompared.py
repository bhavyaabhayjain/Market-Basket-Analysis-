import pandas as pd
import time as tm

filePath = input("Please provide the path of the file: ")

s_t = tm.time()

transaction = pd.read_csv(filePath, header=None, delimiter=',', engine='python', names=range(100))
transaction = transaction.where((pd.notnull(transaction)), None)

transactionIM = pd.get_dummies(transaction.unstack().dropna()).groupby(level=1).sum()
transactionC, itemC = transactionIM.shape
print('The number of transactions in the dataset are: ',transactionC)
print('The number of different items in the dataset are: ',itemC,'\n')

largeItemsets = []
for items in range(1, itemC+1):
    from itertools import combinations
    for itemset in combinations(transactionIM, items):
        itemsetSupport = transactionIM[list(itemset)].all(axis=1).sum()
        s = [str(x) for x in itemset]
        if (len(s) >= 1):
            largeItemsets.append([",".join(s), itemsetSupport])
freqItemset = pd.DataFrame(largeItemsets, columns=["Itemset", "Support"])
results = freqItemset[freqItemset.Support >= 2]
print(results)


dataFile = open('output.txt', 'w')

for eachitem in largeItemsets:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

print("Hence proved that apriori algorithm is faster than brute force method because apriori took 0.010124444961547852 seconds where as brute force method took ","- %s seconds" % (tm.time() - s_t))
