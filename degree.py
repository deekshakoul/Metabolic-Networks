import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

path = 'Data/'

dirs = os.listdir(path)

for dir in dirs:
    listing = os.listdir(path+dir+'/')
    if dir == 'Archae':
        c = 'r'
        s = '^'
    else:
        if dir == 'Bacterium':
            c = 'g'
            s = 's'
        else:
            c = 'b'
            s = 'D'
    for infile in listing:
        print("Current file is ",infile)
        fh = open(path+dir+'/'+infile,"rb")
        G = nx.read_edgelist(fh, create_using=nx.DiGraph())
        fh.close()
        nodes = G.nodes()
        nodes = [node for node in nodes if int(node) < 1000000]
        print(len(nodes))
        n = len(nodes)
        in_degree = G.in_degree()
        in_degree = [in_degree[node] for node in nodes]
        l_n  =  np.sum(np.array(in_degree))/n
        #out_degree = G.out_degree()
        #out_degree = [out_degree[node] for node in nodes]
        #l_n  =  np.sum(np.array(out_degree))/n
        print(l_n)
        plt.plot(n,l_n,c+s,ms='12',markeredgecolor=c)

plt.xlabel('Number of Nodes(N)',fontsize=40)
plt.ylabel(r'$\frac{L_{in}}{N}$',fontsize=40)
#plt.ylabel(r'$\frac{L_{out}}{N}$',fontsize=40)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.show()
