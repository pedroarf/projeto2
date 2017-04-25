from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

asup = 0.029 #m^2
tf = 269#kelvin
tc0 = 293
hs = 100
calor_especifico = 1.01# cal/g
massa_especifica = 1.02 #g/c^3
massa = 403 #g
def Congelamento (tc,t):
	dtcdt = -(hs*asup*(tc-tf))/(calor_especifico * massa)
	return dtcdt


tempo = np.arange (0,500,0.1)
sol = odeint(Congelamento,tc0,tempo)
plt.plot (tempo, sol)
plt.show()
