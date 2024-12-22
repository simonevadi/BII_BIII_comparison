import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


# import simulation parameters
from parameter import energy_rp, energy_flux
from parameter import SlitSize
from parameter import rml_file_name_bessy2_56m
from parameter import rml_file_name_bessy3_56m
from parameter import add_to_title
from parameter import colors, grating

from raypyng.postprocessing import PostProcessAnalyzed
p = PostProcessAnalyzed()
moving_average = p.moving_average

SlitSize = SlitSize*1000
rml_comparison_list = []
rml_comparison_list.append(rml_file_name_bessy2_56m)
rml_comparison_list.append(rml_file_name_bessy3_56m)

# set moving average window
window = 1

# prepare figures
fig, (axs) = plt.subplots(3, 2,figsize=(10,10))
fig.suptitle(f"BESSY II/III comparison @ 56 m standard PGM-BL")

# remove plot 0,1
axs[0, 1].axis('off')
# BEAMLINE TRANSMISSION
flux_ax = axs[0,0]
flux_ax.set_xlabel(r'Energy [eV]')
flux_ax.set_ylabel('Transmission [%]')
flux_ax.set_title('Available Flux [in transmitted bandwidth]')
# flux_ax.grid(which='both', axis='both')
flux_ax.minorticks_on()

# BANDWIDTH
bw_ax = axs[1,0]
bw_ax.set_xlabel('Energy [eV]')
bw_ax.set_ylabel('Transmitted Bandwidth [meV]')
bw_ax.set_title('Transmitted Bandwidth (tbw)')
# bw_ax.grid(which='both', axis='both')
bw_ax.minorticks_on()

# RESOLVING POWER
rp_ax = axs[1,1]
rp_ax.set_xlabel('Energy [eV]')
rp_ax.set_ylabel('RP [a.u.]')
rp_ax.set_title('Resolving Power')
# rp_ax.grid(which='both', axis='both')
rp_ax.minorticks_on()

# HORIZONTAL FOCUS
hf_ax = axs[2,0]
hf_ax.set_xlabel('Energy [eV]')
hf_ax.set_ylabel('Focus Size [um]')
hf_ax.set_title('Horizontal Focus')
hf_ax.minorticks_on()

# VERTICAL FOCUS
vf_ax = axs[2,1]
vf_ax.set_xlabel('Energy [eV]')
vf_ax.set_ylabel('Focus Size [um]')
vf_ax.set_title('Vertical Focus')    
vf_ax.minorticks_on()

color_index = -1
for rml_file_name in rml_comparison_list:
    color_index +=1
    # file/folder/ml index definition
    flux_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_FLUX'
    rp_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_RP'



    # loading the data B2
    oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
    flux = pd.read_csv(os.path.join(flux_simulation_folder, oe))
    rp = pd.read_csv(os.path.join(rp_simulation_folder, oe))
    energy_flux = flux.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy']]
    energy_rp = rp.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy']]
    energy_flux=energy_flux.to_numpy()
    energy_rp=energy_rp.to_numpy()

    # energy_flux = moving_average(energy_flux.to_numpy(), window)
    # energy_rp = moving_average(energy_rp.to_numpy(), window)

    # plotting Flux and RPrp
    # BEAMLINE TRANSMISSION
    flux_perc = flux['PercentageRaysSurvived'].to_numpy()
    # flux_perc = moving_average(flux_perc, window)
    flux_ax.plot(energy_flux,flux_perc, colors[color_index], label=f'{rml_file_name}' )


    # BANDWIDTH
    bw_plot = rp['Bandwidth'].to_numpy()
    # bw_plot = moving_average(bw_plot, window)
    bw_ax.plot(energy_rp,1000*bw_plot,colors[color_index])


    # RESOLVING POWER
    # plot and deal with bandwidth=0 case.

    rp_ax.plot(energy_rp, energy_rp[:,0] / bw_plot, colors[color_index])


    # HORIZONTAL FOCUS
    hor_foc = rp['HorizontalFocusFWHM']
    # hor_foc = moving_average(hor_foc.to_numpy(), window)
    hf_ax.plot(energy_rp,1000*hor_foc,colors[color_index])

    # VERTICAL FOCUS
    ver_foc = rp['VerticalFocusFWHM']
    # ver_foc = moving_average(ver_foc.to_numpy(), window)
    vf_ax.plot(energy_rp,1000*ver_foc,colors[color_index])



# flux_ax.legend()
handles, labels = flux_ax.get_legend_handles_labels()
axs[0, 1].legend(handles, labels, loc='center', fontsize=16)
plt.tight_layout()
plt.savefig(f'plot/Comparison{add_to_title}.pdf')

plt.show()