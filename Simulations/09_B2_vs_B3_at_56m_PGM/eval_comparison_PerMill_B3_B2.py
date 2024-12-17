import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# path to xrt:
import os, sys; sys.path.append(os.path.join('..', '..', '..'))  # analysis:ignore
import xrt.backends.raycing.materials as rm

# raypyng 
from raypyng.postprocessing import PostProcessAnalyzed

# from helper library
from helper_lib import get_reflectivity
from helper_lib import scale_undulator_flux, order

# import simulation parameters
from parameter import energy_rp, energy_flux
from parameter import SlitSize
from parameter import rml_file_name_bessy3_56m as rml_file_name
from parameter import colors, grating


# file/folder/ml index definition
flux_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_FLUX'
rp_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_RP'



varying_var = SlitSize
varying_var_n = 'Exit Slit'
varying_var_unit = 'um'

# loading the data
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux = pd.read_csv(os.path.join(flux_simulation_folder, oe))
rp = pd.read_csv(os.path.join(rp_simulation_folder, oe))
source_flux = flux.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]
print(flux.columns)





# PERMIL BANDWIDTH
ax = axs[0]
for ind, es_size in enumerate(SlitSize):
     filtered_rp = rp[rp['ExitSlit.openingHeight'] == es_size]
     energy = filtered_rp['SU.photonEnergy']
     bw = filtered_rp['Bandwidth']
     ax.plot(energy/1000,energy/(1000*bw) )
 
ax.set_xlabel('Energy [keV]')
ax.set_ylabel('Energy/1000/bandwidth [a.u.]')
ax.set_title('PerMil Transmission')
ax.minorticks_on()
# ax.grid(which='both', axis='both')

 
# PERMIL FLUX 
ax = axs[1]
for ind, es_size in enumerate(SlitSize):
     filtered_flux = flux[flux['ExitSlit.openingHeight'] == es_size]
     energy = filtered_flux['SU.photonEnergy']
     abs_flux = filtered_flux['PercentageRaysSurvived']
     filtered_rp = rp[rp['ExitSlit.openingHeight'] == es_size]
     bw = filtered_rp['Bandwidth']
     ax.plot(energy,(energy/1000/bw)*abs_flux)
 
ax.set_xlabel(r'Energy [eV]')
ax.set_ylabel('Flux [ph/s/tbw]')
ax.set_title('Transmission / Per MIl bandwidth')
ax.minorticks_on()
# ax.grid(which='both', axis='both')
 
plt.suptitle('PGM-Undulator (SU), 1200 l/mm unknown grating')
plt.tight_layout()
plt.savefig('plot/Per Mill BESSY III with 56m PGM standard BL.pdf')