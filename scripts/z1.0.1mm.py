from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 
import numpy as np
#0.1 mm
x = np.array([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.05,0])
y = np.array([46,41.5,37,32,27,21.5,16,10.5,5,2,0])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(0,1,2)
p1 = np.poly1d(np.polyfit(x, y, 1))
plt.errorbar(x, y, xerr=0., yerr=0.5, c='navy', marker='.', mfc='white', ms=5, fmt='o')
plt.plot(x, y, '.',color='navy')
plt.plot(xp, p(xp), '-', color='crimson')
plt.ylim(0,55)
plt.grid(True)
plt.ylabel('J,mA')
plt.xlabel('I.ед')
plt.title('Щель 0.1 mm')
plt.savefig('z101mm.pdf',dpi=300)
plt.show()
#0.06 mm
x = np.array([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.05,0])
y = np.array([44,40,35.5,30,26,21,15.5,10,4.5,2,0])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(0,1,2)
p1 = np.poly1d(np.polyfit(x, y, 1))
plt.errorbar(x, y, xerr=0, yerr=0.5, c='navy', marker='.', mfc='white', ms=5, fmt='o')
plt.plot(x, y, '.',color='navy')
plt.plot(xp, p(xp), '-', color='crimson')
plt.ylim(0,55)
plt.grid(True)
plt.ylabel('J,mA')
plt.xlabel('I.ед')
plt.title('Щель 0.06 mm')
plt.savefig('z1006mm.pdf',dpi=300)
plt.show()
#0.035 mm
x = np.array([0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.05,0])
y = np.array([46,41,36,30.5,25.5,21,15.5,10.5,5,2,0])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(0,1,2)
p1 = np.poly1d(np.polyfit(x, y, 1))
plt.errorbar(x, y, xerr=0, yerr=0.5, c='navy', marker='.', mfc='white', ms=5, fmt='o')
plt.plot(x, y, '.',color='navy')
plt.plot(xp, p(xp), '-', color='crimson')
plt.ylim(0,55)
plt.grid(True)
plt.ylabel('J,mA')
plt.xlabel('I.ед')
plt.title('Щель 0.035 mm')
plt.savefig('z10035mm.pdf',dpi=300)
plt.show()