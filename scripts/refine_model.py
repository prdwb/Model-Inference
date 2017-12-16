TOLERANCE = 0.05

import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

INPUT='../figures and graphs/qa_all.dot'
OUTPUT='../figures and graphs/qa_all_refine.dot'
G = nx.DiGraph(nx.drawing.nx_pydot.read_dot(INPUT))

print('number of nodes = ',G.number_of_nodes())
print('number of edges = ',G.size())

ebunch=[]
sumpro = 0
for edges, edges_datadict in G.edges.items():
	label=edges_datadict['label']
	proba = float("{0:.2f}".format(float(label[1:-1].split()[1])))
	if proba<=TOLERANCE:
		ebunch.append(edges)
		sumpro = sumpro + proba
	edges_datadict['label'] = "P: "+str(proba)

G.remove_edges_from(ebunch)
print('ebunch = ',len(ebunch))
print('proba = ',sumpro)

sumplist = [] 
for innode, nbrdict in G.adjacency():
	probasum = 0
	for outnode, ladict in nbrdict.items():
		label = ladict['label']
		probatemp = float("{0:.2f}".format(float(label[1:].split()[1])))
		probasum = probasum + float(probatemp)
	sumplist.append(probasum)

for edges, edges_datadict in G.edges.items():
	index = int(edges[0])
	label=edges_datadict['label']
	proba=float("{0:.2f}".format(float(label[1:].split()[1])/sumplist[index]))
	edges_datadict['label'] = "P: "+str(proba)

nx.drawing.nx_pydot.write_dot(G, OUTPUT)