# Initialize thermodynamic states at different temperatures.
host_guest = testsystems.HostGuestVacuum()
protocol = {'temperature': [300, 310, 330, 370, 450] * unit.kelvin}
thermo_states = states.create_thermodynamic_state_protocol(host_guest.system, protocol)

# Initialize replica initial configurations.
sampler_states = [states.SamplerState(positions=host_guest.positions)
                  for _ in thermo_states]

# Propagate the replicas with Langevin dynamics.
langevin_move = mcmc.LangevinSplittingDynamicsMove(timestep=2.0*unit.femtosecond,
                                                   n_steps=n_steps)

# Run the parallel tempering simulation.
parallel_tempering = ReplicaExchange(thermo_states, sampler_states, langevin_move)
parallel_tempering.run()
