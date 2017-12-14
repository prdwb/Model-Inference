TOLERANCE = 0.02

import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

INPUT='./qa_all.dot'
OUTPUT='./qa_all_refine.dot'
G = nx.DiGraph(nx.drawing.nx_pydot.read_dot(INPUT))

ebunch=[]
for edges, edges_datadict in G.edges.items():
	label=edges_datadict['label']
	proba = float("{0:.2f}".format(float(label[1:-1].split()[1])))
	print(proba)
	if proba<=TOLERANCE:
		ebunch.append(edges)
	edges_datadict['label'] = "P: "+str(proba)

G.remove_edges_from(ebunch)

for nodes, nodes_datadict in G.nodes.items():
	pprint(nodes)

sumplist = [] 
for innode, nbrdict in G.adjacency():
	probasum = 0
	for outnode, ladict in nbrdict.items():
		label = ladict['label']
		probatemp = float("{0:.2f}".format(float(label[1:].split()[1])))
#		print(probatemp)
		probasum = probasum + float(probatemp)
	sumplist.append(probasum)
print('sumplist = ',sumplist)

for edges, edges_datadict in G.edges.items():
	index = int(edges[0])
	print(index)
	label=edges_datadict['label']
	proba=float("{0:.2f}".format(float(label[1:].split()[1])/sumplist[index]))
	edges_datadict['label'] = "P: "+str(proba)

nx.drawing.nx_pydot.write_dot(G, OUTPUT)