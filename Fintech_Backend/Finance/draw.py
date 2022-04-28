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
for i in range(data.shape[0]):
	ls.append(data[i][4])
	date.append(data[i][1] + "-" + data[i][2])
print(ls)
print(date)
fig, ax = plt.subplots()
ax.set_xticklabels(date , fontsize=6 )
ax.plot(date, ls, label = "line 1")
fig.autofmt_xdate()
#plt.set_yticks( np.linspace(lb, ub, 25 ) )
plt.legend()
plt.show()
