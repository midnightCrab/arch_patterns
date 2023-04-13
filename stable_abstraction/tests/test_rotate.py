import pytest
from rotate_class import Rotate, RotableObject

def test_rotate():
    
    ro = RotableObject(10, 20)
    Rotate(ro).Execute()
    assert ro.direction == 6