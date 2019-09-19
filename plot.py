import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('istherecorrelation.csv', sep=';', decimal=',')
data.set_index("Year", inplace=True)

x = data['WO [x1000]']
y = data['NL Beer consumption [x1000 hectoliter]']

fig, ax1 = plt.subplots(dpi=300)

color = 'tab:red'
ax1.set_xlabel('WO [x1000]')
ax1.set_ylabel('exp', color=color)
ax1.plot(x, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('NL Beer consumption [x1000 hectoliter]', color=color)
ax2.plot(y, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
fig.savefig("beerplot.png",bbox_inches='tight')
