import parmed as pmd

parm = pmd.load_file("system.top",xyz="system.gro")
# Load the Amber FF
ff = pmd.openmm.OpenMMParameterSet.from_parameterset(parm.parameterset)
ff.write('test.xml')
