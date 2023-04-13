import pytest
from move_class import Move, MovableObject, Vector, IMovable



def test_one():
    position = Vector(12, 5)
    velocity = Vector(-7, 3)
    my_obj = MovableObject(position, velocity) 
    Move(my_obj).Execute()
    assert my_obj.position.x == 5
    assert my_obj.position.y == 8



class BrokenObject(IMovable):
    def __init__(self, position:Vector, velocity:Vector) -> None:
        self.position = position
        self.velocity = velocity



def test_broken_getPosition():    
    position = Vector(12, 5)
    velocity = Vector(-7, 3)
    with pytest.raises(TypeError):
        obj = BrokenObject(position, velocity)
        Move(obj).Execute()


def test_broken_getVelocity():    
    position = Vector(12, 5)
    velocity = Vector(-7, 3)
    with pytest.raises(TypeError):
        obj = BrokenObject(position, velocity)
        Move(obj).Execute()


def test_broken_setPosition():    
    position = Vector(12, 5)
    velocity = Vector(-7, 3)
    with pytest.raises(TypeError):
        obj = BrokenObject(position, velocity)
        Move(obj).Execute()