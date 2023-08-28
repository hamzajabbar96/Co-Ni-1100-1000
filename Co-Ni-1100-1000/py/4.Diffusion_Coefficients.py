import pandas as pd
from pydiffusion.plot import profileplot, DCplot, SFplot
from pydiffusion.Dtools import Dmodel
from pydiffusion.io import read_csv, save_csv

CoNi_sm, _ = read_csv('/Users/homepc/Desktop/Final/CoNi_sm.csv')

time = 1000 * 3600  


Xspl = [[0.0025311643355943733, 0.2428008244781973]]  


diffsys_init_auto = Dmodel(CoNi_sm, time, Xspl=Xspl, Xlim=[0, 1])


ax = DCplot(diffsys_init_auto)
save_csv('/Users/homepc/Desktop/Final/CoNi_DC.csv', profile=CoNi_sm, diffsys=diffsys_init_auto)
