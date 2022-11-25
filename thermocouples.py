import matplotlib.pyplot as plt
from math import pow
from math import e

def thermocouple_typeB (): 
    temperature = 0
    aux_soma    = 0
    points      = []

    coefficient_B = [ 0.000000000000*pow(10,0),  -0.246508183460*pow(10,-3),    0.590404211710*pow(10,-5),
                     -0.132579316360*pow(10,-8),  0.156682919010*pow(10,-11),  -0.169445292400*pow(10,-14),
                      0.629903470940*pow(10,-14) ]

    while temperature <= 300:
        for const in coefficient_B:
            soma = const*pow(temperature, (coefficient_B.index(const)))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1
            
    return points

def thermocouple_typeE ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    coefficient_E = [ 0.000000000000*pow(10,0),    0.586655087100*pow(10,-1),   0.450322755820*pow(10,-4),
                      0.289084072120*pow(10,-7),  -0.330568966520*pow(10,-9),   0.650244032700*pow(10,-12),
                     -0.191974955040*pow(10,-15), -0.125366004970*pow(10,-17),  0.214892175690*pow(10,-20),
                     -0.143880417820*pow(10,-23),  0.359608994810*pow(10,-27)  ]       

    while temperature <= 300:
        for const in coefficient_E:
            soma = const*pow(temperature, coefficient_E.index(const))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1
            
    return points

def thermocouple_typeJ ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    coefficient_J = [ 0.000000000000*pow(10,0),    0.503811878150*pow(10,-1),  0.304758369300*pow(10,-4), 
                     -0.856810657200*pow(10,-7),   0.132281952950*pow(10,-9), -0.170529583370*pow(10,-12), 
                      0.209480906970*pow(10,-15), -0.125383953360*pow(10,-18), 0.156317256970*pow(10,-22)  ]

    while temperature <= 300:
        for const in coefficient_J:
            soma = const*pow(temperature, coefficient_J.index(const))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1

    return points
    
def thermocouple_typeK ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    a_0 = 0.118597600000*pow(10,0)
    a_1 = -0.118343200000*pow(10,-3)
    a_2 = 0.126968600000*pow(10,3)
    parcela = pow(a_1*(temperature - a_2), 2)
    
    coefficient_K = [-0.176004136860*pow(10,-1),   0.389212049750*pow(10,-1),   0.185587700320*pow(10,-4), 
                     -0.994575928740*pow(10,-7),   0.318409457190*pow(10,-9),  -0.560728448890*pow(10,-12),
                      0.560750590590*pow(10,-15), -0.320207200030*pow(10,-18),  0.971511471520*pow(10,-22), 
                     -0.121047212750*pow(10,-25)   ]

    while temperature <= 300:
        if temperature == 0:
            for const in coefficient_K:
                soma = ((const*pow(temperature, coefficient_K.index(const))) + a_0*pow(e, parcela))
                aux_soma += soma
        else:    
            for const in coefficient_K:
                soma = const*pow(temperature, coefficient_K.index(const))
                aux_soma += soma
                
        points.append(aux_soma)
        temperature += 1

    return points

def thermocouple_typeN ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    coefficient_N = [ 0.000000000000*pow(10,0),    0.259293946010*pow(10,-1),   0.157101418800*pow(10,-4), 
                      0.438256272370*pow(10,-7),  -0.252611697940*pow(10,-9),   0.643118193390*pow(10,-12), 
                     -0.100634715190*pow(10,-14),  0.997453389920*pow(10,-18), -0.608632456070*pow(10,-21), 
                      0.208492293390*pow(10,-24), -0.306821961510*pow(10,-28)   ]

    while temperature <= 300:
        for const in coefficient_N:
            soma = const*pow(temperature, coefficient_N.index(const))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1

    return points


def thermocouple_typeR ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    coefficient_R = [ 0.000000000000*pow(10,0),    0.528961729765*pow(10,-2),   0.139166589782*pow(10,-4), 
                     -0.238855693017*pow(10,-7),   0.356916001063*pow(10,-10), -0.462347666298*pow(10,-13), 
                      0.500777441034*pow(10,-16), -0.373105886191*pow(10,-19),  0.157716482367*pow(10,-22), 
                     -0.281038625251*pow(10,-26) ]

    while temperature <= 300:
        for const in coefficient_R:
            soma = const*pow(temperature, coefficient_R.index(const))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1
    return points


def thermocouple_typeS ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    coefficient_S = [ 0.000000000000*pow(10,0),    0.540313308631*pow(10,-2),   0.125934289740*pow(10,-4), 
                     -0.232477968689*pow(10,-7),   0.322028823036*pow(10,-10), -0.331465196389*pow(10,-13),
                      0.255744251786*pow(10,-16), -0.125068871393*pow(10,-19),  0.271443176145*pow(10,-23) ]

    while temperature <= 300:
        for const in coefficient_S:
            soma = const*pow(temperature, coefficient_S.index(const))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1

    return points

def thermocouple_typeT ():
    temperature = 0
    aux_soma    = 0
    points      = []
    
    coefficient_T = [ 0.000000000000*pow(10,0),   0.387481063640*pow(10,-1),   0.332922278800*pow(10,-4),  
                      0.206182434040*pow(10,-6), -0.218822568460*pow(10,-8),   0.109968809280*pow(10,-10), 
                      0.308157587720*pow(10,-13), 0.454791352900*pow(10,-16), -0.275129016730*pow(10,-19)  ]

    while temperature <= 300:
        for const in coefficient_T:
            soma = const*pow(temperature, coefficient_T.index(const))
            aux_soma += soma
        points.append(aux_soma)
        temperature += 1
        

    return points

def main():
    plt.figure(figsize=(7,4))
    
    plt.plot(thermocouple_typeB(), label = 'Type B')
    plt.plot(thermocouple_typeE(), label = 'Type E')
    plt.plot(thermocouple_typeJ(), label = 'Type J')
    plt.plot(thermocouple_typeK(), label = 'Type K')
    plt.plot(thermocouple_typeN(), label = 'Type N')
    plt.plot(thermocouple_typeR(), label = 'Type R')
    plt.plot(thermocouple_typeS(), label = 'Type S')
    plt.plot(thermocouple_typeT(), label = 'Type T')
    
    plt.title('Thermocouples Equations')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Thermoelectric Voltage (mV)')
    plt.legend()
    plt.show()
    plt.savefig('termocouples.png')
    
main()
