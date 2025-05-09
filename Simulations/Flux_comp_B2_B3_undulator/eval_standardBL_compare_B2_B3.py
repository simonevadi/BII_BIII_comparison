import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xrt.backends.raycing.materials as rm
 
from raypyng.postprocessing import PostProcessAnalyzed
from helper_lib import get_reflectivity
from parameter import SlitSize

##############################################################
# LOAD IN DATA

this_file_dir=os.path.dirname(os.path.realpath(__file__))

# Read Undulator CSV-File BESSY II LoBeta 
undulator_B2Lo_table_filename = os.path.join(this_file_dir, 'undulator_flux_curves','b2_LoBeta_UE46_2025_smalerz_300mA_flux.txt')
undulator_B2Lo_df = pd.read_csv(undulator_B2Lo_table_filename, delimiter='\t')

# Read Undulator CSV-File BESSY II HiBeta
undulator_B2Hi_table_filename = os.path.join(this_file_dir, 'undulator_flux_curves','b2_HiBeta_UE46_2025_smalerz_300mA_flux.txt')
undulator_B2Hi_df = pd.read_csv(undulator_B2Hi_table_filename, delimiter='\t')

# Read Undulator CSV-File BESSY III
undulator_B3_table_filename = os.path.join(this_file_dir, 'undulator_flux_curves','b3_ue42_5_ver_300mA_flux.csv')
undulator_B3_df = pd.read_csv(undulator_B3_table_filename)


# Read CSV-File of the Beamline Simulation
# BESSY II LoBeta
BL_B2Lo_file_path = os.path.join('RAYPy_Simulation_bessy2lo_37m_PGM_2Perc_coupl_err_on_1_5degree_1200l_V2_FLUX', 'DetectorAtFocus_RawRaysOutgoing.csv')
BL_B2Lo_df = pd.read_csv(BL_B2Lo_file_path)

# BESSY II HiBeta
BL_B2Hi_file_path = os.path.join('RAYPy_Simulation_bessy2hi_37m_PGM_2Perc_coupl_err_on_1_5_degree_1200l_FLUX', 'DetectorAtFocus_RawRaysOutgoing.csv')
BL_B2Hi_df = pd.read_csv(BL_B2Hi_file_path)

# BESSY III
BL_B3_file_path = os.path.join('RAYPy_Simulation_bessy3_56m_PGM_2Perc_coupl_err_on0_75deg_1200l_V3_FLUX', 'DetectorAtFocus_RawRaysOutgoing.csv')
BL_B3_df = pd.read_csv(BL_B3_file_path)


##############################################################
# PLOTTING AND ANALYSIS
# Create the Main figure
fig, (axs) = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle('Comparison BESSY II vs. III Standard-PGM Beamlines', size=16)
x_range = [50, 2150]

harms = [1,3,5] # The Harmonics from the ID. Typically 1,3,5, rather higher. Depends on the FluxSims of the ID.

# BEAMLINE FLUX CURVE
ax1 = axs[0]

# BESSY II LoBeta
for harm in harms:
    Emin_harm = undulator_B2Lo_df[f'Energy{harm}[eV]'].min()
    Emax_harm = undulator_B2Lo_df[f'Energy{harm}[eV]'].max()
    filtered_df = BL_B2Lo_df[(BL_B2Lo_df['PhotonEnergy'] >= Emin_harm) & (BL_B2Lo_df['PhotonEnergy'] <= Emax_harm)]
    ax1.plot(filtered_df['PhotonEnergy'], filtered_df[f'PhotonFlux{harm}'], label=f'Harm. {harm} - UE46 @ BESSY II LoBeta (37 m)')

# BESSY II HiBeta
for harm in harms:
    Emin_harm = undulator_B2Hi_df[f'Energy{harm}[eV]'].min()
    Emax_harm = undulator_B2Hi_df[f'Energy{harm}[eV]'].max()
    filtered_df = BL_B2Hi_df[(BL_B2Hi_df['PhotonEnergy'] >= Emin_harm) & (BL_B2Hi_df['PhotonEnergy'] <= Emax_harm)]
    ax1.plot(filtered_df['PhotonEnergy'], filtered_df[f'PhotonFlux{harm}'], label=f'Harm. {harm} - UE46 @ BESSY II HiBeta (56 m)')

# BESSY III
for harm in harms:
    Emin_harm = undulator_B3_df[f'Energy{harm}[eV]'].min()
    Emax_harm = undulator_B3_df[f'Energy{harm}[eV]'].max()
    filtered_df = BL_B3_df[(BL_B3_df['PhotonEnergy'] >= Emin_harm) & (BL_B3_df['PhotonEnergy'] <= Emax_harm)]
    ax1.plot(filtered_df['PhotonEnergy'], filtered_df[f'PhotonFlux{harm}'], label=f'Harm. {harm} - UE42 @ BESSY III (56 m)')


ax1.set_title('Flux curves')
ax1.set_xlabel('Energy [eV]')
ax1.set_ylabel('Photon flux [ph/s/300 mA/0.1 % BW]')
# ax1.set_yscale('log')
ax1.legend(loc='best', fontsize=8)
ax1.set_xlim(x_range)
ax1.minorticks_on()
ax1.grid(which='major', axis='x', linestyle='--', linewidth=0.5, color='lightgrey')


# Flux Density
ax2 = axs[1]

# BESSY II LoBeta
for harm in harms:
    Emin_harm = undulator_B2Lo_df[f'Energy{harm}[eV]'].min()
    Emax_harm = undulator_B2Lo_df[f'Energy{harm}[eV]'].max()
    filtered_df = BL_B2Lo_df[(BL_B2Lo_df['PhotonEnergy'] >= Emin_harm) & (BL_B2Lo_df['PhotonEnergy'] <= Emax_harm)]
    foc_area = (filtered_df['VerticalFocusFWHM']*filtered_df['HorizontalFocusFWHM'])*1000  # in µm²
    ax2.plot(filtered_df['PhotonEnergy'],filtered_df[f'PhotonFlux{harm}']/foc_area, label=f'Harm. {harm} - UE46 @ BESSY II LoBeta (37 m)')


# BESSY II HiBeta
for harm in harms:
    Emin_harm = undulator_B2Hi_df[f'Energy{harm}[eV]'].min()
    Emax_harm = undulator_B2Hi_df[f'Energy{harm}[eV]'].max()
    filtered_df = BL_B2Hi_df[(BL_B2Hi_df['PhotonEnergy'] >= Emin_harm) & (BL_B2Hi_df['PhotonEnergy'] <= Emax_harm)]
    foc_area = (filtered_df['VerticalFocusFWHM']*filtered_df['HorizontalFocusFWHM'])*1000  # in µm²
    ax2.plot(filtered_df['PhotonEnergy'],filtered_df[f'PhotonFlux{harm}']/foc_area, label=f'Harm. {harm} - UE46 @ BESSY II HiBeta (56 m)')

# BESSY III
for harm in harms:
    Emin_harm = undulator_B3_df[f'Energy{harm}[eV]'].min()
    Emax_harm = undulator_B3_df[f'Energy{harm}[eV]'].max()
    filtered_df = BL_B3_df[(BL_B3_df['PhotonEnergy'] >= Emin_harm) & (BL_B3_df['PhotonEnergy'] <= Emax_harm)]
    foc_area = (filtered_df['VerticalFocusFWHM']*filtered_df['HorizontalFocusFWHM'])*1000  # in µm²
    ax2.plot(filtered_df['PhotonEnergy'],filtered_df[f'PhotonFlux{harm}']/foc_area, label=f'Harm. {harm} - UE42 @ BESSY III (56 m)')


ax2.set_title('Flux Density')
ax2.set_xlabel('Energy [eV]')
ax2.set_ylabel('Photons flux per µm²')
# ax2.set_yscale('log')
ax2.legend(loc='best', fontsize=8)
ax2.set_xlim(x_range)
ax2.minorticks_on()
ax2.grid(which='major', axis='x', linestyle='--', linewidth=0.5, color='lightgrey')

##############################################################
# SAVING
# Ensure the "plot" folder exists
plot_folder = 'plot'
if not os.path.exists(plot_folder):
    os.makedirs(plot_folder)

# Save the the figure
plt.tight_layout()
# plt.savefig('plot/Photon Density B2_B3 errors_on at 24 mu.png')
# plt.savefig('plot/CDR-Plots/Comparison BESSY II vs III_err_on_LogScale.pdf')
plt.tight_layout()
plt.show()
