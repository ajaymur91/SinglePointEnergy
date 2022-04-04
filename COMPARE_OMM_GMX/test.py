from simtk.openmm.app import ForceField
from simtk import unit
from simtk.openmm import app
import parmed
import os

print('Reading the PDB file 1')
pdb = parmed.load_file("1.pdb")

print('Reading the force field')
ff = ForceField('nacl_dang.xml', 'spceh.xml')

print('Creating the system')
omm_system = ff.createSystem(pdb.topology,nonbondedMethod=app.NoCutoff,constraints=None,rigidWater=False)

print('Creating a structure from the OpenMM objects')
pmd_structure = parmed.openmm.load_topology(pdb.topology, system=omm_system, xyz=pdb.positions)
ENE=parmed.openmm.energy_decomposition_system(pdb, omm_system,nrg=unit.kilojoule_per_mole)

print('Saving GROMACS files')
pmd_structure.save("system.top", overwrite=True)
pmd_structure.save("system.pdb", overwrite=True)

os.system('gmx grompp -f spe.mdp -c 1.pdb -p system.top -o spe.tpr >/dev/null 2>&1')
os.system('gmx mdrun -s spe.tpr -rerun 1.pdb >/dev/null 2>&1')
os.system('echo 1 2 3 4 5 | gmx energy -f ener.edr -o ener.xvg >/dev/null 2>&1')

print('\n --------------- \n Total PE from Gromacs: \n ---------------- \n')
os.system('tail -n 15 ener.xvg')


print('\n --------------- \n Total PE from OPENMM: \n ----------------- \n')
#print(ENE)
print(ENE[0][1] + ENE[1][1] + ENE[2][1])

# remove temp files
os.system('rm -rf \#* ener.* md* *.tpr traj.trr')
