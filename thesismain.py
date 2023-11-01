import matplotlib.pyplot as plt
import numpy as np
import os


#Storing all OGLE files in an array
path_ogle = os.path.expanduser('~/Desktop/thesis/I')
ogle_files = np.array([f for f in os.listdir(path_ogle) if f.endswith('.dat')])



#Random select
n = 0
testing = ogle_files[0]
path = os.path.join(path_ogle, testing)

with open(path, 'r') as file:
    lines = file.readlines()

temp = []
for line in lines:
    columns = line.strip().split()
    try:
        columns = [float(column) for column in columns]
        temp.append(columns)
    except ValueError:
        print("No")

data = np.array(temp)



x = data[:,0]
y = data[:,1]
yerror = data[:,2]

#plt.errorbar(x, y, yerr=yerror, fmt='x', ms=5)
plt.scatter(x, y, c='b', s=5, marker='x')
plt.xlabel('HJD-245000 (days)')
plt.ylabel('I (mag)')
plt.title(f'{testing}')
plt.show()
