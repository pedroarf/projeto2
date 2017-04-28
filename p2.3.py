import matplotlib.pyplot as plt
import numpy as np
#lata de 350ml
asupc=0.029 #m^2
tf=268 #kelvin
hc=1000
ce_cerveja=4347 #J/kg.K
massacerveja=0.4 #kg
Tc=[298]
tempo=np.arange (0,200,0.1)
t=1
def temp(t,tf,tempo):
	if t<=750:
		tem=tf+10*(tempo-59)
	if t>=750:
		tem=tf+10*(74-tempo)
	return tem
def DeltaTc(hc,asupc,Tc,tf,ce_cerveja,massacerveja):
		delta=-(hc*asupc*(Tc-tf))/(ce_cerveja*massacerveja)
		return delta

t=np.arange(0,2000,1)
for t in time:
	if t<600:
		Tc.append(Tc[t-1]+DeltaTc(hc,asupc,Tc[t-1],tf,ce_cerveja,massacerveja))
	if t>900:
		Tc.append(Tc[t-1]+DeltaTc(hc,asupc,Tc[t-1],tf,ce_cerveja,massacerveja))
	if t>=600:
		if t>=900:
			Tc.append(Tc[t-1]+DeltaTc(hc,asupc,Tc[t-1],temp(t,tf,tempo[t]),ce_cerveja,massacerveja)

plt.plot(tempo,Tc)
plt.show()