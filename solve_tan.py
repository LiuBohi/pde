import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# To plot the fucntion $\tan(t)$ and the line.
num = 100
intervals = [np.linspace(np.pi/2 + np.pi/num + k*np.pi,
             np.pi/2 + (k+1) * np.pi,num=num,
             endpoint=False) 
             for k in range(0,5)]
intervals.insert(0, np.linspace(0,np.pi/2,num=int(num/2),endpoint=False))
t= np.linspace(0, 5 * np.pi, num=num)
fig, ax = plt.subplots(figsize=(12,6))

zeros = []
for i in intervals:
    y = np.tan(i)
    ax.plot(i, y, color='lightblue')
    x0 = optimize.bisect(lambda t:np.tan(t)+t,i[0],i[-1])
    zeros.append(x0)
    ax.scatter(x0, -x0, color='red', marker='*',s=64)
ax.plot(t, -t, color='orange')
x0 = zeros[3]
x1 = t[int(num/2)] + 3
x2 = t[-1]
ax.annotate(r'$\tan(t)=-t$',
            xy=(x0+0.1, -x0-0.1),
            xytext=(x0+1, -x0-8),
            arrowprops=dict(arrowstyle='->',
                            connectionstyle='arc3, rad=-0.3'),
            )
ax.annotate(r'$y=\tan(t)$',
            xy=(x1, np.tan(x1)),
            xytext=(x1+1, np.tan(x1)),
            arrowprops=dict(arrowstyle='->',
                            connectionstyle='arc3, rad=-0.3'),
            )
ax.annotate(r'$y=-t$',
            xy=(x2, -x2),
            xytext=(x2+1, -x2),
            arrowprops=dict(arrowstyle='->',
                            connectionstyle='arc3, rad=-0.3'),
            )            

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data',0))
ax.set_xlabel(r'$t$',fontsize=12, loc='right')
ax.spines['left'].set_position(('data',0))
ax.set_ylabel(r'$y$', fontsize=12, 
              labelpad=-20, loc='top', rotation=0)
ax.set_title(r'Function $y=\tan(t)$'+'\nand line '+r'$y=-t$',
             fontsize=14, fontweight='bold')

plt.savefig('tan_line.jpg', dpi=300)
plt.show()

