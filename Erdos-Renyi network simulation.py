#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import os, sys
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
import pandas as pd
import scipy
import matplotlib.pyplot as plt

'''N=nodes(20)
You will need to simulate 100 random initializations for 
p=0.05, p=0.1 and p=0.3 and 
plot distributions for number of edges in a single figure.
'''


#n and p as parameters
def calculate_erdos_renyi(n,p):
    graph = nx.Graph()
    
    
    #add 100 nodes
    for i in range(100):
        graph.add_node(i)
        
    #repeat for all pair of nodes    
    for j in range(100):
        for k in range(100):
            
            #Get rid of self loops
            if j==k:
                break
            
            #Generate random number r
            r=random.uniform(0, 1)
            
            #If r<p then add link between j and k
            if(r<p):
                graph.add_edge(j, k)
    
    return graph


def simulate_erdos_renyi(Initialization, probabilities):
    
    fig, ax = plt.subplots()
    
    # Loop over the probabilities
    for p in probabilities:
        
        # Initialize an empty list to store the number of edges for each initialization
        num_edges = []
    
        # Loop over the initialization
        for i in range(Initialization):
            
            # Generate an Erdos-Renyi graph with n=100 nodes and probability p
            G = calculate_erdos_renyi(100, p)
            
            # Append the number of edges to the list
            num_edges.append(G.number_of_edges())
            
        
        # Plot a histogram of the number of edges for this probability
        ax.hist(num_edges, alpha=0.5, bins=20, label=f'p={p}')
        
    # Add labels to the plot
    ax.set_xlabel('Number of Edges')
    ax.set_ylabel('Frequency')
    
    # Add legend to the plot
    ax.legend()

    # Show the plot
    plt.show()

    

#MAIN PROGRAM
Initialization=100
probabilities = [0.05, 0.1, 0.3]

#simulate network
graph=simulate_erdos_renyi(Initialization, probabilities)



# In[ ]:




