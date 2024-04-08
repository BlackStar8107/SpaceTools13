import turbine
import PID
import loguru
from random import randrange
from matplotlib import pyplot as plt
from matplotlib import animation as anm
from os import curdir

## Global Variables ##
# Default Timestep for SS13 is 1
TIMESTEP = .025
# Reactor Temperature and Random Fluctuation
REACTOR_OFFTEMP = 300
REACTOR_TEMP_RANGE = 1
# How many canisters of gas are in the turbine
CANISTER_NUMBER = 1
SIMULATION_LENGTH = 1000
# Enable Graphs
VISUAL_ENABLED = False
# Should the graph be cleared every x
PERIOD_CLEAR = True
PERIOD = 150

## Main Code Body ##
## DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING!! ##

@loguru.logger.catch
def __init__():
    loguru.logger.add("TurbineSim.log")
    SimTurbine = turbine.Turbine()
    # TU = 2 steps
    # KU = 0.6
    # KI = 0.36 or 360 or 36
    # KD = 0.09
    #SimPID = PID.PIDController(600,.6,0,0)
    SimPID = PID.PIDController(600,0.6,36,0.09)
    loguru.logger.info("Generated Turbine")
    SimTurbine.gas_content.set_canister_number(CANISTER_NUMBER)
    SimTurbine.set_flowrate(5000)
    #SimTurbine.set_statorload(75000)
    loguru.logger.info("Starting Simulation")
    for i in range(SIMULATION_LENGTH):
        loguru.logger.info(f"Step: {i}")
        if i % 2 == 0:
            SimTurbine.gas_content.set_temperature(SimTurbine.gas_content.c_to_k(randrange(REACTOR_OFFTEMP - REACTOR_TEMP_RANGE, REACTOR_OFFTEMP + REACTOR_TEMP_RANGE)))
        SimTurbine.process()
        SimTurbine.set_statorload(SimPID.process(SimTurbine.RPM))
        
        # [self.RPM,self.stattor_load,self.lastgen]
        if i % PERIOD == 0 and PERIOD_CLEAR:
            x_data = []
            rpm_data = []
            stator_data = []
            line_data = []
            plt.cla()
            
        x_data.append([i,i])
        rpm_data.append(SimTurbine.history[-1][0])
        stator_data.append(SimTurbine.history[-1][1])
        line_data.append([600, 600])
        if VISUAL_ENABLED:
            plt.plot(x_data,rpm_data,c="blue", label = "RPM")
            plt.plot(x_data, stator_data,c="orange", label = "Stator Load")
            plt.plot(x_data, line_data, c="red", label = "Ideal RPM")
            plt.legend(["RPM","Stator Load","Ideal RPM"])
            plt.pause(TIMESTEP)
            plt.draw()

if __name__ == "__main__":
    __init__()
    if VISUAL_ENABLED:
        plt.show()
    
###################################
##   _______      _____          ##
##  |__   __|    |  __ \         ##
##     | | ___   | |  | | ___    ##
##     | |/ _ \  | |  | |/ _ \   ##
##     | | (_) | | |__| | (_) |  ##
##     |_|\___/  |_____/ \___/   ##
##                               ##
###################################
# 1. Maybe hook this front end upto something like pygame so I can change it in realtime?
# 2. Maybe nab the values for other gasses because why not