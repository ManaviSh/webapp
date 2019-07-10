import math
import scipy as np
def getSOC(power):
    P=power
    Voc = 400
    R = 0.1
    c=90 #in kwh
    I = (Voc - math.sqrt(math.Voc** - 4*R*P))/2*R
    SOC = np.trapz(Voc*I)/(c*3600*1000)
    soc_percent = SOC*100
    return soc_percent