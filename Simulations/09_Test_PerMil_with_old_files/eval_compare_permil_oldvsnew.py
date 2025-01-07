import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


# import simulation parameters
from parameter import energy_rp, energy_flux
from parameter import SlitSize
from parameter import rml_file_name_bessy3_long_52
from parameter import rml_file_name_bessy2_LoBeta_long_52

from parameter import rml_file_name_bessy3_long_52 as rml_file_name_b3
from parameter import rml_file_name_bessy2_LoBeta_long_52 as rml_file_name_b2

from parameter import colors, grating



# file/folder/ml index definition
flux_simulation_folder_b2 = 'RAYPy_Simulation_'+rml_file_name_b2+'_FLUX'
rp_simulation_folder_b2 = 'RAYPy_Simulation_'+rml_file_name_b2+'_RP'
flux_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_FLUX'
rp_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_RP'


# loading the data B2
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b2 = pd.read_csv(os.path.join(flux_simulation_folder_b2, oe))
rp_b2 = pd.read_csv(os.path.join(rp_simulation_folder_b2, oe))
source_flux_b2 = flux_b2.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]

# loading the data B3
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b3 = pd.read_csv(os.path.join(flux_simulation_folder_b3, oe))
rp_b3 = pd.read_csv(os.path.join(rp_simulation_folder_b3, oe))
source_flux_b3 = flux_b3.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]


from raypyng.postprocessing import PostProcessAnalyzed
p = PostProcessAnalyzed()
moving_average = p.moving_average

SlitSize = SlitSize*1000
rml_comparison_list = []
rml_comparison_list.append(rml_file_name_bessy3_long_52)  
rml_comparison_list.append(rml_file_name_bessy2_LoBeta_long_52)


# set moving average window
window = 1

# prepare figures
fig, (axs) = plt.subplots(1, 2,figsize=(15,10))
fig.suptitle(f"BESSYII/III PGM standard beamline comparison")



# PerMil TRANSMISSION
hf_ax = axs[0]
hf_ax.set_xlabel('Energy/1000 [eV]')
hf_ax.set_ylabel('E/1000/bandwidth')
hf_ax.set_title('OLD PerMil transmission')
#hf_ax.set_ylim(13, 51.5)

# OLD Transmission/PerMil bandwidth
vf_ax = axs[1]
vf_ax.set_xlabel('Energy [eV]')
vf_ax.set_ylabel('Transmission/PerMil bandwidth [%]')
vf_ax.set_title('OLD Transmission/bandwidth')    


color_index = -1
for rml_file_name in rml_comparison_list:
    ind=0
    color_index +=1
    # file/folder/ml index definition
    flux_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_FLUX'
    rp_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_RP'



    # load Flux simulations results
    folder_name  = flux_simulation_folder
    oe           = 'DetectorAtFocus'
    flux_path    = os.path.join(flux_simulation_folder, oe+'_RawRaysOutgoing.dat')
    flux         = pd.read_csv(flux_path, sep='\t', index_col=None)
    en_flux_path = os.path.join(flux_simulation_folder, 'input_param_SU_photonEnergy.dat')
    energy_flux  = np.loadtxt(en_flux_path)
    ssf          = energy_flux.shape[0]

    # load RP simulations results
    folder_name  = rp_simulation_folder
    oe           = 'DetectorAtFocus'
    rp_path      = os.path.join(rp_simulation_folder, oe+'_RawRaysOutgoing.dat')
    rp           = pd.read_csv(rp_path, sep='\t', index_col=None)
    en_rp_path   = os.path.join(rp_simulation_folder, 'input_param_SU_photonEnergy.dat')
    energy_rp    = np.loadtxt(en_rp_path)
    ssrp         = energy_rp.shape[0]

    energy_flux = moving_average(energy_flux, window)
    energy_rp = moving_average(energy_rp, window)


    # PER MIL BANDWIDTH
    bw_plot = rp['Bandwidth'][ssrp*ind:ssrp*(ind+1)]
    bw_plot = moving_average(bw_plot, window)
    hf_ax.plot(energy_rp/1000,(energy_rp/1000)/bw_plot,colors[color_index])
    hf_ax.minorticks_on()


    # PER MIL TRANSMISSION (FLUX) COMPARISON
    flux_plot = flux['PercentageRaysSurvived'][ssf*ind:ssf*(ind+1)]
    flux_plot = moving_average(flux_plot.to_numpy(), window)
    bw_plot = rp['Bandwidth'][ssrp*ind:ssrp*(ind+1)]
    bw_plot = moving_average(bw_plot, window)
    vf_ax.plot(energy_rp,energy_rp/1000/bw_plot*flux_plot,colors[color_index], label=rml_file_name)
    vf_ax.minorticks_on()




# import simulation parameters
from parameter import SlitSize
from parameter import rml_file_name_bessy3_long_52 as rml_file_name_b3
from parameter import rml_file_name_bessy2_LoBeta_long_52 as rml_file_name_b2


# # file/folder/ml index definition
# flux_simulation_folder_b2 = 'RAYPy_Simulation_'+rml_file_name_b2+'_FLUX'
# rp_simulation_folder_b2 = 'RAYPy_Simulation_'+rml_file_name_b2+'_RP'
# flux_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_FLUX'
# rp_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_RP'


varying_var = SlitSize
varying_var_n = 'Exit Slit'
varying_var_unit = 'um'

# loading the data B2
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b2 = pd.read_csv(os.path.join(flux_simulation_folder_b2, oe))
rp_b2 = pd.read_csv(os.path.join(rp_simulation_folder_b2, oe))
source_flux_b2 = flux_b2.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]

# loading the data B3
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b3 = pd.read_csv(os.path.join(flux_simulation_folder_b3, oe))
rp_b3 = pd.read_csv(os.path.join(rp_simulation_folder_b3, oe))
source_flux_b3 = flux_b3.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]



# NEW PERMIL BANDWIDTH
ax = axs[0]
for ind, es_size in enumerate(SlitSize):
     filtered_rp_b2 = rp_b2[rp_b2['ExitSlit.openingHeight'] == es_size]
     energy = filtered_rp_b2['SU.photonEnergy']
     bw_b2 = filtered_rp_b2['Bandwidth']
     ax.scatter(energy/1000,energy/(1000*bw_b2), label='bessy2 (new)')

     filtered_rp_b3 = rp_b3[rp_b3['ExitSlit.openingHeight'] == es_size]
     energy = filtered_rp_b3['SU.photonEnergy']
     bw_b3= filtered_rp_b3['Bandwidth']
     ax.scatter(energy/1000,energy/(1000*bw_b3), label='bessy3 (new)')
     

ax.set_xlabel('Energy [keV]')
ax.set_ylabel('Energy/1000/bandwidth [a.u.]')
ax.set_title('NEW PerMil Transmission')
ax.minorticks_on()
ax.legend()

# fig, (axs_new) = plt.subplots(1, 1,figsize=(15,10))

# NEW PERMIL FLUX 
ax = axs[1]
for ind, es_size in enumerate(SlitSize):
     filtered_flux_b2 = flux_b2[flux_b2['ExitSlit.openingHeight'] == es_size]
     energy_b2 = filtered_flux_b2['SU.photonEnergy']
     abs_flux_b2 = filtered_flux_b2['PercentageRaysSurvived']
     filtered_rp = rp_b2[rp_b2['ExitSlit.openingHeight'] == es_size]
     bw_b2 = filtered_rp_b2['Bandwidth']
     ax.scatter(energy_b2,(energy_b2/1000/bw_b2)*abs_flux_b2, label='bessy2 (new)')

     filtered_flux_b3 = flux_b3[flux_b3['ExitSlit.openingHeight'] == es_size]
     energy_b3 = filtered_flux_b3['SU.photonEnergy']
     abs_flux_b3 = filtered_flux_b3['PercentageRaysSurvived']
     filtered_rp = rp_b3[rp_b3['ExitSlit.openingHeight'] == es_size]
     bw_b3 = filtered_rp_b3['Bandwidth']
     ax.scatter(energy_b3,(energy_b3/1000/bw_b3)*abs_flux_b3, label='bessy3 (new)')
    #  axs_new.plot(energy_b3,bw_b3, label='bessy3 (new)')
     

ax.set_xlabel(r'Energy [eV]')
ax.set_ylabel('Flux [ph/s/tbw]')
ax.set_title('NEW Transmission / Per MIl bandwidth')
ax.minorticks_on()
ax.legend()

plt.tight_layout()
plt.savefig('plot/FluxRpFocus_comparison_permil_old.png')



# plt.show()