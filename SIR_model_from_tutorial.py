# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:01:29 2022

@author: habee
"""

import scipy.integrate
import numpy 
import matplotlib.pyplot as plt

#ODEs
def SIR_model(y, t, beta, gamma):
    S, I, R = y

    dS_dt = -beta*S*I
    dI_dt = beta*S*I-gamma*I
    dR_dt= gamma*I

    return([dS_dt,dI_dt,dR_dt])


#Initial Conditions

So=0.1
Io=0.9
Ro=0.0
beta=0.25
gamma=0.1

#time vector
t= numpy.linspace(0, 100, 10000)

#results
solution= scipy.integrate.odeint(SIR_model,[So,Io,Ro] , t, args=(beta, gamma))
solution=numpy.array(solution)

#plot
plt.figure(figsize=[6,4])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="R(t)")

plt.grid()
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportions")
plt.show()




