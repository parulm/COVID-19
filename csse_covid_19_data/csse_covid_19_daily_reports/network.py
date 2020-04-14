import networkx as nx
import random
import time

#Total population or the number of nodes of the network
n = 6400

#Number of days to run this simulation for
days = 5

#transmission probability of giving the virus to a person if there was contact
T = 0.6

#death rate
d = 0.1

#initial number of confirmed cases, dead people. Initial data from March 16th, 2020: 967, 10
cases = 67
dead = 12

#################
print 'Input values are: n =', n, 'cases =', cases

infected = cases-dead
start = time.time()
G = nx.scale_free_graph(n)
print 'Graph created in', time.time()-start, 'seconds'
dead_nodes = random.sample(G.nodes(), dead)
G.remove_nodes_from(dead_nodes)
infected_nodes = random.sample(G.nodes(), infected)

print 'Starting node status assignment'
start = time.time()
for n in G.nodes():
	if n in infected_nodes:
		G.node[n]['status'] = 'infected'
	else:
		G.node[n]['status'] = 'healthy'
print 'Node status assignment finished in', time.time()-start, 'seconds'

for i in range(days):
	print 'Running for day', i+1
	#remove the nodes that die from existing infections
	dead_nodes = random.sample(infected_nodes, int(d*infected))
	G.remove_nodes_from(dead_nodes)
	print 'Dead nodes removed'

	#infect T fraction of an infection node's neighbors
	print 'Spreading infection along an infected node neighbors'
	start = time.time()
	to_infect = []
	for n in G.nodes():
		if G.node[n]['status']=='infected':
			neighbors = G.neighbors(n)
			affected_neighbors = random.sample(neighbors, int(T*len(neighbors)))
			to_infect.extend(affected_neighbors)
	for n in to_infect:
		G.node[n]['status'] = 'infected'
	print 'Spread completed in', time.time()-start, 'seconds'

	print 'Processing network to calculate current state'
	start = time.time()
	infected_total = 0
	for n in G.nodes():
		if G.node[n]['status']=='infected':
			infected_total+=1
	infected_fraction = float(infected_total)/G.number_of_nodes()
	print 'Network processing completed in', time.time()-start, 'seconds'

	print 'Status on day', i+1, ': Deaths today =', len(dead_nodes), '; Active infections =', infected_total, '; Total uninfected =', G.number_of_nodes()-infected_total
