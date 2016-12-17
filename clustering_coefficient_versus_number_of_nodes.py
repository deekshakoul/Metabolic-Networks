from os import walk
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

bacterium_path = '/home/saumya/Documents/DAIICT/seventh_sem/complex_networks/DATA/bacterium/'
archae_path = '/home/saumya/Documents/DAIICT/seventh_sem/complex_networks/DATA/archae/'
eukaryote_path = '/home/saumya/Documents/DAIICT/seventh_sem/complex_networks/DATA/eukaryote/'

bacterium_files = []
for (dirpath, dirnames, filenames) in walk(bacterium_path):
    bacterium_files.extend(filenames)
    break

archae_files = []
for (dirpath, dirnames, filenames) in walk(archae_path):
    archae_files.extend(filenames)
    break

eukaryote_files = []
for (dirpath, dirnames, filenames) in walk(eukaryote_path):
    eukaryote_files.extend(filenames)
    break

bacterium_graphs = []
for b in bacterium_files:
	G = nx.Graph()  
	f = open(bacterium_path+b)
	ddd = defaultdict(list)
	for line in f:
		nodes = line.split()
		nodes_int = [int(x) for x in nodes]
		if nodes_int[0] >= 1000000:
			ddd[nodes_int[0]].append(nodes_int[1])
			G.add_node(nodes_int[1])
		else:
			ddd[nodes_int[1]].append(nodes_int[0])
			G.add_node(nodes_int[0])
	for n in ddd.keys():
		for u in ddd[n]:
			for v in ddd[n]:
				if u!=v:
					G.add_edge(u,v)			
	bacterium_graphs.append(G)


archae_graphs = []
for a in archae_files:
	G = nx.Graph()  
	f = open(archae_path+a)
	ddd = defaultdict(list)
	for line in f:
		nodes = line.split()
		nodes_int = [int(x) for x in nodes]
		if nodes_int[0] >= 1000000:
			ddd[nodes_int[0]].append(nodes_int[1])
			G.add_node(nodes_int[1])
		else:
			ddd[nodes_int[1]].append(nodes_int[0])
			G.add_node(nodes_int[0])
	for n in ddd.keys():
		for u in ddd[n]:
			for v in ddd[n]:
				if u!=v:
					G.add_edge(u,v)
	archae_graphs.append(G)

eukaryote_graphs = []
for e in eukaryote_files:
	G = nx.Graph()  
	f = open(eukaryote_path+e)
	ddd = defaultdict(list)
	for line in f:
		nodes = line.split()
		nodes_int = [int(x) for x in nodes]
		if nodes_int[0] >= 1000000:
			ddd[nodes_int[0]].append(nodes_int[1])
			G.add_node(nodes_int[1])
		else:
			ddd[nodes_int[1]].append(nodes_int[0])
			G.add_node(nodes_int[0])
	for n in ddd.keys():
		for u in ddd[n]:
			for v in ddd[n]:
				if u!=v:
					G.add_edge(u,v)
	eukaryote_graphs.append(G)

N = []
N_bac = []
clustering_bac = []
for G_bac in bacterium_graphs:
	N.append(G_bac.order())
	N_bac.append(G_bac.order())
	clustering_bac.append(nx.average_clustering(G_bac))

N_arc = []
clustering_arc = []
for G_arc in archae_graphs:
	N.append(G_arc.order())
	N_arc.append(G_arc.order())
	clustering_arc.append(nx.average_clustering(G_arc))

N_euk = []
clustering_euk = []
for G_euk in eukaryote_graphs:
	N.append(G_euk.order())
	N_euk.append(G_euk.order())
	clustering_euk.append(nx.average_clustering(G_euk))

clustering_2 = []
for n in N:
	G = nx.barabasi_albert_graph(n,10)
	clustering_2.append(nx.average_clustering(G))

ax = plt.subplot()
bac = ax.scatter(N_bac,clustering_bac,s=37,color='red',marker='o')
arc = ax.scatter(N_arc,clustering_arc,s=37,color='green',marker='+')
euk = ax.scatter(N_euk,clustering_euk,s=37,color='blue',marker='x')
scale = ax.scatter(N,clustering_2,s=37,color='black',marker='s')
plt.legend((bac,arc,euk,scale),('bacterium','archae','eukaryotes','scale free'),scatterpoints=1,loc=7,ncol=4,fontsize=25)
ax.set_xscale("log",nonposy='clip')
plt.xlabel('log(N)',fontsize=25)
plt.ylabel('C(N)',fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.show()

