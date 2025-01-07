import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


def permil():
    fig, (axs) = plt.subplots(2, 1,figsize=(10,10))

    for gr in grating:
        # loading the data B2
        oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
        flux_b2 = pd.read_csv(os.path.join(flux_simulation_folder_b2, oe))
        rp_b2 = pd.read_csv(os.path.join(rp_simulation_folder_b2, oe))
        source_flux_b2 = flux_b2.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]

        # loading the data B3
        oe = 'DetectorAtFocus' + '_RawRaysOutgoing.csv'
        flux_b3 = pd.read_csv(os.path.join(flux_simulation_folder_b3, oe))
        rp_b3 = pd.read_csv(os.path.join(rp_simulation_folder_b3, oe))
        source_flux_b3 = flux_b3.drop_duplicates(subset='SU.photonEnergy')[['SU.photonEnergy', 'SourcePhotonFlux']]

        flux_b2 = flux_b2[flux_b2['PG.lineDensity']==gr]
        rp_b2 = rp_b2[rp_b2['PG.lineDensity']==gr]
        flux_b3 = flux_b3[flux_b3['PG.lineDensity']==gr]
        rp_b3 = rp_b3[rp_b3['PG.lineDensity']==gr]

        # PERMIL BANDWIDTH
        ax = axs[0]
        energy = rp_b2['SU.photonEnergy']
        bw_b2 = rp_b2['Bandwidth']
        ax.plot(energy/1000,(energy/1000)/bw_b2, label=f'bessy2 {gr}')

        energy = rp_b3['SU.photonEnergy']
        bw_b3 = rp_b3['Bandwidth']
        ax.plot(energy/1000,(energy/1000)/bw_b3, label=f'bessy3 {gr}')

        ax.set_xlabel('Energy [keV]')
        ax.set_ylabel('Energy/1000/bandwidth [a.u.]')
        ax.set_title('PerMil Transmission')
        ax.minorticks_on()
        # ax.grid(which='both', axis='both')
        ax.legend()

        
        # PERMIL FLUX 
        ax = axs[1]
        energy = flux_b2['SU.photonEnergy']
        abs_flux_b2 = flux_b2['PercentageRaysSurvived']
        bw_b2 = rp_b2['Bandwidth']
        ax.plot(energy,energy/1000/bw_b2*abs_flux_b2, label=f'bessy2 {gr}')

        energy = flux_b3['SU.photonEnergy']
        abs_flux_b3 = flux_b3['PercentageRaysSurvived']
        bw_b3 = rp_b3['Bandwidth']
        ax.plot(energy,energy/1000/bw_b3*abs_flux_b3, label=f'bessy3 {gr}')

        ax.set_xlabel(r'Energy [eV]')
        ax.set_ylabel('Flux [ph/s/tbw]')
        ax.set_title('Transmission / Per MIl bandwidth')
        ax.minorticks_on()
        # ax.grid(which='both', axis='both')
    
    plt.suptitle('PGM-Undulator (SU)')
    plt.tight_layout()
    plt.savefig(f'plot/Comparison_PerMIl{add_to_title}.pdf')
    plt.show()