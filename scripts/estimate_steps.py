import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

INPUT='../trace_dot/traces_2034_refine.dot'
OUTPUT='../trace_dot/traces_2034_steps.jpg'
G = nx.DiGraph(nx.drawing.nx_pydot.read_dot(INPUT))

nnodes = G.order()
print('nnodes = ',nnodes)
matrix = np.zeros([nnodes,nnodes])
print(type(matrix[0,0]))
nodesarray = range(nnodes)

for edges, edges_datadict in G.edges.items():
	outnode = int(edges[0])
	innode = int(edges[1])
	label=edges_datadict['label']
	proba = float("{0:.2f}".format(float(label[1:-1].split()[1])))
	matrix[outnode,innode] = proba

for i in range(nnodes):
	line = matrix[i]
	sumprob = line.sum()
#	print(sumprob)
	if (sumprob>1):
		line[np.argmax(line)] = line[np.argmax(line)]-(sumprob-1)
	if (sumprob<1):
		line[nnodes-2] = line[nnodes-2]+1-sumprob
	sumprob = line.sum()
	print(sumprob)
	
print(matrix.sum(axis=1))
#matrix[:,nnodes-2] = matrix[:,nnodes-2]+1-matrix.sum(axis=1)

loop = 10000
steparray = np.zeros(loop)
criteria = 30
steplist = np.zeros(criteria)
for indice in range(loop):
	steps = 0
	node = nnodes-1
	for i in range(criteria):
		node = np.random.choice(nodesarray, 1, replace=False, p=matrix[node])[0]
		if node == nnodes-2:
			steps = i
			break
		steps = i
	steplist[steps] = steplist[steps] + 1
	steparray[indice] = steps
print('steplist = ',steplist)
mean_step = np.mean(steparray)
median_step = np.median(steparray)
print('mean_step = ',mean_step)
print('median_step = ',median_step)

plt.figure()
plt.plot(range(criteria),steplist/loop,'k')
plt.axis([0, criteria, 0, 0.3])
plt.xlabel('number of steps')
plt.ylabel('probability')
plt.savefig(OUTPUT)
plt.show()