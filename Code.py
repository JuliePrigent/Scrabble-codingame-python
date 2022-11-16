#https://www.codingame.com/training/medium/scrabble


import sys
import math

#Create a dict with the value of each letter
tab={1:['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u'] ,
2 : ['d', 'g'], 
3 : ['b', 'c', 'm', 'p'], 
4 : ['f', 'h', 'v', 'w', 'y'],
5: ['k'],
8: ['j','x'],
10: ['q','z']
}

values=[] #list of word values 
n = int(input()) #Number of found words
prop=[] #list of word
prop_valide=[] #list of valid word
max=0

#COLLECTING THE WORDS

for i in range(n): 
    w = input() 
    
    #Words with more than 7 letters are not stored
    if(len(w)>7):
        continue
    else:
        #words with the appropriate number of letter are stored 
        prop.append(w) 

#COLLECTING THE AUTHORIZED LETTERS 
letters = input() 

#for each word, collecting the lenght, and creating a copy of the allowed letter

for elem_prop in prop: 
    longueur_mot=len(elem_prop)
    increment = 0
    letters_copy=list(letters)
    
    #for each letters of a word, testing if the letter is part of the authorized one, cancelling it if it is to prevent authorizing twice a same letter
    for lettres in elem_prop: 
    
        if(lettres in letters_copy):
            increment +=1
            letters_copy.remove(lettres) 
            
            #once all letters are approved for a word, we can add it to the valid word list
            if(longueur_mot == increment): 
                prop_valide.append(elem_prop)

        else:
            break

#CALCULATING THE VALUE OF EACH VALID WORD by adding the value of each letter to a variable
for elem_prop_valide in prop_valide: 
    som=0
    decomp_prop_valide = list(elem_prop_valide)

    for elem_decomp_valide in decomp_prop_valide:
        if(elem_decomp_valide in tab[1]):
            som+=1
        elif(elem_decomp_valide in tab[2]):
            som+=2
        elif(elem_decomp_valide in tab[3]):
            som+=3
        elif(elem_decomp_valide in tab[4]):
            som+=4
        elif(elem_decomp_valide in tab[5]):
            som+=5
        elif(elem_decomp_valide in tab[8]):
            som+=8
        elif(elem_decomp_valide in tab[10]):
            som+=10

    #STORING EACH VALUES IN THE VALUE LIST
    values.append(som)

x=0
longueur= len(values)

#TESTING EACH VALUES TO CHOOSE THE MAXIMUM

for elem_values in values: 
    dernier_elem = x+1
    if(longueur==1): #si l'on a qu'un mot de valide
        print(prop_valide[0])

    else:
        if(values[x]>=max):
            max = values[x]
            
        #PRINTING THE WORD WITH THE MAXIMUM VALUE ONCE WE COMPARED EACH ONE
        if(longueur == dernier_elem):
            index_max= values.index(max)
            mot_max=prop_valide[index_max]
            print(mot_max)
    x+=1
