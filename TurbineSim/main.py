import gas
import turbine

## Global Variables ##
timestep = 1

## Global Defines ##
def __init__():
    SimTurbine = turbine.Turbine()
    print("Generated Turbine")
    print("Starting Simulation")
    #SimTurbine.gas_content.set_canister_number(5)
    SimTurbine.gas_content.set_temperature(SimTurbine.gas_content.c_to_k(500))
    for i in range(250):
        print(f"Step: {i}")
        SimTurbine.process()
    
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
'''
1. Fix the odd temperature interaction, I think the copy is running the __init__!
2. Maybe hook this front end upto something like pygame so I can change it in realtime?
3. Maybe nab the values for other gasses because why not
4a. Build the PID System
4b. CONFIGURE THE PID SYSTEM!!

'''