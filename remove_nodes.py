import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Returns the diameter(average shortest path length) of network G with n nodes
def diameter(G,n, nodes):
    li = nx.all_pairs_shortest_path_length(G)
    l = []
    for node in nodes:
        l = l + [li[node][x] for x in nodes if x in li[node]]

    paths = np.array(l)
    diameter = np.mean(paths)/2

    return diameter


path = 'Data/Bacterium/EC.dat.gz'
N = 60

fh = open(path,"rb")
G = nx.read_edgelist(fh, create_using=nx.DiGraph())
fh.close()
nodes = G.nodes()
nodes = [node for node in nodes if int(node) < 1000000]
n = len(nodes)
random, = plt.plot(0,diameter(G,n,nodes),'rs',ms=10,markeredgecolor='r')
for i in range(N):
    print(i)
    G.remove_node(nodes.pop(np.random.randint(n-i)))
    dia = diameter(G,n-i-1, nodes)
    random, = plt.plot(i+1,dia,'rs',ms=10,markeredgecolor='r')

fh = open(path,"rb")
G = nx.read_edgelist(fh, create_using=nx.DiGraph())
fh.close()
nodes = G.nodes()

nodes = [node for node in nodes if int(node) < 1000000]
n = len(nodes)

in_degree =  G.in_degree(nodes)
hub, = plt.plot(0,diameter(G,n,nodes),'go',ms=10,markeredgecolor='g')
for i in range(N):
    print(i)
    index = max(in_degree, key=lambda k: in_degree[k])
    in_degree.pop(index)
    nodes.remove(str(index))
    G.remove_node(str(index))
    dia = diameter(G,n-i-1, nodes)
    hub, = plt.plot(i+1,dia,'go',ms=10,markeredgecolor='g')

plt.legend([random,hub],['Random','Hub'],fontsize=40)
plt.xlabel('Number of Nodes Removed(M)',fontsize=40)
plt.ylabel('Diameter',fontsize=40)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.show()
