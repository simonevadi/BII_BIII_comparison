import matplotlib.pyplot as plt
import pandas as pd


# Read CSV-File

simdata_B2hi_37m = pd.read_csv('RAYPy_Simulation_bessy2hi_37m_PGM_2Perc_coupling_errors_on_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')
simdata_B2hi_56m = pd.read_csv('RAYPy_Simulation_bessy2hi_56m_PGM_2Perc_coupling_errors_on_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')
simdata_B3_37m = pd.read_csv('RAYPy_Simulation_bessy3_56m_PGM_2Perc_coupling_errors_on_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')
simdata_B3_56m = pd.read_csv('RAYPy_Simulation_bessy3_56m_PGM_2Perc_coupling_errors_on_FLUX/DetectorAtFocus_RawRaysOutgoing.csv')


fig, (ax) = plt.subplots(1, 1,figsize=(15,10))


reduced_simdata_B2hi_37m = simdata_B2hi_37m
energy_B2hi_37m = reduced_simdata_B2hi_37m['SU.photonEnergy']
N_rays_B2hi_37m = reduced_simdata_B2hi_37m['PercentageRaysSurvived']
    
reduced_simdata_B2hi_56m = simdata_B2hi_56m
energy_B2hi_56m = reduced_simdata_B2hi_56m['SU.photonEnergy']
N_rays_B2hi_56m = reduced_simdata_B2hi_56m['PercentageRaysSurvived']
   
reduced_simdata_B3_37m = simdata_B3_37m
energy_B3_37m = reduced_simdata_B3_37m['SU.photonEnergy']
N_rays_B3_37m = reduced_simdata_B3_37m['PercentageRaysSurvived']

reduced_simdata_B3_56m = simdata_B3_56m
energy_B3_56m = reduced_simdata_B3_56m['SU.photonEnergy']
N_rays_B3_56m = reduced_simdata_B3_56m['PercentageRaysSurvived']
    
# Density Plot
lines, = ax.plot(energy_B2hi_37m, N_rays_B2hi_37m, label = 'BII (high beta) 37m @ 30 µm ES', linestyle='dashed')
# used_colors = lines.get_color()
ax.plot(energy_B2hi_56m, N_rays_B2hi_56m, label = 'BII (high beta) 56m @ 61 µm ES', linestyle='dashed')
ax.plot(energy_B3_37m, N_rays_B3_37m, label ='BIII 37m @ 35 µm ES', marker='o')
ax.plot(energy_B3_56m, N_rays_B3_56m, label = 'BIII 56m @ 62 µm ES', marker='.')


ax.minorticks_on()
ax.grid(linestyle='dotted', color='grey')
ax.tick_params(axis='both', labelsize=14)
ax.set_ylabel ('Transmission [%]', fontsize=14)
# ax.set_ylabel(r'$\frac{N}{\mathrm{[µm^2]}} \, @ \, 0.1\% \, \mathrm{bandwidth}$' + ' in [%]', fontsize=16)
ax.set_xlabel('Energy [eV]', fontsize= 16)
ax.set_title('BESSY II (high beta) vs. BESSY III (37 m and 56 m PGM-BL) @ 'r'$\frac{\Delta E}{E}= 10000$', fontsize= 18)
# ax.set_title('BESSY III @ 56 m standard PGM-BL bandwidth normalized transmission', fontsize= 18)
ax.legend(fontsize=16, loc='best')
plt.tight_layout()
# plt.savefig('plot/Transmission B2_B3.png')
plt.show()
