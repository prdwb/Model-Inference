import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint

# for python3 networkx 2.0
INPUT='../figures and graphs/qa_all_refine.dot'
OUTPUT='../figures and graphs/qa_all_refine_style.dot'
G = nx.DiGraph(nx.drawing.nx_pydot.read_dot(INPUT))

for nodes, nodes_datadict in G.nodes.items():
	label=nodes_datadict['label']
	if '"RQ"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='red'
		nodes_datadict['style']='filled'
		nodes_datadict['fontcolor']='white'
	if '"PF"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='orange'
		nodes_datadict['style']='filled'
	if '"INITIAL"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='cyan'
		nodes_datadict['style']='filled'
		nodes_datadict['shape']='box'
	if '"TERMINAL"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='cyan'
		nodes_datadict['style']='filled'
		nodes_datadict['shape']='diamond'
	if '"FD"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='bisque'
		nodes_datadict['style']='filled'
		nodes_datadict['fontcolor']='black'
	if '"CQ"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='red'
		nodes_datadict['style']='filled'
		nodes_datadict['fontcolor']='white'
	if '"GG"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='hotpink'
		nodes_datadict['style']='filled'
	if '"FQ"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='red'
		nodes_datadict['style']='filled'
		nodes_datadict['fontcolor']='white'
	if '"IR"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='red'
		nodes_datadict['style']='filled'
		nodes_datadict['fontcolor']='white'
	if '"OQ"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='red'
		nodes_datadict['style']='filled'
		nodes_datadict['fontcolor']='white'
	if '"NF"' in nodes_datadict.values():
		nodes_datadict['orange']='red'
		nodes_datadict['style']='filled'
	if '"PA"' in nodes_datadict.values():
		nodes_datadict['fillcolor']='green'
		nodes_datadict['style']='filled'

for edges, edges_datadict in G.edges.items():
	label=edges_datadict['label']
	proba = float("{0:.2f}".format(float(label[1:-1].split()[1])))
	edges_datadict['penwidth'] = proba * 10
	edges_datadict['label'] = str(proba)

nx.drawing.nx_pydot.write_dot(G, OUTPUT)
