import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

path = 'Data/Bacterium/EC.dat.gz'


fh = open(path,"rb")
G = nx.read_edgelist(fh, create_using=nx.DiGraph())
fh.close()
nodes = G.nodes()
nodes = [node for node in nodes if int(node) < 1000000]
#print(nodes)
n = len(nodes)
print(n)
li = nx.all_pairs_shortest_path_length(G)
#print (li)
l = []
for node in nodes:
    #l = l + list(li[node].values())
    #l = l + [li[node][x] for x in nodes if x in li[node] and li[node][x] != 0]
    l = l + [li[node][x] for x in nodes if x in li[node]]

print(len(l))
#print(l)
paths = np.array(l)
paths = paths/2

plt.hist(paths,bins=9)
#ax.axis([1,1000,0.001,1])

plt.xlabel('Path Length(l)',fontsize=40)
plt.ylabel('Number of Paths(π(l))',fontsize=40)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
#plt.tight_layout()
plt.show()
