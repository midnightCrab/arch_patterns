from abc import ABC, abstractmethod
from stable_abstraction.move_class import Move


class ICommand(ABC):
 
    @abstractmethod
    def execute(self) -> None:
       pass
 
    @abstractmethod
    def undo(self) -> None:
       pass
 



class CheckFuelCommand(ICommand):    
    def __init__(self, receiver):        
        self.receiver = receiver

    def execute(self):
        self.receiver.check_fuel()

    def undo(self):
        pass


class BurnFuelCommand(ICommand):
    def __init__(self, receiver):        
        self.receiver = receiver

    def execute(self):
        self.receiver.burn_fuel()

    def undo(self):
        self.receiver.return_fuel()



class Macro_check_move_burn(ICommand):
    def __init__(self, receiver):        
        self.receiver = receiver

    def execute(self):
        commands = [
                        CheckFuelCommand(self.receiver),
                        Move(self.receiver),
                        BurnFuelCommand(self.receiver)
                    ]
        
        executed = []
        
        for command in commands:
            try:
                command.execute()
                executed.push(command)
            except:
                for cmd in executed:
                    cmd.undo()
                break
        
        if len(executed) < len(commands):
            raise AttributeError
        



class move_straight(ICommand):
    def __init__(self, receiver):        
        self.receiver = receiver
        self.move_counter = 0

    def execute(self):
        while True:
            Macro_check_move_burn(self.receiver).execute()
            self.move_counter += 1

    def undo(self):
        for _ in range(self.move_counter):
            Macro_check_move_burn(self.receiver).undo()

