import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

path = 'Data/'

dirs = os.listdir(path)

for dir in dirs:
    listing = os.listdir(path+dir+'/')
    if dir == 'Archae':
        s = '^'
        c = 'r'
    else:
        if dir == 'Bacterium':
            s = 's'
            c = 'g'
        else:
            s = 'D'
            c = 'b'
    for infile in listing:
        print("Current file is ",infile)
        fh = open(path+dir+'/'+infile,"rb")
        G = nx.read_edgelist(fh, create_using=nx.DiGraph())
        fh.close()
        nodes = G.nodes()
        nodes = [node for node in nodes if int(node) < 1000000]
        print(len(nodes))
        n = len(nodes)
        li = nx.all_pairs_shortest_path_length(G)
        l = []
        for node in nodes:
            l = l + [li[node][x] for x in nodes if x in li[node]]

        paths = np.array(l)
        diameter = np.mean(paths)/2
        plt.errorbar(n,diameter,yerr = np.std(paths)/2,fmt=s,color=c,ms='12',markeredgecolor=c)
#plt.axis([0,900,1,5])
plt.xlabel('Number of Nodes(N)',fontsize=40)
plt.ylabel('Diameter',fontsize=40)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
#plt.tight_layout()
plt.show()
