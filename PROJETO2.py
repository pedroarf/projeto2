from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

#lata de 350ml
asupc=0.029 #m^2
asupl=0.03 #m^2
tf=268 #kelvin
hc=300
kl=204
dl=0.0028
ce_cerveja=1.04 #cal/g*grau
ce_aluminimo=0.22 #cal/g*grau
massacerveja=400 #g
massalata=415 #g
def Congelamento (Y,t):
	tc=Y[0]
	tl=Y[1]
	dtldt=((kl*asupc)/dl)*(tc-tl)/(ce_cerveja*massacerveja)-(hc*asupl*(tl-tf))/(ce_aluminimo*massalata)
	dtcdt=-(((kl*asupc)/dl)*(tc-tl))/(ce_cerveja*massacerveja)
	return ([dtcdt,dtldt])

Y0=[290,298]

tempo=np.arange (0,200,0.1)
sol=odeint(Congelamento,Y0,tempo)
plt.plot(tempo, sol)
plt.show()
