import matplotlib.pyplot as plt
import pandas as pd
# create data
x = [10,20,30,40,50]
y = [30,30,30,30,30]

data = pd.read_csv("aggregation.csv")
data = data.to_numpy()
print(data[0])
# plot lines
ls = []
date = []
btc = []
twtr = []
l = data.shape[0]
joe = []
katy = []
ll = data.shape[1]
print(ll)
for i in range(10):
	k = l - 7 - (10 - i)
	ls.append(data[k][4])
	date.append(data[k][1] + "-" + data[k][2])
	btc.append(data[k][5] / 1000.0)
	twtr.append(data[k][7])
	joe.append(data[k][ll-3])
	katy.append(data[k][ll-1])
print(joe)
print(katy)
fig, ax = plt.subplots()
ax.set_xticklabels(date , fontsize=6 )
ax.plot(date, ls, label = "number of Elon's tweets")
ax.plot(date, btc, label = "btc AVG high")
ax.plot(date, twtr, label = "twtr AVG high")
ax.plot(date, joe, label = "number of Joe's tweets")
ax.plot(date, katy, label = "number of Katy's tweets")
fig.autofmt_xdate()
#plt.set_yticks( np.linspace(lb, ub, 25 ) )
plt.legend()
plt.show()
