import matplotlib.pyplot as plt
from prettytable import PrettyTable

#Assuming basis to be 1 mole:
R = 0.008314 #MJ/kgmol.K
T = 357.6 #K
Components = ['C1','C2','C3','i-C4','n-C4','i-C5','n-C5','C6','C7']
Component_mole_PERCENTAGE = [38.68,8.20,7.55,1.93,3.17,1.38,1.13,2.1,35.37]

Component_mole_fraction = [i/100 for i in Component_mole_PERCENTAGE]

Expt_pressures = [7.341,11.339,15.373,20.786,27.680,34.575] #MPa
Expt_volumes = [0.2271,0.1629,0.1345,0.1264,0.1245,0.1226] #m3/mol

#plt.plot(Expt_volumes,Expt_pressures)plt.show()
#USING THE SRK EQUATION OF STATE
#Pc is critical pressure, Tc is critical temperature and w is accentric factor. For the different components, these values are:
print('Using the Soave Redlich Kwong Equation of state, the value of the required parameters are:')
Tc = [190.4, 305.4, 369.8, 408.2, 425.2, 460.4]

Pc = [4.6, 4.88, 4.25, 3.65, 3.8, 3.39]

w = [0.011, 0.099, 0.153, 0.183, 0.199, 0.227]


a=[(0.42748*(R**2)*(Tc[i]**(2))/Pc[i]) for i in range(len(Tc))]
Composite_a = sum([a[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('a_m =',Composite_a)

b=[(0.08664*R*(Tc[i])/Pc[i])  for i in range(len(Tc))]
Composite_b = sum([b[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('b_m =',Composite_b)
Tr = [T/Tc[i] for i in range(len(Tc))]

m = [(0.480+(1.574*w[i]) - ((0.176*(w[i])**2))) for i in range(len(Tc))]

alpha = [(1+(m[i]*(1-(Tr[i]**(0.5)))))**2 for i in range(len(Tc))]
Composite_alpha = sum([alpha[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('alpha_m =',Composite_alpha)

SRK_Pressures =[((R*T)/(Expt_volumes[i]-Composite_b))-((Composite_a*Composite_alpha)/(Expt_volumes[i]*(Expt_volumes[i] + Composite_b)))\
                for i in range(len(Expt_volumes))]

print('\n')
#USING THE PENG ROBINSON EOS
print('Using the Peng Robinson Equation of state, the value of the required parameters are:')

a1= [0.457235*(R**2)*((Tc[i])**(2))/Pc[i] for i in range(len(Tc))]
Composite_a1 = sum([a1[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('a_m =',Composite_a1)

b1= [0.077796*R*(Tc[i])/Pc[i] for i in range(len(Tc))]
Composite_b1 = sum([b1[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('bm =',Composite_b1)
m1 = [((0.374640+(1.54226*w[i]) - ((0.26992*(w[i])**2)))) for i in range(len(Tc))]

alpha1 = [((1+(m1[i]*(1-(Tr[i]**(0.5)))))**2) for i in range(len(Tc))]
Composite_alpha1 =sum([alpha1[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('alpha_m =',Composite_alpha1)

PENG_Pressures = [ (((R*T)/(Expt_volumes[i]-Composite_b1))-((Composite_a1*Composite_alpha1)/((Expt_volumes[i]*(Expt_volumes[i] + Composite_b1))+(Composite_b1*(Expt_volumes[i]-Composite_b1))))) for i in range(len(Expt_volumes))]

#REDLICH-KWONG EQUATION OF STATE
a_2=[(0.42748*(R**2)*(Tc[i]**(2.5))/Pc[i]) for i in range(len(Tc))]
Composite_a2 = sum([a_2[i]*Component_mole_fraction[i] for i in range(len(Tc))])/0.6091
print('a_m =',Composite_a2)

b_2 = Composite_b
print('b_m =',b_2)

RK_Pressures = [(((R*T)/Expt_volumes[i] - b_2) - (Composite_a2/((T**0.5)*Expt_volumes[i]*(Expt_volumes[i] + b_2)))) \
                for i in range(len(Expt_volumes))]


t= PrettyTable(['Compound', 'Expt volume (m3/mol)','Expt Pressures (MPa)','SRK_Pressures (MPa)','PENG_Pressures (MPa)','RK_Pressures (MPa)'])
for i in zip(Components,Expt_volumes,Expt_pressures,SRK_Pressures,PENG_Pressures,RK_Pressures):
    t.add_row(list(i))

print('\n')

print(' Below is the table containing the experimental values for pressure at different volumes and\n the predicted pressure values \
 obtained from the equations of state used:')
print(t)
plt.plot(Expt_volumes,Expt_pressures)
plt.plot(Expt_volumes,PENG_Pressures)
plt.plot(Expt_volumes,SRK_Pressures)
plt.plot(Expt_volumes,RK_Pressures)
plt.show()