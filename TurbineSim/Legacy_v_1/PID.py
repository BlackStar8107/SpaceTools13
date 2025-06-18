from loguru import logger

class PIDController(object):
    def __init__(self, target, KP = 1, KI = 1, KD = 1, TIMESTEP = 1) -> None:
        self.kp = KP
        self.ki = KI
        self.kd = KD
        self.timestep = TIMESTEP
        self.target = target
        self.error = 0
        self.int_error = 0
        self.error_l = 0
        self.derv_error = 0
        
    def process(self, input):
        #self.error = self.target - input # The PID knows where it is at all times it knows this because it knows where it isn't
        self.error = input - self.target
        self.int_error += self.error * self.timestep
        self.derv_error = (self.error - self.error_l) / self.timestep
        self.error_l = self.error
        output = (self.kp * self.error + self.ki * self.int_error + self.kd * self.derv_error)
        logger.debug(f"Error: {self.error}")
        logger.debug(f"Inegral Error: {self.int_error}")
        logger.debug(f"Derivative Error: {self.derv_error}")
        logger.debug(f"Error Last: {self.error_l}")
        logger.info(f"PID: {output}")
        return output