import numpy as np

rml_file_name_bessy3_short          = 'Bessy3_short'
rml_file_name_bessy3_long           = 'Bessy3_long'
rml_file_name_bessy2_HiBeta_short   = 'Bessy2_HiBeta_short'
rml_file_name_bessy2_HiBeta_long    = 'Bessy2_HiBeta_long'
rml_file_name_bessy2_LoBeta_short   = 'Bessy2_LoBeta_short'
rml_file_name_bessy2_LoBeta_long    = 'Bessy2_LoBeta_long'


order       = 1
SlitSize    = np.array([ .1, .05, .01])
grating     = np.array([2400])
cff         = np.array([2.25])

energy_flux = np.arange(100, 2001,50)
energy_rp   = np.arange(100, 2001,50)

nrays_flux  = 1e5
nrays_rp    = 1e5

round_flux = 5
round_rp   = 5


ncpu = 10
### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]
