from math import sin, cos
from scipy.constants import g, pi

####################
# weitere Konstanten
# Luftdichte:
luftdichte = 1.205 # kg/m^3
# Masse des Autos:
m = 1011 # kg
# Aerodynamischer Widerstandsbeiwert:
cw = 0
# Frontfläche:
A = 0
# Verlust durch rotierende Massen:
C_rot = 0
#####################
# Funktionen zur berechnung der Fahrtwiderstände
# pV: momentane Geschwindigkeit (m/s
# pa: momentane Beschleunigung (m/s^2)
# pAlpha: steigungswinkel (rad)

def f(pV):
    return 1
def F_ST(pAlpha):
    return m*g*sin(pAlpha)
def F_r(pV, pAlpha):
    return m*g*f(pV)*cos(pAlpha)
def F_L(pV):
    return ((luftdichte)/2)*cw*A*(pV**2)
def F_a(pa):
    return (1+C_rot)*m*pa
def F_w(pV, pa, pAlpha):
    return F_ST(pAlpha)+F_r(pV,pAlpha)+F_L(pV)+F_a(pa)

#####################
# Funktionen zur Momentanen Bestimmung der Leistung des Motors
# Variante 1:
def leistung_1(pV, pa ,pAlpha):
    # pV: momentane Geschwindigkeit
    # pa: momentane Beschleunigung
    # pAlpha: steigungswinkel
    return F_w(pV, pa, pAlpha) * pV

def leistung_2(pL,pRPM):
    pass