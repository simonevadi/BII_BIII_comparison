from raypyng import Simulate
import numpy as np
import os

from parameter import rml_file_name_kb as rml_file_name

this_file_dir=os.path.dirname(os.path.realpath(__file__))
rml_file = os.path.join('rml/'+rml_file_name+'.rml')

sim = Simulate(rml_file, hide=True)

rml=sim.rml
beamline = sim.rml.beamline

# cpu
ncpu=1

# rounds
rounds = 1

# name for simulation folder
sim_name = rml_file_name+'_FLUX'

# define the values of the parameters to scan 
from parameter import order, energy_flux as energy
from parameter import SlitSize, cff, nrays_flux as nrays


# define a list of dictionaries with the parameters to scan
params = [  
            {beamline.PG.cFactor:cff}, 

            {beamline.ExitSlit.totalHeight:SlitSize},
            
            {beamline.SU.photonEnergy:energy},
            
            {beamline.PG.orderDiffraction:order},

            {beamline.SU.numberRays:nrays}
        ]

#and then plug them into the Simulation class
sim.params=params

# sim.simulation_folder = '/home/simone/Documents/RAYPYNG/raypyng/test'
sim.simulation_name = sim_name

# turn off reflectivity
# sim.reflectivity(reflectivity=True)

# repeat the simulations as many time as needed
sim.repeat = rounds

sim.analyze = False # don't let RAY-UI analyze the results
sim.raypyng_analysis=True # let raypyng analyze the results

## This must be a list of dictionaries
sim.exports  =  [{beamline.SU:['RawRaysOutgoing']},
                 {beamline.DetectorAtFocus:['RawRaysOutgoing']}]


# create the rml files
#sim.rml_list()

#uncomment to run the simulations
sim.run(multiprocessing=1, force=False)
