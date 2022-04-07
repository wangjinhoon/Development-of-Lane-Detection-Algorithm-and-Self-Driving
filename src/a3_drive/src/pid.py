class PID:
    def __init__(self, kp, ki, kd):
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd
        self.p_error = 0.0 # current error at time t
        self.i_error = 0.0 # cumulative
        self.d_error = 0.0 # rate of change

    def pid_control(self, cte):
        self.d_error = cte - self.p_error # current error - previous error
        self.p_error = cte # current error
        self.i_error += cte # cumulative error

        return self.Kp*self.p_error + self.Ki*self.i_error + self.Kd*self.d_error