import numpy as np

def readfile(filename):
    data =  np.loadtxt(filename,skiprows=11,dtype=float,usecols=(0,2,3,4),unpack=True)
    return (data)

def parser(filename):
    print('reading',filename)
    data = readfile(filename)
    return (data)

#read file
#read 1yplus file
def getdata():    
    #Initial the array
    data=np.ones([6,4,98],dtype=float)
    data[0] = parser('/home/yyc/run/CO-predict/diffusion-FR5/diffusion-FR5-measure.dat')
    data[1] = parser('/home/yyc/run/CO-predict/diffusion-TF5/diffusion-TF5-measure.dat') 
    data[2] = parser('/home/yyc/run/CO-predict/premix-FR5/premix-FR5-measure.dat')
    data[3] = parser('/home/yyc/run/CO-predict/premix-TF5/premix-TF5-measure.dat')

    data[4][0][0:5] = np.loadtxt('/home/yyc/run/CO-predict/expData/T-noCooling.dat',skiprows=1,dtype=float,usecols=(1),unpack=True)
    data[4][0][0:5] = data[3][0][0:5]+273.15
    data[5][3][0:5] = np.loadtxt('/home/yyc/run/CO-predict/expData/COppm-noCooling.dat',skiprows=1,dtype=float,usecols=(0),unpack=True)
    return (data)
