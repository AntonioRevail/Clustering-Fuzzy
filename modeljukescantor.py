# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:57:58 2019

@author: João Lagôas
@author: Antonio Revail
"""
""" Imports """
import random
import math

 
""" Support Functions """
def listToString(lst):
    strg = ''.join(lst)
    return strg

def split(word): 
    return [char for char in word] 

def replace(listOfBases):
    i = random.randint(-1,len(listOfBases)-1)
    possibilities = ['A', 'T', 'C', 'G', 'N', '-']
    listOfBases[i] = random.choice(possibilities)
    return listOfBases
    
def readBaseSequence(filePath):
    with open(filePath) as f:
        lines = f.read()
        
    return split(lines)

def writeBaseSequence(filePath, newListOfBases):
    f = open(filePath, "a")
    f.write(listToString(newListOfBases) + '\n\n')
    f.close()

""" Main Code """
    

listOfBases = readBaseSequence('input.fasta')
pos = 0
for i in range(0, len(listOfBases)):
    if(listOfBases[i] == '\n'):
        pos = i
        break
listOfBases = listOfBases[i+1:-1]
print(listOfBases)
print("Numero de bases: " + str(len(listOfBases)))

""" Rounding up. In practice, bases are often larger than 100. """

percentualToChange = 0.02 #0.01 = 1%
percentualToChange = random.uniform(0.000001, percentualToChange)
print("Percentual de bases a serem trocadas (%): " + str(percentualToChange*100.0))

countToChange = math.ceil((len(listOfBases)*percentualToChange))
print("Quantidade de bases a serem trocadas: " + str(countToChange))


""" print("Old sequence: " + str(listOfBases)) """

""" Call the replace function countToChange times """

for i in range(0, countToChange):
    listofBases = replace(listOfBases)
    
""" print("New sequence: " + str(listOfBases)) """
writeBaseSequence('resultadobase21.fas', listOfBases)


#print(listOfBases)


