import numpy as np

rml_file_name_bessy2_HiBeta_37m    = 'bessy2hi_37m_PGM_2Perc_coupling_errors_on'
rml_file_name_bessy2_HiBeta_56m    = 'bessy2hi_56m_PGM_2Perc_coupling_errors_on'
rml_file_name_bessy3_37m           = 'bessy3_37m_PGM_2Perc_coupling_errors_on'
rml_file_name_bessy3_56m           = 'bessy3_56m_PGM_2Perc_coupling_errors_on'
       

# rml_file_name_bessy2_LoBeta_long_56    = 'bessy2lo_56m_PGM_2Perc_coupling_errors_on'


order       = 1
# SlitSize    = np.array([.027])
grating     = np.array([1200])
cff         = np.array([2.5])

energy_flux = np.arange(100, 2101,100)
energy_rp   = np.arange(100, 2101,100)

nrays_flux  = 1e5
nrays_rp    = 1e5

round_flux = 10
round_rp   = 10


ncpu = 12
### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]
