import turbine
import loguru

## Logging Things ##


## Global Variables ##
timestep = 1

## Global Defines ##
@loguru.logger.catch
def __init__():
    SimTurbine = turbine.Turbine()
    loguru.logger.info("Generated Turbine")
    loguru.logger.info("Starting Simulation")
    SimTurbine.gas_content.set_canister_number(3)
    SimTurbine.gas_content.set_temperature(SimTurbine.gas_content.c_to_k(2000))
    for i in range(100):
        loguru.logger.info(f"Step: {i}")
        SimTurbine.process()
        if i % 2 == 0:
            SimTurbine.gas_content.set_temperature(SimTurbine.gas_content.c_to_k(2000))
    
if __name__ == "__main__":
    __init__()
    
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
# 3a. Build the PID System
# 3b. CONFIGURE THE PID SYSTEM!!