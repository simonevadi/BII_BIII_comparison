import os
import matplotlib.pyplot as plt
import pandas as pd


simdata_dict = {2:os.path.join('RAYPy_Simulation_bessy2lo_56m_PGM_2Perc_coupling_errors_on_FLUX',
                               'DetectorAtFocus_RawRaysIncoming.csv'), 
                3:os.path.join('RAYPy_Simulation_bessy3_56m_PGM_2Perc_coupling_errors_on_FLUX',
                               'DetectorAtFocus_RawRaysIncoming.csv')
                }

fig, (ax) = plt.subplots(1, 1,figsize=(15,10))

for b_label, path_to_sim_folder in simdata_dict.items():
    simdata = pd.read_csv(path_to_sim_folder)
    ExitSlit_list = simdata['ExitSlit.openingHeight'].unique()
    for ExitSlit in ExitSlit_list:
        reduced_simdata = simdata[simdata['ExitSlit.openingHeight']==ExitSlit]
        bandwidth = reduced_simdata['Bandwidth']
        energy = reduced_simdata['SU.photonEnergy']
        
        ax.plot(energy, bandwidth*1000, label=f'B{b_label} ExitSlit {int(ExitSlit*1000)} µm')

ax.legend()
ax.set_ylabel('Bandwidth [meV]')
ax.set_xlabel('Energy [eV]')
ax.set_title('B2/B3')
plt.show()


# Read CSV-File

# simdata_B2 = pd.read_csv('RAYPy_Simulation_bessy2_LoBeta_long_52_FLUX/DetectorAtFocus_RawRaysIncoming.csv')
# simdata_B3= pd.read_csv('RAYPy_Simulation_bessy3_long_52_FLUX/DetectorAtFocus_RawRaysIncoming.csv')

# fig, (ax) = plt.subplots(1, 1,figsize=(15,10))


# ExitSlit_list = simdata_B2['ExitSlit.openingHeight'].unique()
# for ExitSlit in ExitSlit_list:
#     reduced_simdata_B2 = simdata_B2[simdata_B2['ExitSlit.openingHeight']==ExitSlit]
#     bandwidth_B2 = reduced_simdata_B2['Bandwidth']
#     energy_B2 = reduced_simdata_B2['SU.photonEnergy']

#     reduced_simdata_B3 = simdata_B3[simdata_B3['ExitSlit.openingHeight']==ExitSlit]
#     bandwidth_B3 = reduced_simdata_B3['Bandwidth']
#     energy_B3 = reduced_simdata_B3['SU.photonEnergy']
    
#     ax.plot(energy_B2, bandwidth_B2*1000, label=f'B2 ExitSlit {ExitSlit}')
#     ax.plot(energy_B3, bandwidth_B3*1000, label=f'B3 ExitSlit {ExitSlit}')


# ax.legend()
# ax.set_ylabel('Bandwidth [meV]')
# ax.set_xlabel('Energy [eV]')
# ax.set_title('B3')