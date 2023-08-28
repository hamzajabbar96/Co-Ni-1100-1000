import pandas as pd
import matplotlib.pyplot as plt  
from pydiffusion.core import DiffProfile
from pydiffusion.plot import profileplot
from pydiffusion.smooth import datasmooth

data = pd.read_excel('/Users/homepc/Desktop/Final/CoNi_exp.xls')

dis, X = data['dis'], data['X']

CoNi_exp = DiffProfile(dis=dis, X=X, name='CoNi_exp')

fig, ax = plt.subplots()

ax = profileplot(CoNi_exp, ax, c='b', marker='o', ls='none', fillstyle='none')

plt.show()

CoNi_sm = datasmooth(CoNi_exp, [311.5, 340.5], n=500)

profileplot(CoNi_sm, ax, c='r')


save_excel('/Users/homepc/Desktop/Final/CoNi_sm.xls', profile=CoNi_sm)

