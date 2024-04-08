from numbers import Number
from copy import deepcopy

# Global Variables #
R_IDEAL_GAS_EQUATION = 8.3144626
ONE_ATMOSPHERE = 101.325

# Defaults to CO2 #
class Gas():
    def __init__(self):
        self.specific_heat = 40
        self.temperature = self.c_to_k(20) # Should be about room temp - IS IN KELVIN IDIOT!!!
        self.volume = 1000 # Default of 1 Canister being in the system
        self.max_pressure = (90*101.325) # Default Max Pressure of a Canister
        self.filled = 0.5 # This just is .5
        self.canister_number = 1
        self.recalc_moles()
        self.recalc_thermal_energy()
        
    def __copy__(self):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone
        
    def mixture_pressure(self):
        self.recalc_moles()
        return (self.total_moles * self.canister_number) * R_IDEAL_GAS_EQUATION * self.temperature / self.volume
    
    def recalc_moles(self):
        self.total_moles = (self.max_pressure * self.filled) * self.volume / (R_IDEAL_GAS_EQUATION * self.temperature)
    
    def recalc_heat_capacity(self):
        self.heat_capacity = self.total_moles * self.specific_heat
        
    def recalc_thermal_energy(self):
        self.recalc_heat_capacity()
        self.thermal_energy = self.temperature * self.heat_capacity
    
    def c_to_k(self,temp):
        return temp + 273.15
    
    def k_to_c(self,temp):
        return temp - 273.15
    
    def set_canister_number(self,amount):
        if amount >= 0 and isinstance(amount, Number):
            self.canister_number = amount
        self.recalc_moles()
        
    def set_temperature(self, temperature):
        if temperature >= 0 and isinstance(temperature, Number):
            self.temperature = temperature