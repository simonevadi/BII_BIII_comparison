import os
import matplotlib.pyplot as plt
import pandas as pd


# import simulation parameters

from parameter import rml_file_name_bessy3_long_56 as rml_file_name_b3
from parameter import rml_file_name_bessy2_LoBeta_long_56 as rml_file_name_b2lo
from parameter import rml_file_name_bessy2_HiBeta_long_56 as rml_file_name_b2hi


# file/folder/ml index definition
flux_simulation_folder_b2lo = 'RAYPy_Simulation_'+rml_file_name_b2lo+'_FLUX'
flux_simulation_folder_b2hi = 'RAYPy_Simulation_'+rml_file_name_b2hi+'_FLUX'
flux_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_FLUX'
rp_simulation_folder_b2lo = 'RAYPy_Simulation_'+rml_file_name_b2lo+'_RP'
rp_simulation_folder_b2hi = 'RAYPy_Simulation_'+rml_file_name_b2hi+'_RP'
rp_simulation_folder_b3 = 'RAYPy_Simulation_'+rml_file_name_b3+'_RP'


# loading the data B2lo
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b2lo = pd.read_csv(os.path.join(flux_simulation_folder_b2lo, oe))
rp_b2lo = pd.read_csv(os.path.join(rp_simulation_folder_b2lo, oe))

# loading the data B2hi
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b2hi = pd.read_csv(os.path.join(flux_simulation_folder_b2hi, oe))
rp_b2hi = pd.read_csv(os.path.join(rp_simulation_folder_b2hi, oe))

# loading the data B3
oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
flux_b3 = pd.read_csv(os.path.join(flux_simulation_folder_b3, oe))
rp_b3 = pd.read_csv(os.path.join(rp_simulation_folder_b3, oe))



# Bandwidth normalized Transmission
fig, (ax) = plt.subplots(3, 1,figsize=(15,10))

for energy in rp_b2lo['PhotonEnergy'].unique():
    
    # BESSY 2lo:
    filtered_rp_b2lo = rp_b2lo[rp_b2lo['PhotonEnergy'] == energy]
    es_size_b2lo = filtered_rp_b2lo['ExitSlit.openingHeight']  
    energy_b2lo = filtered_rp_b2lo['PhotonEnergy']  
    bandwidth_b2lo = filtered_rp_b2lo['Bandwidth']  

    # BESSY 2hi:
    filtered_rp_b2hi = rp_b2hi[rp_b2hi['PhotonEnergy'] == energy]
    es_size_b2hi = filtered_rp_b2hi['ExitSlit.openingHeight']  
    energy_b2hi = filtered_rp_b2hi['PhotonEnergy']  
    bandwidth_b2hi = filtered_rp_b2hi['Bandwidth']  
    
    # # BESSY 3:
    filtered_rp_b3 = rp_b3[rp_b3['PhotonEnergy'] == energy]
    es_size_b3 = filtered_rp_b3['ExitSlit.openingHeight']  
    energy_b3 = filtered_rp_b3['PhotonEnergy']  
    bandwidth_b3 = filtered_rp_b3['Bandwidth']  

    # Plot: 
    
    ax[0].plot(es_size_b2lo, energy_b2lo/bandwidth_b2lo, marker='o', label = f'{energy} eV')
    ax[1].plot(es_size_b2hi, energy_b2hi/bandwidth_b2hi, marker='o', label = f'{energy} eV')
    ax[2].plot(es_size_b3, energy_b3/bandwidth_b3, marker='o', label = f'{energy} eV')
    
# ax.legend(fontsize=16)
ax[0].minorticks_on()
ax[0].tick_params(axis='both', labelsize=14)
ax[0].grid(linestyle='dotted')
ax[0].set_xlabel('ExitSlit [µm]', fontsize=16)
ax[0].set_ylabel('Resolving Power', fontsize=16)
ax[0].set_title('BESSY II LowBeta')
ax[0].legend()

ax[1].minorticks_on()
ax[1].tick_params(axis='both', labelsize=14)
ax[1].grid(linestyle='dotted')
ax[1].set_xlabel('ExitSlit [µm]', fontsize=16)
ax[1].set_ylabel('Resolving Power', fontsize=16)
ax[1].set_title('BESSY II LowBeta')
ax[1].legend()

ax[2].minorticks_on()
ax[2].tick_params(axis='both', labelsize=14)
ax[2].grid(linestyle='dotted')
ax[2].set_xlabel('ExitSlit [µm]', fontsize=16)
ax[2].set_ylabel('Resolving Power', fontsize=16)
ax[2].set_title('BESSY III')
ax[2].legend()

plt.suptitle('ResolvingPower BESSY II vs. BESSY III @ Standard 56 m PGM BL', fontsize=18)
plt.tight_layout()
# plt.savefig('plot/SlitLimit BESSY II vs BESSY III with standard PGM BL @ dif µm ExitSlit.png')
plt.show()