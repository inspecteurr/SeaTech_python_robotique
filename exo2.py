from exo1 import Robot

class Human():  
    #__slots__ = ('__breath','__sexe','__food')

    def __init__(self,sexe):
        self.__sexe = sexe
        self.__food = []
        self.__breath = True
        n=1
        k=1
        while(n is not "0"):
            self.__food.append(input("\nMerci ! Qu'est ce que je peux manger ? \n"))
            k+=1
            n = input("\nAutre chose ? \nOui --> 1\nNon --> 0\n")

    def breathe_On(self):
        self.__breath = True
        print("\nJe revie !!!!\n")

    def breathe_Off(self):
        self.__breath = False

    def eat(self,args):
        lenght = len(args)
        k=0
        if (type(args) == str): 
            if args in self.__food :
                print("\nJe mange : ",args,"\n")
            else :
                print("\nJe ne peux pas manger cet aliment\n")
        else :
            for i in args :
                i = args[k]
                k+=1
                if i in self.__food :
                    print("\nJe mange : ",i,"\n")
                else :
                    print("\nJe ne peux pas manger cet aliment\n")
            

    @property
    def sexe(self):
        return self.__sexe

    @sexe.setter
    def sexe(self,sexe):
        self.__sexe = sexe

    @property
    def breath(self):
        return self.__breath

    @breath.setter
    def breath(self,breath):
        self.__breath = breath


class Cyborg(Robot, Human):  

    #__slots__=() 

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def infrared_vision(self):
        print("Je vois dans la nuit .....\nComme Batman !!")

    def death(self):
        if ((self.breath == False) or (self.power == False)):
            self.power=False
            self.breath=False
            print("\nJe suis mort mon oeuf ...\n")
        else :
            print("\nC'est bon je suis en vie !\n")




cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, ' sexe ', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.death()
cyborg.start()
cyborg.breathe_On()
cyborg.death()

# cyborg.truc_fun()