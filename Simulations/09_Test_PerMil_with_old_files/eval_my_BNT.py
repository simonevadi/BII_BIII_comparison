import matplotlib.pyplot as plt
import pandas as pd


# Read CSV-File

simdata_B2 = pd.read_csv('RAYPy_Simulation_bessy2_LoBeta_long_52_FLUX/DetectorAtFocus_RawRaysIncoming.csv')
simdata_B3= pd.read_csv('RAYPy_Simulation_bessy3_long_52_FLUX/DetectorAtFocus_RawRaysIncoming.csv')

fig, (ax) = plt.subplots(1, 1,figsize=(15,10))


ExitSlit_list = simdata_B2['ExitSlit.openingHeight'].unique()
for ExitSlit in ExitSlit_list:
    reduced_simdata_B2 = simdata_B2[simdata_B2['ExitSlit.openingHeight']==ExitSlit]
    bnt_B2 = reduced_simdata_B2['FluxPerMilPerBwPerc']
    energy_B2 = reduced_simdata_B2['SU.photonEnergy']

    reduced_simdata_B3 = simdata_B3[simdata_B3['ExitSlit.openingHeight']==ExitSlit]
    bnt_B3 = reduced_simdata_B3['FluxPerMilPerBwPerc']
    energy_B3 = reduced_simdata_B3['SU.photonEnergy']
    
    # ax.plot(energy_B2, bnt_B2/10, label=f'B2 ExitSlit {ExitSlit}')
    ax.plot(energy_B3, bnt_B3/10, label=f'ExitSlit {int(ExitSlit*1000)}'+' µm', marker='o')

ax.minorticks_on()
ax.grid(linestyle='dotted', color='grey')
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel(r'$\frac{I_1}{I_0} \cdot \frac{\Delta E_0}{\Delta E_1}$', fontsize= 16)
ax.set_xlabel('Energy [eV]', fontsize= 16)
# ax.set_title('BESSY II (LowBeta) vs. BESSY III @ 56 m standard PGM-BL bandwidth normalized transmission', fontsize= 18)
ax.set_title('BESSY III @ 56 m standard PGM-BL bandwidth normalized transmission', fontsize= 18)
ax.legend(fontsize=16, loc='best')
plt.tight_layout()
plt.show()




# simdata_dict = {'II':os.path.join('RAYPy_Simulation_bessy2_LoBeta_long_52_FLUX',
#                                'DetectorAtFocus_RawRaysIncoming.csv'), 
#                 'III':os.path.join('RAYPy_Simulation_bessy3_long_52_FLUX',
#                                'DetectorAtFocus_RawRaysIncoming.csv')
#                 }

# fig, (ax) = plt.subplots(1, 1,figsize=(15,10))

# for b_label, path_to_sim_folder in simdata_dict.items():
#     simdata = pd.read_csv(path_to_sim_folder)
#     ExitSlit_list = simdata['ExitSlit.openingHeight'].unique()
    
#     for ExitSlit in ExitSlit_list:
#         reduced_simdata = simdata[simdata['ExitSlit.openingHeight']==ExitSlit]
#         bandwidth = reduced_simdata['Bandwidth']
#         energy = reduced_simdata['SU.photonEnergy']
        
#         ax.plot(energy, bandwidth*1000, label=f'BESSY {b_label} ExitSlit {int(ExitSlit*1000)} µm')

# ax.legend()
# ax.set_ylabel('Bandwidth [meV]')
# ax.set_xlabel('Energy [eV]')
# ax.set_title('B2/B3')
# plt.show()












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