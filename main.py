import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def vogelipr():
    porosity = float(input("Enter Porosity: "))
    K = float(input("Enter Perm.(md): "))
    h = float(input("Enter pay zone thickness(Feet): "))
    P = float(input("Enter Reservoir Pressure(psi): "))
    Pb = float(input("Enter Bubble Point Pressure(psi): "))
    Bo = float(input("Enter Formation Volume Factor: "))
    Viscosity = float(input("Enter fluid viscosity(cp): "))
    ct = float(input("Enter Total Compressibility(psi-1): "))
    A = float(input("Enter Drainage Area(Acres): "))
    re = np.sqrt(43560 * A / 3.14)
    rw = float(input("Enter Wellbore radius(ft): "))
    S = float(input("Enter Skin Factor: "))
    J = K * h / (141.2 * Bo * Viscosity * (np.log(re / rw) - 0.75 + S))
    print("The value of productivity index is", J)
    qmax = J * P / 1.8
    print("The value of Absolute open flow is ", qmax, "stb/day")
    a = np.arange(0, P, 500)
    b = np.append(a, P)
    pwf = b[-1::-1]
    flowrate = []
    for i in pwf:
        q = qmax * (1 - 0.2 * (i / P) - 0.8 * ((i / P) ** 2))
    flowrate.append(q)
    flowrates = np.array(flowrate)
    plt.figure(figsize=(9, 6))
    plt.plot(flowrates, pwf, c="red", linewidth=3)
    plt.xlabel("Flowrate(stb/day)")
    plt.ylabel("pwf(psia)")
    plt.grid(True)
    plt.title("Vogel's IPR for Saturated Reservoir")
print(vogelipr())



