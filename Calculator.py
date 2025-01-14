import math 

#Fonctions operations de bases
def addition(a,b):
    return a+b
def soustraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a / b 
    else: 
        raise ValueError("Division par zéro !")
#Fonctions operations avancées
def puissance(a,b): 
    return math.pow(a,b) 

def racine_carré(a):
    if a >= 0: 
        return math.sqrt(a) 
    else:
         raise ValueError("Racine carrée d'un nombre négatif !") 
    
def logarithm(a): 
    if a > 0: 
        return math.log(a) 
    else:
        raise ValueError("Logarithme d'un nombre non positif !")    

class Calculatrice :
    def __init__(self):
        self.operations={
            '+': addition,
            '-': soustraction,
            '*':multiplication,
            '/': division,
            '^':puissance,
            '√':racine_carré,
            'log':logarithm
        }

    def add_operation(self,symbole,fonction) :
        if symbole in self.operations:
            print("Cette operation est deja stockée")
        else :
            self.operations['symbole']=fonction

    def calculate(self,num1,symbole,num2):       
        signe=self.operations[symbole]               
        if signe in self.operations.values():
           if not isinstance(num1,(int,float)) or not isinstance(num2,(int,float)):
              raise ValueError ("Saisie incorrecte vous devez saisir des nombres ")           
           else:   
                if signe==logarithm or signe==racine_carré:          
                    return signe(num1)     
                else : 
                    return signe(num1,num2)                
        else : 
            print("Cette operation n'est pas disponible pour le moment")


        
    
''' symbole=Calculatrice()
symbole.add_operation('^',puissance)
symbole.add_operation('√', racine_carré)
symbole.add_operation('log', logarithm) '''

#Programme

Calculator=Calculatrice()
run=True 
while run==True:
    nb1=float(input("Veuillez entrer le premier nombre : "))
    op=input("Veuillez selectionner un operateur  parmi les suivants : (+,-,*,/,√,log,^) ")
    if op =='√' or op =='log':
        res=Calculator.calculate(nb1,op,nb1)
        print(res)
    else :   
        nb2=float(input("Veuillez entre le second nombre : "))    
        res=Calculator.calculate(nb1,op,nb2)
        print(res)
    print('voulez vous continuer vos operations')
    rep=input('Repondre par Y ou N ')
    if rep=='N' :
        run=False