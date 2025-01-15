import matplotlib.pyplot as plt
import pandas as pd


# Read CSV-File

simdata_B2lo = pd.read_csv('RAYPy_Simulation_bessy2_LoBeta_long_52_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')
simdata_B2hi = pd.read_csv('RAYPy_Simulation_bessy2_HiBeta_long_52_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')
simdata_B3= pd.read_csv('RAYPy_Simulation_bessy3_long_52_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')

fig, (ax) = plt.subplots(1, 1,figsize=(15,10))


ExitSlit_list = simdata_B2lo['ExitSlit.openingHeight'].unique()
for ExitSlit in ExitSlit_list:
    reduced_simdata_B2lo = simdata_B2lo[simdata_B2lo['ExitSlit.openingHeight']==ExitSlit]
    energy_B2lo = reduced_simdata_B2lo['SU.photonEnergy']
    N_rays_B2lo = reduced_simdata_B2lo['PercentageRaysSurvived']
    
    reduced_simdata_B2hi = simdata_B2hi[simdata_B2hi['ExitSlit.openingHeight']==ExitSlit]
    energy_B2hi = reduced_simdata_B2hi['SU.photonEnergy']
    N_rays_B2hi = reduced_simdata_B2hi['PercentageRaysSurvived']
   
    reduced_simdata_B3 = simdata_B3[simdata_B3['ExitSlit.openingHeight']==ExitSlit]
    energy_B3 = reduced_simdata_B3['SU.photonEnergy']
    N_rays_B3 = reduced_simdata_B3['PercentageRaysSurvived']
    
    # Density Plot
    lines, = ax.plot(energy_B2lo, N_rays_B2lo, label = f'B2 low beta ExitSlit {int(ExitSlit*1000)}'+' µm', marker='s')
    used_colors = lines.get_color()
    ax.plot(energy_B2hi, N_rays_B2hi, color = used_colors, label = f'B2 high beta ExitSlit {int(ExitSlit*1000)}'+' µm', marker='+')
    ax.plot(energy_B3, N_rays_B3, color = used_colors, label = f'B3 ExitSlit {int(ExitSlit*1000)}'+' µm', marker='o')


ax.minorticks_on()
ax.grid(linestyle='dotted', color='grey')
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel ('Transmission [%]', fontsize=14)
# ax.set_ylabel(r'$\frac{N}{\mathrm{[µm^2]}} \, @ \, 0.1\% \, \mathrm{bandwidth}$' + ' in [%]', fontsize=16)
ax.set_xlabel('Energy [eV]', fontsize= 16)
ax.set_title('BESSY II (LowBeta) vs. BESSY III @ 56 m standard PGM-BL PhotonDensity', fontsize= 18)
# ax.set_title('BESSY III @ 56 m standard PGM-BL bandwidth normalized transmission', fontsize= 18)
ax.legend(fontsize=16, loc='best')
plt.tight_layout()
# plt.savefig('plot/Transmission B2_B3.png')
plt.show()
