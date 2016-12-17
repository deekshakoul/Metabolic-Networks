from os import walk
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
def clustering_coeff(G):
	mean_degree = float(sum(G.degree().values()))/float(G.order())
	return mean_degree/float(G.order())

bacterium_path = '/home/deeksha/Desktop/network/data/bacterium/'
archae_path = '/home/deeksha/Desktop/network/data/barchae/'
eukaryote_path = '/home/deeksha/Desktop/network/data/eukaryote/'


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

global_arr1 = np.zeros(9);
global_arr2 = np.zeros(9);

bacterium_graphs = []

for b in bacterium_files:
	G = nx.DiGraph();
	f = open(bacterium_path+b);
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

	for k in dd2:
		for v in dd2[k]:
			val_2 = v;
		 	val_1 = dd1[val_2] #list of nodes attached to node k
			for i in xrange(0,len(val_1) - 1):		
				G.add_edge(k,val_1[i]) 	
	list_nodes = G.nodes()
	nodes_in_degree = G.in_degree(list_nodes) # list of nodes - check frequency of each degree
	in_degree = nodes_in_degree.values()
	bins = np.logspace(0,3,10)
	num_nodes = len(list_nodes)
	hist,freq = np.histogram(in_degree,bins)
	arr11 = hist/float(num_nodes)
	global_arr1 = np.add(global_arr1,arr11)
	
	nodes_out_degree = G.out_degree(list_nodes) 
	out_degree = np.array(nodes_out_degree.values())
	x2,fq = np.histogram(out_degree,bins)
  	arr12 = x2/float(num_nodes)
	global_arr2 = np.add(global_arr2,arr12)
	#new file
for a in archae_files:
	G = nx.DiGraph();
	f = open(achae_path+a);
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

	for k in dd2:
		for v in dd2[k]:
			val_2 = v;
		 	val_1 = dd1[val_2] #list of nodes attached to node k
			for i in xrange(0,len(val_1) - 1):		
				G.add_edge(k,val_1[i]) 	
	list_nodes = G.nodes()
	nodes_in_degree = G.in_degree(list_nodes) # list of nodes - check frequency of each degree
	in_degree = nodes_in_degree.values()
	bins = np.logspace(0,3,10)
	hist,freq = np.histogram(in_degree,bins)
	num_nodes = len(list_nodes)
	arr11 = hist/float(num_nodes)
	global_arr1 = np.add(global_arr,arr11)
	
	nodes_out_degree = G.out_degree(list_nodes) 
	out_degree = np.array(nodes_out_degree.values())
	x2,fq = np.histogram(out_degree,bins)
  	arr12 = x2/float(num_nodes)
	global_arr2 = np.add(global_arr2,arr12)

  
for e in eukaryote_files:
	G = nx.DiGraph();
	f = open(eukaryote_path+e);
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

	for k in dd2:
		for v in dd2[k]:
			val_2 = v;
		 	val_1 = dd1[val_2] #list of nodes attached to node k
			for i in xrange(0,len(val_1) - 1):		
				G.add_edge(k,val_1[i]) 	
	list_nodes = G.nodes()
	num_nodes = len(list_nodes)
	nodes_in_degree = G.in_degree(list_nodes) # list of nodes - check frequency of each degree
	in_degree = nodes_in_degree.values()
	bins = np.logspace(0,3,10)
	hist,freq = np.histogram(in_degree,bins)
	arr11 = hist/float(num_nodes)
	global_arr1 = np.add(global_arr1,arr11)
	
	nodes_out_degree = G.out_degree(list_nodes) 
	out_degree = np.array(nodes_out_degree.values())
	x2,fq = np.histogram(out_degree,bins)
  	arr12 = x2/float(num_nodes)
	global_arr2 = np.add(global_arr2,arr12)

global_arr1 = global_arr1/43;
global_arr2 = global_arr2/43;
bins = np.logspace(0,3,10)
ax = plt.subplot() 
out_plot, = ax.plot(bins[:-1],global_arr2,marker='s',linestyle='--',color='r',label='out_degree')
in_plot, = ax.plot(bins[:-1],global_arr1,marker='o',linestyle='-',color='b',label='in_degree',)
plt.xlabel('K',fontsize=25)
plt.ylabel('P(K)',fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend([in_plot, out_plot],['in_degree','out_degree'],fontsize=25)



ax.set_yscale("log",nonposy="clip")
ax.set_xscale("log",nonposx="clip")
plt.show()



