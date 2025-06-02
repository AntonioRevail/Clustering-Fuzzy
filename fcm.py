"""
========================
Fuzzy c-means clustering
========================



"""
from __future__ import division, print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz


'''
Clustering
----------

Above is our test data. We see three distinct blobs. However, what would happen
if we didn't know how many clusters we should expect? Perhaps if the data were
not so clearly clustered?

Let's try clustering our data several times, with between 2 and 9 clusters.
'''

# Set up the loop and plot
fig1, axes1 = plt.subplots(3,3, figsize=(8, 8))
alldata =np.transpose(pd.read_csv("input.csv", header=None).to_numpy())
#alldata = pd.read_csv("vetorfcmfake1.csv", header=None).to_numpy()
#alldata = np.vstack((xpts, ypts))
fpcs = []
cluster_memberships=[]


pertinencias = [] 


for ncenters, ax in enumerate(axes1.reshape(-1), 2):
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        alldata, ncenters, 2, error=0.005, maxiter=10000, init=None)

    pertinencias.append(u)

    print(u)
    print('------\n')
    print(fpc)
    print('------\n')
    print(fpcs)
    print('------\n')
    # Store fpc values for later
    fpcs.append(fpc)


    
    # Plot assigned clusters, for each data point in training set
    cluster_membership = np.argmax(u, axis=0)
    cluster_memberships.append(u)

    #print(cluster_membership)
    '''
    for j in range(ncenters):
        ax.plot(xpts[cluster_membership == j],
                ypts[cluster_membership == j], '.', color=colors[j])
    '            
    # Mark the center of each fuzzy cluster
    for pt in cntr:
        ax.plot(pt[0], pt[1], 'rs')

    ax.set_title('Centers = {0}; FPC = {1:.2f}'.format(ncenters, fpc))
    ax.axis('off')
'''


indices = [i for i,x in enumerate(fpcs) if x == max(fpcs)][0]
#print (pertinencias[[i for i,x in enumerate(fpcs) if x == max(fpcs)]])

matriz = np.transpose(pertinencias[indices])
print(list(matriz))

D = open('pertinences.csv' , 'w')
'''
for i in matriz:
    D.write(str(i).replace('[','').replace(']','').replace('\n','')+";")
    D.write(str(sum(i))+'\n')
'''
for ln in matriz:
    for i in ln:
        D.write(str(i).replace('[','').replace(']','').replace('\n','')+";")
    D.write(str(sum(ln))+'\n')
D.close()


print(type(pertinencias[indices]))






    
