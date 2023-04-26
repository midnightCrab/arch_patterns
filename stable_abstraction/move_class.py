from abc import ABC, abstractmethod


class Vector:

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)



class IMovable(ABC):
 
    @abstractmethod
    def getPosition(self) -> Vector:
       pass
 
    @abstractmethod
    def getVelocity(self) -> Vector:
       pass
 
    @abstractmethod
    def setPosition(self,  newV:Vector) -> None:
       pass
 



class Move:     

    def __init__(self, m: IMovable):        
        self.m = m

    def execute(self):
        new_position = self.m.getPosition() +  self.m.getVelocity()
        self.m.setPosition(new_position)

    def undo(self):
        old_position = self.m.getPosition() - self.m.getVelocity()
        self.m.setPosition(old_position)



class MovableObject(IMovable):

    def __init__(self, position:Vector, velocity:Vector) -> None:
        self.position = position
        self.velocity = velocity

    def getPosition(self) -> Vector:
        return self.position
    
    def getVelocity(self) -> Vector:
        return self.velocity

    def setPosition(self,  newV:Vector) -> None:
       self.position = newV