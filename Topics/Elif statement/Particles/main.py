spin = input()
el_charge = input()
particle_name = "unknown"
particle_class = "unknown"

if spin == "1/2":
    if el_charge == "-1/3":
        particle_name = "Strange"
        particle_class = "Quark"
    elif el_charge == "2/3":
        particle_name = "Charm"
        particle_class = "Quark"
    elif el_charge == "-1":
        particle_name = "Electron"
        particle_class = "Lepton"
    elif el_charge == "0":
        particle_name = "Neutrino"
        particle_class = "Lepton"
elif spin == "1" and el_charge == "0":
    particle_name = "Photon"
    particle_class = "Boson"

print(particle_name, particle_class)
