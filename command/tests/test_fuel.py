import pytest
from command import CheckFuelCommand


class refueled_object():
    def __init__(self, fuel_count:int, speed_fuel_burn:int) -> None:
        self.fuel_count = fuel_count
        self.speed_fuel_burn = speed_fuel_burn


    def check_fuel(self):
        if self.fuel_count == 0:
            raise AttributeError
    
    def burn_fuel(self):
        self.fuel_count -= self.speed_fuel_burn

    def return_fuel(self):
        self.fuel_count += self.speed_fuel_burn

def test_check_fuel_exception():
    ro = refueled_object(0, 1)
    cf_command = CheckFuelCommand(ro)
    with pytest.raises(AttributeError):
        cf_command.execute()



@pytest.mark.parametrize("fuel_count, speed_fuel_burn, fuel_remainder", [
                                                      (10, 1, 9)
                                                      ])
def test_burn_fuel(fuel_count, speed_fuel_burn, fuel_remainder):
    ro = refueled_object(fuel_count, speed_fuel_burn)
    bf_command = CheckFuelCommand(ro)
    bf_command.execute()
    assert ro.fuel_count == fuel_remainder

