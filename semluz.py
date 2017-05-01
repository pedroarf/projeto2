from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
#lata de 350 ml
asupc=0.029 #m^2
tf=266 #kelvin
hc=1000
ce_cerveja=4347 #J/kg.K
massacerveja=0.4 #kg
t=1
def Congelamento (tc,t):
	dtcdt=-(hc*asupc*(tc-tf))/(ce_cerveja*massacerveja)
	return dtcdt

tc0=293
tempo=np.arange (0,30,0.1)
sol=odeint(Congelamento,tc0,tempo)
a = np.array(sol)

def Cong (tc,t):
	dtcdt=-(hc*asupc*(tc-tf))/(ce_cerveja*massacerveja)
	return dtcdt


u=0
while u<=150:
	g=u*10
	if g>=30:
		if g<60:
			sol[g+1]=sol[g]-0.01
	u=u+0.1



time=np.arange (60.1,150,0.1)
solu=odeint(Cong,sol[60],time)
b = np.array (solu)
np.concatenate((a, b))

#print(solu)

#print(sol)
plt.plot(tempo,sol)
plt.title("Temperatura da cerveja entrando a 293K no Freezer de 266K")
plt.ylabel("Temperatura da cerveja [Kelvin]")
plt.xlabel("Tempo [minutos]")
plt.legend(["Temperatura da cerveja","Temperatura de congelamento"])
plt.show()
