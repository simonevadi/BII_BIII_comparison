import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from raypyng.postprocessing import PostProcessAnalyzed
p = PostProcessAnalyzed()

x = np.arange(1, 101, 1)
y = np.arange(10, 1001, 10)
window=10
x_averaged = p.moving_average(x, window)
y_averaged = p.moving_average(y, window)
print(x_averaged)
print(y_averaged)


undulator_table_filename = 'b3_ue42_5_ver_flux.csv'
undulator_df = pd.read_csv(undulator_table_filename)

# Read CSV-File
b3_file_path = os.path.join('RAYPy_Simulation_bessy3_56m_PGM_2Perc_coupling_errors_on_FLUX', 'DetectorAtFocus_RawRaysOutgoing.csv')
b3_df = pd.read_csv(b3_file_path)

fig, (ax) = plt.subplots(2, 1,figsize=(15,10))

for harm in [1,3,5]:
    
    ax[0].plot(undulator_df[f'Energy{harm}[eV]'], undulator_df[f'Photons{harm}'], label=f'Harmonic {harm}')
    
    min_h = undulator_df[f'Energy{harm}[eV]'].min()
    max_h = undulator_df[f'Energy{harm}[eV]'].max()
    b3_first_harm_df = b3_df[(b3_df['PhotonEnergy'] >= min_h) & (b3_df['PhotonEnergy'] <= max_h)]
    ax[1].plot(b3_first_harm_df['PhotonEnergy'], b3_first_harm_df[f'PhotonFlux{harm}'], label=f'Harmonic {harm}')

ax[0].legend(fontsize=16, loc='best')
ax[1].legend(fontsize=16, loc='best')
plt.tight_layout()
# plt.savefig('plot/Photon Density B2_B3 errors_on at 24 mu.png')
# plt.savefig('plot/Photon Density B2_B3 errors_on at 24 mu.pdf')
plt.show()