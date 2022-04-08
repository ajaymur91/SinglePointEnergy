# Prepare the host-guest system for alchemical modification.
guest_atoms = host_guest.mdtraj_topology.select('resname B2')
alchemical_region = alchemy.AlchemicalRegion(alchemical_atoms=guest_atoms)
factory = alchemy.AbsoluteAlchemicalFactory()
alchemical_system = factory.create_alchemical_system(host_guest.system, alchemical_region)

# Initialize compound thermodynamic states at different temperatures and alchemical states.
protocol = {'temperature': [300, 310, 330, 370, 450] * unit.kelvin,
            'lambda_electrostatics': [1.0, 0.5, 0.0, 0.0, 0.0],
            'lambda_sterics': [1.0, 1.0, 1.0, 0.5, 0.0]}
alchemical_state = alchemy.AlchemicalState.from_system(alchemical_system)
compound_states = states.create_thermodynamic_state_protocol(
    alchemical_system, protocol=protocol, composable_states=[alchemical_state])

# Run the combined Hamiltonian replica exchange + parallel tempering simulation.
hrex_tempering = ReplicaExchange(compound_states, sampler_states, langevin_move)
