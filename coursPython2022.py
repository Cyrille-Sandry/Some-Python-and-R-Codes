#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 09:39:35 2022

@author: cyrillesimeu
"""


###########################################################

     ##############   Exercice 17    ###############

##########################################################


service=bool(int(input("Voulez-vous une boisson 1=OUI, 0=NON ? ")))
stockCoca=3
stockFanta=5
stockSprite=2
stockRedbull=3

while service:
      votreChoix= int(input("Entrez votre choix 1=Coca,2=Fanta,3=Sprite,4=Redbull "))
      while votreChoix not in [1,2,3,4]:
            votreChoix= int(input("Entrez votre choix 1=Coca,2=Fanta,3=Sprite,4=Redbull "))
      if votreChoix==1:
         if stockCoca!=0:
            print("Prenez votre Coca")
            stockCoca-=1
         else:
            print("Coca n'est pas disponible pour l'instant!")
      elif votreChoix==2:
           if stockFanta!=0:
              print("Prenez votre Fanta")
              stockFanta-=1
           else: 
              print("Fanta n'est pas disponible pour l'instant!")
      elif votreChoix==3:
           if stockSprite!=0:
              print("Prenez votre Sprite")
              stockSprite-=1
           else: 
              print(" Sprite n'est pas disponible pour l'instant!")
            
      elif votreChoix==4 :
           if stockRedbull!=0:
              print("Prenez votre Redbull")
              stockRedbull-=1
           else:
              print("Redbull n'est pas disponible pour l'instant!")  
      service = bool(int(input("Voulez-vous une autre boisson ? 1=oui/0=Non "))) 
      
print("Merci! À bientôt")





###########################################################

     ##############   Exercice 18    ###############

##########################################################





print("#################################\n    ####   Calculatrice   ####\n##################################\n")

op=bool(int(input("Voulez-vous effectuer une opération 1=OUI/ 0=Non? ")))
operation=input("Quelle opération désirez-vous effectuer? +,-,/,//,% ? ")
while op==True:
      nbr1=int(input("Entrez le premier nombre "))
      nbr2=int(input("Entrez le second nombre "))
      if operation in ["/","//","%"]:
         if nbr2==0:
            print("Erreur: division par zéro !")
         elif operation=="/":
              print(nbr1, operation, nbr2, "=", nbr1/nbr2)
         elif operation=="//":
              print(nbr1, operation, nbr2, "=", nbr1//nbr2)
         elif operation=="%":
               print(nbr1, operation, nbr2, "=", nbr1%nbr2)
      else:
          if operation=="+":
             print(nbr1, operation, nbr2, "=", nbr1+ nbr2)
          elif operation=="-":
             print(nbr1, operation, nbr2, "=", nbr1-nbr2)
      op= bool(int(input("Voulez-vous effectuer une autre opération? 1=0UI,0=Non")))
      if op==True:
         operation=input("Quel opération désirez-vous effectuer? +,-,/,//,% ? ")
 
             



###########################################################

     ##############   Exercice 19    ###############

##########################################################

print("#################################\n    ####   Puissance de 10   ####\n##################################\n")

nbr=int(input("Entrez le nombre à élever à la puissance 10 "))
i=1
resul=1
while i<=10:
    resul=resul*nbr
    i+=1
print(nbr," puissance 10","=",resul)    
    
    


###########################################################

     ##############   Exercice 20   ###############

##########################################################

print("#################################\n    ####   Puissance    ####\n##################################\n")

nbr=int(input("Entrez un nombre "))
exp=int(input("Entrez un exposant "))

if nbr==0 and exp==0:
   print("Erreur: opération impossible ")
elif nbr!=0 and exp==0:
     print(nbr," exposant" ,exp,"=",1) 
else:     

    i=1
    resul=1
    while i<=exp:
         resul=resul*nbr
         i+=1
    print(nbr," exposant" ,exp,"=",resul)    
    
    


###########################################################

     ##############   PROJET JUSTE PRIX   ###############

##########################################################




import pandas as pd
import numpy as np
import random
import os


nouveauJeu=bool(int(input("Voulez-vous essayer ce jeu 1=Oui/ 0=Non ? ")))

while nouveauJeu:
      print(""" 
            Voici les niveaux du jeu:
            facile: entre 1 et 10
            moyen: entre 1 et 100
            difficile entre 1 et 1000
           """ )             
      niveau=input("Entrez votre niveau de jeu ")
      
      while niveau not in ["facile", "moyen","difficile "]:
           print(""" 
            Voici les niveaux de jeu disponibles:
            facile: entre 1 et 10
            moyen: entre 1 et 100
            difficile entre 1 et 1000
           """ )  
           print("Entrez votre niveau parmi ces niveaux svp!")
           niveau=input("Entrez votre niveau de jeu ")
      nbrEssaies=10
      if niveau=="facile": 
         juste_prix=random.randrange(0,11,1)
         nbrChoix=11
         while nbrChoix!=juste_prix and nbrEssaies> 0 :
               nbrChoix=int(input("Entrez votre nombre "))
               if nbrChoix >juste_prix:
                  nbrEssaies-=1
                  print("C'est moins, il vous reste ", nbrEssaies, "essaies" if nbrEssaies>0 else "")
               elif nbrChoix < juste_prix:
                   nbrEssaies-=1
                   print( "C'est plus, il vous reste ", nbrEssaies, "essaies" if nbrEssaies>0 else "" )
         if  nbrChoix!=juste_prix:
             print("Vous avez perdu, le juste_prix est ", juste_prix) 
         else:
              print("C'est gagné, vous l'avez fait en ", 10-nbrEssaies+1,"essaies")
      elif niveau=="moyen": 
           juste_prix=random.randrange(0,101,1)
           nbrChoix=101
           while nbrEssaies !=juste_prix and nbrEssaies>0 :
                 nbrChoix=int(input("Entrez votre choix "))
                 if nbrChoix >juste_prix:
                    nbrEssaies-=1
                    print("C'est moins, il vous reste ", nbrEssaies,"essais" if nbrEssaies>0 else "")
                 elif nbrChoix < juste_prix:
                   nbrEssaies-=1
                   print("C'est plus, il vous reste ", nbrEssaies, "essaies" if nbrEssaies>0 else "")
           if nbrChoix != juste_prix:
              print("Vous avez perdu le juste prix est ", juste_prix) 
           else:
                print("C'est gagné, vous l'avez fait en ", 10-nbrEssaies+1,"essaies")
      elif niveau=="difficile": 
           juste_prix=random.randrange(0,1001,1)
           nbrChoix=1001
           while nbrEssaies !=juste_prix and nbrEssaies>0 :
                 nbrChoix=int(input("Entrez votre nombre "))
                 if nbrChoix >juste_prix:
                    nbrEssaies-=1
                    print("C'est moins, il vous reste ", nbrEssaies, "essaies" if nbrEssaies>0 else "")
                 elif nbrChoix < juste_prix:
                      nbrEssaies-=1
                      print("C'est plus, il vous reste ", nbrEssaies, "essaies" if nbrEssaies>0 else "")
           if nbrChoix != juste_prix:
              print("Vous avez perdu le juste prix est", juste_prix) 
           else:
                print("C'est gagné, vous l'avez fait en ", 10-nbrEssaies+1,"essaies")
      
      nouveauJeu=bool(int(input("Voulez-vous jour à nouveau 1=Oui/ 0=Non ? ")))






























      