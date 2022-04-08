from openmmtools import alchemy

# Create the reference OpenMM System that will be alchemically modified.
lysozyme_pxylene = testsystems.LysozymeImplicit()
t4_system = lysozyme_pxylene.system

# Define the region of the System to be alchemically modified.
pxylene_atoms = lysozyme_pxylene.mdtraj_topology.select('resname TMP')
#alchemical_region = alchemy.AlchemicalRegion(alchemical_atoms=pxylene_atoms)

# Soft core
alchemical_region = alchemy.AlchemicalRegion(alchemical_atoms=pxylene_atoms,
                                             softcore_alpha=0.5, softcore_c=6)

factory = alchemy.AbsoluteAlchemicalFactory()
alchemical_system = factory.create_alchemical_system(t4_system, alchemical_region)

alchemical_state = alchemy.AlchemicalState.from_system(alchemical_system)
alchemical_state.lambda_electrostatics = 0.0
alchemical_state.lambda_sterics = 0.5
alchemical_state.apply_to_context(context)


