import matplotlib.pyplot as plt
import pandas as pd


# Read CSV-File

simdata_B2hi = pd.read_csv('RAYPy_Simulation_bessy2hi_56m_PGM_2Perc_coupling_errors_on_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')
simdata_B3= pd.read_csv('RAYPy_Simulation_bessy3_56m_PGM_2Perc_coupling_errors_on_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')

fig, (ax) = plt.subplots(1, 1,figsize=(15,10))


ExitSlit_list = simdata_B2hi['ExitSlit.openingHeight'].unique()
for ExitSlit in ExitSlit_list:
    if ExitSlit != 0.027:
        continue
    reduced_simdata_B2hi = simdata_B2hi[simdata_B2hi['ExitSlit.openingHeight']==ExitSlit]
    energy_B2hi = reduced_simdata_B2hi['SU.photonEnergy']
    N_rays_B2hi = reduced_simdata_B2hi['PercentageRaysSurvived']
    vf_B2hi = reduced_simdata_B2hi['VerticalFocusFWHM']
    hf_B2hi = reduced_simdata_B2hi['HorizontalFocusFWHM']
    PhotonDensity_B2hi = N_rays_B2hi/((vf_B2hi*hf_B2hi)*1000)

    reduced_simdata_B3 = simdata_B3[simdata_B3['ExitSlit.openingHeight']==ExitSlit]
    energy_B3 = reduced_simdata_B3['SU.photonEnergy']
    N_rays_B3 = reduced_simdata_B3['PercentageRaysSurvived']
    vf_B3 = reduced_simdata_B3['VerticalFocusFWHM']
    hf_B3 = reduced_simdata_B3['HorizontalFocusFWHM']
    PhotonDensity_B3 = N_rays_B3/((vf_B3*hf_B3)*1000)

    # Density Plot
    # lines, = ax.plot(energy_B2hi, PhotonDensity_B2hi,  label = f'B2 high beta ExitSlit {int(ExitSlit*1000)}'+' µm')
    # used_colors = lines.get_color()
    ax.plot(energy_B2hi, PhotonDensity_B2hi, label = f'B2 low beta ExitSlit {int(ExitSlit*1000)}'+' µm', marker='s', color='blue')

    ax.plot(energy_B3, PhotonDensity_B3, label = f'B3 ExitSlit {int(ExitSlit*1000)}'+' µm', marker='s', color='green')

ax.minorticks_on()
ax.grid(linestyle='dotted', color='grey')
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel ('Photon density [%/µm²]', fontsize=14)
# ax.set_ylabel(r'$\frac{N}{\mathrm{[µm^2]}} \, @ \, 0.1\% \, \mathrm{bandwidth}$' + ' in [%]', fontsize=16)
ax.set_xlabel('Energy [eV]', fontsize= 16)
ax.set_title('BESSY II (LowBeta) vs. BESSY III @ 56 m standard PGM-BL PhotonDensity', fontsize= 18)
# ax.set_title('BESSY III @ 56 m standard PGM-BL bandwidth normalized transmission', fontsize= 18)
ax.legend(fontsize=16, loc='best')
plt.tight_layout()
plt.savefig('plot/Photon Density B2_B3 at 27mu.png')
plt.savefig('plot/Photon Density B2_B3 at 27mu.pdf')
plt.show()
