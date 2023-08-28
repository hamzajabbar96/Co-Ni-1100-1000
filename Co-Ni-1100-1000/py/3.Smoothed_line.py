import pandas as pd
import matplotlib.pyplot as plt


CoNi_sm = pd.read_excel('/Users/homepc/Desktop/Final/CoNi_sm.xls')


dis = CoNi_sm['dis']  
X = CoNi_sm['X']     


plt.plot(dis, X, label='CoNi_sm', lw=2)
plt.xlabel('Distance (microns')
plt.ylabel('Mole Fraction')
plt.legend()  
plt.grid(True)  
plt.show()
