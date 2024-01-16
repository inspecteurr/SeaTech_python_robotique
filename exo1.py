import time
import keyboard

def StartedAction(f):
    def wrapper(*args):
        obj:Robot = args[0]
        if obj.power:
            return f(*args)
        else:
            print("\nIl faut m'allumer avant gros malin")
    return wrapper



class Robot():
    
    #__slots__ = ('__name','__power', '__current_speed', '__speed_max','__battery_level','__speed_min')
    
    def __init__(self,name):
        self.__name = name
        #input('\nJe viens de naitre, donne moi un nom maître :-O \n')
        self.__power = False
        self.__current_speed = 0
        self.__speed_max = 100
        self.__speed_min = -20
        self.__battery_level = 100
        self.summary()
	
    def start(self):
        self.__power = True
        self.__battery_level = self.__battery_level - 5

        if (0<= self.__battery_level <10) :
            if (self.__battery_level ==0) :
                print("La batterie est vide mon reuf !!")
                self.off()
            print("\nFais gaffe ! La batterie est à : ", self.__battery_level, "%")

        print("Je suis allumé mon reuf, ma batterie est à : ",self.__battery_level)
        
                    
    def off(self):
        self.deceleration(0)
        self.__current_speed = 0
        self.__power = False

    def charge(self):
        while (self.__battery_level <100) :
                print("La batterie est à : ", self.__battery_level, "%\r")
                self.__battery_level = self.__battery_level + 1
                time.sleep(0.1)
        if (self.__battery_level == 100):
            print("La batterie est full mon reuf")

    @StartedAction
    def acceleration(self,vitesse):
        print("\nOk je cours ! Attend moi")
        if (vitesse>0):
            while (self.__current_speed <vitesse) :
                if (self.__current_speed<=self.__speed_max):
                    self.__current_speed = self.__current_speed + 1
                    self.__battery_level = self.__battery_level - 1
                    time.sleep(0.2)
        else : 
            while (self.__current_speed >vitesse) :
                if (self.__current_speed>=self.__speed_min):
                    self.__current_speed = self.__current_speed - 1
                    self.__battery_level = self.__battery_level - 1
                    time.sleep(0.2)
        print("\nLa vitesse a été atteinte, elle est de : ", self.__current_speed, "\nMa batterie est descendu à : ",self.__battery_level)


    @StartedAction
    def deceleration(self,vitesse):
        print("\nTéma comment je tire le frein à main mon copaing !")
        while (self.__current_speed >vitesse and self.__current_speed>0) :
            self.__current_speed = self.__current_speed - 1
            time.sleep(0.2)
        print("\nLa vitesse a été atteinte, elle est de : ", self.__current_speed)

    @StartedAction
    def stop(self):
        while (self.__current_speed != 0) :
                if (vitesse>0):
                    self.__current_speed = self.__current_speed - 1
                    time.sleep(0.2)
                else :
                    self.__current_speed = self.__current_speed + 1
                    time.sleep(0.2)
        print("\nC'est bon, je me suis arrété, ma vitesse est de : ", self.__current_speed)


    def summary(self):
        print("\nMon nom est : ", self.__name, "\nMa batterie est à ", self.__battery_level,"%","\nMa vitesse est de : ",self.__current_speed,"\nMa vitesse max est de : ",self.__speed_max)
        if (self.__power == True):
            print("\nJe suis allumé")
        else :
            print("\nJe suis éteint")


    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self,power):
        self.__power = power

    @property
    def speed(self):
        return self.__current_speed

    @speed.setter
    def speed(self,speed):
        self.__current_speed = speed

    @property
    def speed_max(self):
        return self.__speed_max

    @speed.setter
    def speed_max(self,speed_max):
        self.__speed_max = speed_max

    @property
    def name(self):
        return self.__name

    @power.setter
    def name(self,name):
        self.__name = name


if __name__ == '__main__' :
    r1 = Robot("Grégoire")

    print("\nVoila ma notice : \nAllumer --> start\nAccelerer --> acceleration\nDécélérer --> décélération\summary --> summary\nStop --> stop\nCharge --> charge\nOff --> off\n")
        
    
    while (True) :


        # print("\nVoila ma notice : \nAllumer --> a\nAccelerer --> z\nDécélérer --> e\summary --> r\nStop --> s\nCharge --> c\nEteindre --> q\n")
        # action = input('\nJe suis a ton service, dis moi quoi faire : \n')

        # if keyboard.read_key() == "a":
        #     r1.start()
        
        # if keyboard.read_key() == "z":
        #     vitesse = input('\nJe veux avancer, donne moi une vitesse : ')
        #     vitesse = int(vitesse)
        #     r1.acceleration(vitesse)
        #vitesse = input('\nJe veux décélérer, donne moi une vitesse : ')
        #     vitesse = int(vitesse)
        # if keyboard.read_key() == "e":
        #     vitesse = input('\nJe veux décélérer, donne moi une vitesse : ')
        #     vitesse = int(vitesse)
        #     r1.deceleration(vitesse)

        # if keyboard.read_key() == "r":
        #     r1.summary()

        # if keyboard.read_key() == "s":
        #     r1.stop()self.__current_speed = self.__current_speed - 1
        #                time.sleep(0.2)

        # if keyboard.read_key() == "c":
        #     r1.charge()

        # if keyboard.read_key() == "q":
        #     r1.off()

        action = input('\nJe suis à votre service, que voulez vous que je fasse ? \n')

        if (action == "start") :
            r1.start()

        if (action == "acceleration") :
            vitesse = input('\nJe veux avancer, donne moi une vitesse : ')
            vitesse = int(vitesse)
            r1.acceleration(vitesse)

        if (action == "décélération") :
            vitesse = input('\nJe veux décélérer, donne moi une vitesse : ')
            vitesse = int(vitesse)
            r1.deceleration(vitesse)

        if (action == "summary") :
            r1.summary()

        if (action == "stop") :
            r1.stop()

        if (action == "charge") :
            r1.charge()

        if (action == "off") :
            r1.off()



    
    


        
