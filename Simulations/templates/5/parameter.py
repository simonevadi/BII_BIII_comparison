import numpy as np

rml_file_name_tor_1200= 'NAP-LEEM_toroid_1200'
rml_file_name_tor_2400= 'NAP-LEEM_toroid_2400'
rml_file_name_kb = 'NAP-LEEM_KB'


order       = 1
SlitSize    = np.array([ .05, .04, .03, .02, .01, 0.005])
grating     = np.array([1200])
blaze       = np.array([0.9])
cff         = np.array([2.25])

energy_flux = np.arange(100, 1601,500)
energy_rp   = np.arange(100, 1601,500)

nrays_flux  = 1e6 
nrays_rp    = 1e6

round_flux = 1
round_rp   = 2


ncpu = 7
### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]
