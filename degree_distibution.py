from os import walk
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
bacterium_path = '/home/deeksha/Desktop/network/data/bacterium/EC.dat'
archae_path = '/home/deeksha/Desktop/network/data/archae/AG.dat'
eukaryote_path = '/home/deeksha/Desktop/network/data/eukaryote/CE.dat' 


G = nx.DiGraph();
f = open(eukaryote_path);
dd1 = defaultdict(list); # type of value is list
dd2 = defaultdict(list);
for line in f:
	nodes = line.split();
	nodes_int = [int(x) for x in nodes]
	if nodes_int[0]>= 1000000:
		dd1[nodes_int[0]].append(nodes_int[1]) # list with key 100000 and value 1,2,3
		G.add_node(nodes_int[1])
	else:
		dd2[nodes_int[0]].append(nodes_int[1]) #list with key 1 and values 100001,1000002,10003  
		G.add_node(nodes_int[0])

#traverse the list dd2 and make directed edges between them

for k in dd2:
	for v in dd2[k]:
		val_2 = v;
	 	val_1 = dd1[val_2] #list of nodes attached to node k
		for i in xrange(0,len(val_1) - 1):		
			G.add_edge(k,val_1[i]) 		

list_nodes = G.nodes()
y_in = 2.1
y_out = 2.2
nodes_in_degree = G.in_degree(list_nodes) # list of nodes - check frequency of each degree
in_degree = nodes_in_degree.values()
in_degree = np.array(in_degree)

y_in =  np.bincount(in_degree) # include zeros also
y = y_in/float(len(list_nodes))

ax = plt.subplot()

bins = np.logspace(0,3,10)
hist,freq = np.histogram(in_degree,bins)
in_plot, = ax.plot(freq[:-1],hist/float(len(list_nodes)),marker='o',linestyle='-',color='r',label='in_degree')
 
nodes_out_degree = G.out_degree(list_nodes) 
out_degree = np.array(nodes_out_degree.values())
z =  np.bincount(out_degree) 
z = z/float(len(list_nodes))
x2,fq = np.histogram(out_degree,bins)
out_plot, = ax.plot(fq[:-1],x2/float(len(list_nodes)),marker='s',linestyle='--',color='b',label='out_degree')

ax.set_yscale("log",nonposy="clip")
ax.set_xscale("log",nonposx="clip")

plt.xlabel('K',fontsize=25)
plt.ylabel('P(K)',fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend([in_plot, out_plot],['in_degree','out_degree'],fontsize=25)

plt.show()
