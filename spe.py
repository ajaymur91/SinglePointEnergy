import parmed
from openmm import unit
parm = parmed.load_file("NACL_1.top",xyz="NACL_1.gro")
system=parm.createSystem()
print(parmed.openmm.energy_decomposition_system(parm, system,nrg=unit.kilojoules_per_mole))

#Learn more from https://github.com/ParmEd/ParmEd
