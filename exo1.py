import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    def __init__(self):
        self.__name = "Grégoire"
        print("Mon nom est : ", self.__name)
	
    def allumage(self):
        self.__power = self.__states[0]
        print("La batteri est allumée mon reuf")

    def eteignage(self):
        self.__power = self.__states[1]

    def charge(self):
        while (self.__battery_level <100) :
                print("La batterie est à : ", self.__battery_level, "%")
                self.__battery_level = self.__battery_level + 1
                time.sleep(1)
        if (self.__battery_level == 100):
            print("La batterie est full mon reuf")
        
