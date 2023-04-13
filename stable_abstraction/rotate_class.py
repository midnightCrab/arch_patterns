from abc import ABC, abstractmethod


class IRotable(ABC):
    @abstractmethod
    def getDirection() -> int:
        pass

    @abstractmethod
    def getAngularVelocity() -> int:
        pass

    @abstractmethod
    def setDirection(newD: int) -> None:
        pass

    @abstractmethod
    def getDirectionsNumber() -> int:
        pass



class Rotate:

    def __init__(self, r: IRotable):        
        self.r = r

    def Execute(self):
        directionsNumber = self.r.getDirectionsNumber()
        new_direction = (self.r.getDirection() + self.r.getAngularVelocity()) % directionsNumber        
        self.r.setDirection(new_direction)
    



class RotableObject(IRotable):

    def __init__(self, direction:int, angVelocity:int) -> None:
        self.direction = direction
        self.angVelocity = angVelocity

    def getDirection(self) -> int:
        return self.direction
    
    def getAngularVelocity(self) -> int:
        return self.angVelocity
    
    def setDirection(self, newD: int) -> None:
        self.direction = newD

    def getDirectionsNumber(self) -> int:
        return 8