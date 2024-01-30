from abc import ABCMeta
from abc import abstractmethod


'''
# EXO 

## Exigences

* En tant que client, je veux pouvoir jouer avec trois types de Véhicules différents : UUV, UAV, UGV
* Seul les Véhicules finaux doivent être utilisables
* Un Véhicules Unmanned doit exécuter une mission
* Mettre en avant un principe de classe abstraite
* Mettre en avant un principe de polymorphisme
* Mettre en avant un principe d'héritage multiple
* Pas d'algorithmes complexes, juste des print ;

### Aide

Sortez un bon vieux crayon pour schématiser vos dépendances d'héritages
'''

	
class Unmanned(metaclass=ABCMeta):
    @property
    @abstractmethod
    def presentation(self):
        pass

    def connection(self):
        print("Je suis bien connecté\n")

class Vehicule(metaclass=ABCMeta):
    @property
    @abstractmethod
    def speed(self):
        pass

    def move(self):
        print("Je suis entrain de bouger\n")

class UUV(Unmanned,Vehicule):

    def presentation(self):
        print("Je suis un UUV\n")
	
    def speed(self):
        print("Je vais à 6 knots\n")
    
    def verite (self):
        print("en vrai c'est moi le meilleur ")

class UAV(Unmanned,Vehicule):
	
    def presentation(self):
        print("Je suis un UAV\n")

    def speed(self):
        print("Je vais à 44km/h\n")

class UGV(Unmanned,Vehicule):
	
    def presentation(self):
        print("Je suis un UGV\n")

    def speed(self):
        print("Je vais à 20km/h\n")

def sherch(u: Unmanned) -> bool:

    print("On va chercher qui a une méthode vérité")
    u.connection()
    try:
        u.verite()
	
    except Exception as e:
        print(e, "  << mauvais appel, on est allé trop loin dans l'attente de l'objet")
	
    finally:
        print()
    try:
        u.verite()
	
    except Exception as e:
        print(e, "  << mauvais appel, on est allé trop loin dans l'attente de l'objet")
	
    finally:
        print()

Vehic = [
    UUV(), UAV(), UGV()
]

for r in Vehic :
    sherch(r)
        
	
if issubclass(UUV, Vehicule):
    if issubclass(UUV,Unmanned):
        print("\nL'UUV est un véhicule et un Unmanned askip\n")

uuv = UUV()
uuv.presentation()
uuv.move()
uuv.connection()
uuv.speed()

uav = UAV()
uav.presentation()
uav.move()
uav.connection()
uav.speed()

ugv = UGV()
ugv.presentation()
ugv.move()
ugv.connection()
ugv.speed()
