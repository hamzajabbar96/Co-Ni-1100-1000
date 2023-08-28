import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pydiffusion.core import DiffSystem
from pydiffusion.utils import step, mesh
from pydiffusion.simulation import mphSim
from pydiffusion.plot import profileplot, DCplot
from pydiffusion.io import read_csv, save_csv

diffsys = DiffSystem(Xr=[0, 1], X=[0, 1], DC=[1e-14, 1e-14], name='Constant D')

dis = mesh(0, 1000, 501)
profile_init = step(dis, 500, diffsys, name='Initial step profile')

fig = plt.figure(figsize=(16, 6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)
ax1.set_title('Diffusion Coefficients', fontsize=15)
ax2.set_title('Initial Step Profile', fontsize=15)
DCplot(diffsys, ax1)
profileplot(profile_init, ax2)

time = 200 * 3600
profile_final = mphSim(profile_init, diffsys, time)

ax = profileplot(profile_init, ax2, ls='--')
profileplot(profile_final, ax, c='r')

plt.show()
