# SinglePointEnergy
gmx grompp -f sp.mdp -c NACL_1.gro -p NACL_1.top -o parmed.tpr

gmx mdrun -deffnm parmed -rerun NACL_1.gro

echo 1 2 3 | gmx energy -f parmed.edr -o parmed.xvg 


Energy                      Average   Err.Est.       RMSD  Tot-Drift

-------------------------------------------------------------------------------

LJ (SR)                  -0.00255319         --          0          0  (kJ/mol)

Coulomb (SR)               -163.689         --          0          0  (kJ/mol)

Potential                  -163.691         --          0          0  (kJ/mol)


python spe.py 

Warning: importing 'simtk.openmm' is deprecated.  Import 'openmm' instead.

[('NonbondedForce', -163.68870544433594), ('CustomNonbondedForce', -0.00255318870767951), ('CMMotionRemover', 0.0)]


