class PID():
    def __init__(self, kp,ki, kd):
        self.Kp=0.0
        self.Ki=0.0
        self.Kd=0.0
        self.p_error=0.0
        self.i_error=0.0
        self.d_error=0.0

    def pid_control(self,cte):
        self.d_error=cte-self.p_error
        self.p_error=cte
        self.i_error+=cte

        return self.Kp*self.p_error + self.Ki*self.i_error + self.Kd*self.d_error