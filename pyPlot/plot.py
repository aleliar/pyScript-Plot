import read
import numpy as np
import matplotlib as plt
plt.use('Qt5Agg')
import matplotlib.pyplot as mpt
import math

#Function for profiles without errorbar,term is the rank number of species
def profile(data,term,ymax):
    x=np.arange(-0.98,0.98,0.02,dtype=float)
    mpt.plot(x,data[0][term],color='brown',label="diffusion-FR")
    mpt.plot(x,data[1][term],color='r',label="diffusion-TF")
    mpt.plot(x,data[2][term],color='b',label="premix-FR")
    mpt.plot(x,data[3][term],color='purple',label="premix-TF")
    if term==0:
        mpt.scatter(np.arange(-0.794,1.191,0.397,dtype=float),data[4][term][0:5],color='black',marker='s',label="Exp.")
    elif term==3:
        mpt.scatter(np.arange(-0.794,1.191,0.397,dtype=float),data[5][term][0:5],color='black',marker='s',label="Exp.")
    mpt.xlim(-1,1)
    mpt.ylim(0,ymax)
    mpt.xlabel("normalized height")
    label=np.array(['T','Yc','Ych4','COppm'])
    mpt.ylabel(label[term])
    mpt.legend(loc=4)
    mpt.savefig(label[term]+'profile.png')
    mpt.show()

#Function for profiles with errorbar, use ymax to define the size
def errprofile(data,term,ymax):
    x=np.arange(-0.98,0.98,0.02,dtype=float)
    mpt.plot(x,data[0][term],color='brown',label="premix-TF")
    mpt.plot(x,data[1][term],color='r',label="premix-FR")
    mpt.plot(x,data[2][term],color='b',label="diffusion-TF")
    mpt.plot(x,data[3][term],color='purple',label="premix-TF")
    if term==0:
        Terror = np.array([data[4][0][0:5]*0.2,data[4][0][0:5]*0.2])
        mpt.errorbar(np.arange(-0.794,1.191,0.397,dtype=float),data[4][term][0:5],yerr=Terror,color='black',marker='s',linestyle="none",capsize=5,label="T-Exp.")
    elif term==3:
        COerror = np.array([data[5][3][0:5]*0.2,data[5][3][0:5]*0.2])
        mpt.errorbar(np.arange(-0.794,1.191,0.397,dtype=float),data[5][term][0:5],yerr=COerror,color='black',marker='s',linestyle="none",capsize=5,label="COppm-Exp.")
    mpt.xlim(-1,1)
    mpt.ylim(0,ymax)
    mpt.xlabel("normalized height")
    label=np.array(['T','Yc','Ych4','COppm'])
    mpt.ylabel(label[term])
    mpt.legend(loc=4)
    mpt.savefig(label[term]+'errProfile.png')
    mpt.show()

data=read.getdata()
print()
profile(data,0,2200)
errprofile(data,0,2200)
profile(data,3,5000)
errprofile(data,3,5000)


