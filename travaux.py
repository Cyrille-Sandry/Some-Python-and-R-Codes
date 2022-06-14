###########################################################

    ##########  Comparaison de nombre ##########

###########################################################


"""
Ce code demande à un utilisateur d'entrer deux  nombres et les comparent

"""

a=int(input("Entrez le premier nombre: "))
b=int(input("Entrez le second nombre: "))


if a-b>0:
   print("C'est plus")
elif a-b<0:
     print("C'est moins")
else:
    print("C'est gagné")
    
    
    
    
    
    
###########################################################

    ########## Distributeur automatique  ###########

###########################################################
    
"""
 Ce code simule un distributeur automatique de boisons
"""
    


service=bool(int(input("Voulez-vous une boisson 1=OUI, 0=NON ? ")))

while (service!=0) and (service!=1):
       service=bool(input("Entrez 1=Oui ou 0=Non"))
       
       
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






################################################################

  ################ Exercices supplémentaires ##############
  
###############################################################


######################## Connexion ########################

"""
Ce code simule la création d'un mot de passe et 
les tantatives de connexion à un compte. Après trois tentative manquées
un message de compte bloqué est affiché à l'utilisateur.

"""

motDePasse=input("Entrez un mot de passe ")
confirm=input("Confirmez votre mot de passe ")

while motDePasse!= confirm:
      print("Les mots de passe que vous avez entrés ne sont pas identiques")
      motDePasse=input("Entrez de nouveau un mot de passe ")
      confirm=input("Confirmez ce mot de passe (doit être identique au précédent) ")
      
print("""
      ##############################################
            Connectez vous maintenant
      ##############################################
    """)

motDePasseConnexion=input("Entrez votre mot de passe pour vous connecter ")
nbrEssaies=3
while motDePasseConnexion != motDePasse and nbrEssaies>1 :
      nbrEssaies-=1
      print("Il vous reste", nbrEssaies, "tentative" if nbrEssaies >= 1 else "")
      motDePasseConnexion=input("Entrez un mot de passe valide svp " )
      
if motDePasseConnexion!=motDePasse :
   print("Votre compte est bloqué, vous ne saurez reéssayer une quatrième fois!")
   print("Au revoir!")
else:
    print("Salut ! ")


###########################################################

         ############## Nombre lignes ##############

###########################################################

nbrLignes=int(input("Entrez le nombre de ligne que vous désirez afficher "))

while nbrLignes<1:
      print("Entrez un nombre entier strictement positif")
      nbrLignes=int(input("Entrez un nombre positif "))

affichage=1
while affichage<= nbrLignes :
      print("#"*affichage)
      affichage+=1
      
#################################################################
 
         ################ Borne inférieure ################
         
#################################################################

"""
ce code demande à l'utilisateur d'entrer 10 nombre de façons successive
et affiche le minimum de ces nombre à la fin.
"""

tab=[]
i=1

while i <=10: 
      nbr=float(input("Entrez un nombre "))
      tab.append(nbr)
      i+=1
print("Le plus petit parmi ces nombre est ", min(tab))


####################################################################


   
           ########### PROJET JUSTE PRIX ###############



#####################################################################




import pandas as pd
import numpy as np
import random
import os




print("#################################\n #### Choix aléatoire ####\n##################################\n")



nouveauJeu=int(input("Voulez-vous essayer ce jeu du choix aléatoire ? tapez 1=Oui/ 0=Non "))


while nouveauJeu !=0 and nouveauJeu !=1:
      print("""
             SVP tapez 1 pour Oui ou tapez 0 pour Non
           """)
      nouveauJeu=int(input("Voulez-vous Essayer ce jeu de choix aléatoire? 1=Oui/ 0=Non "))



while nouveauJeu== 1:
    
      print("""
            Voici les niveaux du jeu:
            facile: entre 1 et 10
            moyen: entre 1 et 100
            difficile entre 1 et 1000
            """ )
            
      niveau=input("Entrez le niveau de jeu désiré ")

      while niveau not in ["facile", "moyen","difficile"]:
          
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
                    
         if nbrChoix!=juste_prix:
             
            print("Vous avez perdu, le juste_prix est ", juste_prix)
            
         else:
             
             print("C'est gagné, vous l'avez fait en ", 10-nbrEssaies+1,"essaies")
             
      elif niveau=="moyen":
          
           juste_prix=random.randrange(0,101,1)
           
           nbrChoix=101
           
           while (nbrChoix != juste_prix) and nbrEssaies >0 :
               
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
           
           while nbrChoix !=juste_prix and nbrEssaies>0 :
               
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
              

      nouveauJeu=int(input("Voulez-vous jouer à nouveau 1=Oui/ 0=Non ? "))





###########################################################



############## Exercice 21 ###############



##########################################################



print("""
##################################

#### Remplir un tableau ####

##################################
""")





tab=[]

compteur=0
while compteur<6 :
      tab.append(float(input("Entrez un nombre ")))
      compteur+=1


print("Voici le tableau:", tab)




###########################################################



############## Exercice 22 ###############



##########################################################


print("#"*30)

print("Voici la table")
tab=[]
compteur=0
exp=1
while compteur <10 :
      tab.append(exp*2)
      exp=tab[compteur]
      compteur+=1
print(tab)

print("#"*30)
print("Voici les cellules de la table")
compteur2=0
while compteur2<10:
      print(tab[compteur2])
      compteur2+=1





















