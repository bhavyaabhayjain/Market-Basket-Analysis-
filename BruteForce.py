import time as tm
import numpy as np
import pandas as pd
import csv
from mlxtend.preprocessing import TransactionEncoder
s_t = tm.time()
def isInList(aList, item):
    if item in aList:
        return 1
    else:
        return -1
def removeEmptyValues(aList, symbolToRemove):
    while (True):
        val = isInList(aList, symbolToRemove)
        if (val == 1):
            aList.remove(symbolToRemove)
        else:
            break
def generateListOfListsFromCSV(fullFileName):
    with open(fullFileName, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
    listOfLists = []
    for i in range(len(data)):
        removeEmptyValues(data[i], '')
        listOfLists.append(data[i])
    return listOfLists
def oneHotEncodedDataFrame(data):
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    dataFrame = pd.DataFrame(te_ary, columns=te.columns_)
    return dataFrame
def generateItemsBaskets(dataFrame):
    items = []
    for col in dataFrame.columns:
        items.append(col)
    baskets = []
    transaction_id = 1
    for i in range(len(dataFrame)):
        itemset = []
        for j in range(len(items)):
            if (dataFrame.iloc[i][j] == True):
                itemset.append(items[j])
        baskets.append({transaction_id: itemset})
        transaction_id += 1
    return items, baskets
dataset = generateListOfListsFromCSV('D:\Data Mining Projects\Book4.csv')
def bruteForceFrequentItemsets(dataFrame, min_support=1, max_len=None):
    items, baskets = generateItemsBaskets(dataFrame)
    freq_itemsets = []
    for i in range(len(items)):

        for j in range(len(items)):

            if (j != i and j > i):
                basket_count = 0
                basket_item = 1
                for b in baskets:
                    val1 = isInList(b.get(basket_item), items[i])
                    val2 = isInList(b.get(basket_item), items[j])
                    if (val1 != -1 and val2 != -1):
                        basket_count += 1
                    basket_item += 1

                if (basket_count >= min_support):
                    freq_itemsets.append([items[i], items[j]])

    return freq_itemsets
dataset_onehotencoded = oneHotEncodedDataFrame(dataset)
frequent_itemsets = bruteForceFrequentItemsets(dataset_onehotencoded, min_support=2)
frequent_itemsets2 = bruteForceFrequentItemsets(dataset_onehotencoded, min_support=3)
frequent_itemsets3 = bruteForceFrequentItemsets(dataset_onehotencoded, min_support=4)
frequent_itemsets4 = bruteForceFrequentItemsets(dataset_onehotencoded, min_support=5)
frequent_itemsets5 = bruteForceFrequentItemsets(dataset_onehotencoded, min_support=6)
print("Frequent 2-itemsets:")
for i in range(len(frequent_itemsets2)):
    print(frequent_itemsets[i])
print("\n____________________")
print("Frequent 3-itemsets:")
for i in range(len(frequent_itemsets3)):
    print(frequent_itemsets2[i])
print("\n____________________")
print("Frequent 4-itemsets:")
for i in range(len(frequent_itemsets4)):
    print(frequent_itemsets3[i])
print("\n____________________")
print("Frequent 5-itemsets:")
for i in range(len(frequent_itemsets5)):
    print(frequent_itemsets4[i])

print("The time to get brute force methods itemsets are","--- %s seconds ---" % (tm.time() - s_t))
