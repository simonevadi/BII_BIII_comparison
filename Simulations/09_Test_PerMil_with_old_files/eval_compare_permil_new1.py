import os
import matplotlib.pyplot as plt
import pandas as pd


# import simulation parameters

from parameter import SlitSize
from parameter import rml_file_name_bessy3_long_52 as rml_file_name_b2
from parameter import rml_file_name_bessy2_LoBeta_long_52 as rml_file_name_b3

SlitSize = SlitSize*1000
rml_comparison_list = {}
rml_comparison_list[rml_file_name_b2]  = 1
rml_comparison_list[rml_file_name_b3]  = 1


# file/folder/ml index definition
flux_simulation_folder_b2 = 'RAYPy_Simulation_'+rml_file_name_b2+'_FLUX'
flux_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_FLUX'


# loading the data B2
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b2 = pd.read_csv(os.path.join(flux_simulation_folder_b2, oe))

# loading the data B3
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b3 = pd.read_csv(os.path.join(flux_simulation_folder_b3, oe))

# Bandwidth normalized Transmission
fig, (ax) = plt.subplots(1, 1,figsize=(15,10))

for ind, es_size in enumerate(SlitSize):
    
    # BESSY 2:
    filtered_flux_b2 = flux_b2[flux_b2['ExitSlit.openingHeight'] == es_size]
    energy_b2 = filtered_flux_b2['SU.photonEnergy']  
    permilflux_b2 = flux_b2['FluxPerMilPerBwPerc']    
    
    
    # BESSY 3:
    filtered_flux_b3 = flux_b3[flux_b3['ExitSlit.openingHeight'] == es_size]
    energy_b3 = filtered_flux_b3['SU.photonEnergy']
    permilflux_b3 = flux_b3['FluxPerMilPerBwPerc']

    # Plot: 
    
    ax.plot(energy_b2, permilflux_b2, color ='blue', marker='o', label = 'BESSY II')
    ax.plot(energy_b3, permilflux_b3, color ='green', marker='o', label = 'BESSY III')
    
    ax.legend(fontsize=16)
    ax.minorticks_on()
    ax.tick_params(axis='both', labelsize=14)
    ax.grid(linestyle='dotted')
    ax.set_title('Comparison BESSY II vs. BESSY III @ ' + str(int(es_size * 1000)) + ' µm', fontsize=18)
    ax.set_xlabel('Energy [eV]', fontsize=16)
    ax.set_ylabel('Bandwidth normalized Transmission (BNT) [%]', fontsize=16)
    ax.set_ylim()
    ax.set_xlim(0,2250)

plt.tight_layout()
# plt.savefig('plot/Comparision BESSY II vs BESSY III with standard PGM BL @' + str(int(es_size * 1000)) + ' µm ExitSlit.png')
# plt.savefig('plot/Comparision BESSY II vs BESSY III with standard PGM BL @' + str(int(es_size * 1000)) + ' µm ExitSlit.pdf')
plt.savefig('plot/Comparision BESSY II vs BESSY III with standard PGM BL @ dif µm ExitSlit.png')

# plt.show()