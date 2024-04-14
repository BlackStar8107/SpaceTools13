from numbers import Number
from math import sqrt
import gas
from copy import copy,deepcopy
from loguru import logger

# Global Variables #
R_IDEAL_GAS_EQUATION = 8.3144626
ONE_ATMOSPHERE = 101.325
EULERS = 2.7182818284

# Main Class #
class Turbine():
    def __init__(self):
        # Initial Vars #
        self.lastgen = 0
        self.stator_load = 10000
        self.RPM = 0
        self.turbine_mass = 1000
        self.best_RPM = 600
        self.flow_rate = 200
        self.gas_content = gas.Gas()
        
        # Flags #
        self.stalling = False
        self.overspeed = False
        self.overtemp = False
        self.undertemp = False
        
        # History #
        self.history = []
        self.history_max = 50
    
    # Set Variables #
    def set_statorload(self,val):
        if val > 0 and isinstance(val, Number):
            self.stator_load = val
            
    def set_flowrate(self,val):
        if val > 0 and isinstance(val, Number):
            self.flow_rate = val
    
    def sech(self,x):
        #return (2 / ((EULERS ** x) - 1) + ((EULERS ** -x) + 0.000001))
        return (2 / ((EULERS ** x) + (EULERS ** -x) + 0.000001))
    
    def byond_round(self,x, y):
        return y * round(x/y)
    
    # Main Process Call #
    def process(self):
        self.air_contents = copy(self.gas_content)
        gas = self.gas_content
        
        logger.debug(f"Gasinit: {gas.temperature} mol",)
        logger.debug(f"NewGas: {self.air_contents.temperature} mol")
        if len(self.history) > self.history_max:
            self.history.pop(0) # Remove the OLDEST entry
        
        self.history.append([self.RPM,self.stator_load,self.lastgen])
        
        input_starting_pressure = gas.mixture_pressure()
        logger.debug(f"Starting Pressure: {input_starting_pressure}kPa")
        
        transfer_moles = 0
        
        if input_starting_pressure:
            transfer_moles = (gas.volume * input_starting_pressure) / (R_IDEAL_GAS_EQUATION * gas.temperature)
        
        gas.recalc_moles()
        self.air_contents.total_moles = gas.total_moles - transfer_moles
        
        self.overtemp = gas.temperature > 2500
        self.undertemp = gas.temperature < gas.c_to_k(20)
        
        if(gas.temperature > 3000):
            logger.warning(f"Turbine overheating!\n Temperature: {gas.temperature}K!")
        else:
            gas.recalc_thermal_energy()
            input_starting_energy = gas.thermal_energy
            input_heat_cap = gas.heat_capacity
            
            if input_starting_energy <= 0:
                input_starting_energy = 1
            if input_heat_cap <= 0:
                input_heat_cap = 1
            if gas.temperature > gas.c_to_k(20):
                gas.set_temperature(self.byond_round(max((input_starting_energy - ((input_starting_energy - (input_heat_cap * gas.c_to_k(20))) * .8)) / input_heat_cap,gas.c_to_k(20)),0.01))
                
            gas.recalc_thermal_energy()
            output_starting_energy = gas.thermal_energy
            energy_generated = self.stator_load * (self.RPM / 60)
            delta_E = input_starting_energy - output_starting_energy
            logger.debug(f"input_starting_energy: {input_starting_energy}")
            logger.debug(f"output_starting_energy: {output_starting_energy}")
            logger.debug(f"Delta_E: {delta_E}")
            
            newRPM = 0
            
            if delta_E - energy_generated > 0:
                newRPM = self.RPM + sqrt(2 * (max(delta_E - energy_generated,0)) / self.turbine_mass)
            else:
                newRPM = self.RPM - sqrt(2 * (max(energy_generated - delta_E,0)) / self.turbine_mass)
                
            nextgen = self.stator_load * (max(newRPM,0) / 60)
            nextRPM = 0
            
            if delta_E - nextgen > 0:
                nextRPM = max(newRPM,0) + sqrt(2 * (max(nextgen - delta_E,0)) / self.turbine_mass)
            else:
                nextRPM = max(newRPM,0) - sqrt(2 * (max(delta_E - nextgen,0)) / self.turbine_mass)
                
            if newRPM < 0 or nextRPM < 0:
                self.stalling = True
                self.RPM = 0
            else:
                self.stalling = False
                self.RPM = nextRPM
            
            self.lastgen = self.stator_load * (self.RPM / 60) * self.sech(0.01 * (self.RPM - self.best_RPM))
            
            self.overspeed = self.RPM > self.best_RPM * 1.2
            
            self.gas_content.volume = self.flow_rate
            self.air_contents.volume = self.flow_rate
            
            logger.info(f"RPM:{self.RPM}")
            logger.debug(f"NewRPM: {newRPM}")
            logger.debug(f"NextRPM: {nextRPM}")
            logger.debug(f"Stalling: {self.stalling}")
            logger.debug(f"Overspeed: {self.overspeed}")
            logger.debug(f"Gas Temp: {gas.temperature}K")