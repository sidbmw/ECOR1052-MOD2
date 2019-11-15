import time

class PID:
    def __init__(self, kP, kI, kD):
        #initialize gains
        self.kP = kP
        self.kI = kI
        self.kD = kD

    def initialize(self):
        #init current and previous time
        self.currTime = time.time()
        self.prevTime = self.currTime

        #init the previous error
        self.prevError = 0

        #init the term result vars

        self.cP = 0
        self.cI = 0
        self.cD = 0

    def update(self, error, sleep=0.2):
        time.sleep(sleep)

        #grab current time and get delta time
        self.currTime = time.time()
        deltaTime = self.currTime - self.prevTime

        #delta error
        deltaError = error - self.prevError

        #proportional term
        self.cP = error

        #integral term

        self.cI += error * deltaTime

        #derivative term and divide by zero
        self.cD = (deltaError / deltaTime) if deltaTime > 0 else 0

        #save previous time and error for the next update
        self.prevTime = self.currTime
        self.prevError = error

        #sum the terms and return
        return sum([
            self.kP * self.cP,
            self.kI * self.cI,
            self.kD * self.cD])
    
