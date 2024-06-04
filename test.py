

AoA = 4 #Degrees
IAS = 125 #kts
AirDensity = 1.204 #kg/m3
WingArea =  14.8 #m2


LiftCoeffecient = .4



Lift = LiftCoeffecient * 1/2 * AirDensity * (IAS * IAS) * WingArea

print(Lift)