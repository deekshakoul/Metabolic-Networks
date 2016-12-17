from os import walk
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

G_cd = nx.Graph()  
f = open('SC.dat')
ddd = defaultdict(list)
for line in f:
	nodes = line.split()
	nodes_int = [int(x) for x in nodes]
	if nodes_int[0] >= 1000000:
		ddd[nodes_int[0]].append(nodes_int[1])
		G_cd.add_node(nodes_int[1])
	else:
		ddd[nodes_int[1]].append(nodes_int[0])
		G_cd.add_node(nodes_int[0])
for n in ddd.keys():
	for u in ddd[n]:
		for v in ddd[n]:
			if u!=v:
				G_cd.add_edge(u,v)	

degrees = []
clustering_degrees = []
for n in G_cd.nodes():
	degrees.append(G_cd.degree(n))
	clustering_degrees.append(nx.clustering(G_cd,n))

G_sf = nx.barabasi_albert_graph(G_cd.order(),10)
degrees_sf = []
clustering_degrees_sf = []
for n in G_sf.nodes():
	degrees_sf.append(G_sf.degree(n))
	clustering_degrees_sf.append(nx.clustering(G_sf,n))

ax = plt.subplot()
bac_degree = ax.scatter(degrees,clustering_degrees,s=30,color='blue',marker='o')
#arc = ax.scatter(N_arc,clustering_arc,s=30,color='green',marker='+')
#euk = ax.scatter(N_euk,clustering_euk,s=30,color='blue',marker='x')
scale_degree = ax.scatter(degrees_sf,clustering_degrees_sf,s=30,color='black',marker='s')
plt.legend((bac_degree,scale_degree),('Saccharomyces cerevisiae','scale free'),scatterpoints=1,loc='upper right',ncol=4,fontsize=40)
ax.set_xscale("log",nonposx='clip')
ax.set_yscale("log",nonposy='clip')
plt.xlabel('k',fontsize=40)
plt.ylabel('C(k)',fontsize=40)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.show()
