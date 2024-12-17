import numpy as np

# these must match the name of the rml files in the rml folder that you want to simulate

rml_file_name_bessy2_52m     = 'bessy2_LoBeta_long_52'
rml_file_name_bessy3_52m     = 'bessy3_long_52'


order       = 1
SlitSize    = np.array([.020])
grating     = np.array([2400])
cff         = np.array([2.50])

energy_flux = np.arange(50, 2101, 50)
energy_rp   = np.arange(50, 2101, 50)

nrays_flux  = 1e5
nrays_rp    = 1e5

round_flux = 5
round_rp   = 5

ncpu       = 12

### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]
