import random
from typing import List
from bayesian_node import *
from network import *

#OSS: the first values of CPT is always the  first states of the variable itself 

# ---------------------- NODE CREATION ----------------------------

# NODE 1: healt node
possible_value = ["good", "not good"]
healt_node_name = 'healt'
current_value = None
parents = []
children = []
cpt = [{healt_node_name:"good", 'prob': 0.7}, 
       {healt_node_name:'not good', 'prob': 0.7}]
healt_node = BayesianNode(healt_node_name, possible_value , cpt, current_value, children, parents)

# NODE 2: stress node 
possibile_value = ["stressed", "not stressed"]
stress_node_name = 'stress'
current_value = None
parents = [healt_node]
children = []
healt_name = healt_node.get_name()
cpt =  [{stress_node_name: "stressed", healt_node_name: 'good', 'prob':0.2}, 
        {stress_node_name: "stressed", healt_node_name: 'not good', 'prob':0.7},
        {stress_node_name: "not stressed", healt_node_name: 'good', 'prob':0.8},
        {stress_node_name: "not stressed", healt_node_name: 'good', 'prob':0.3}]
stress_node = BayesianNode(stress_node_name, possible_value , cpt, current_value, children, parents)

# NODE 3: sleep node
sleep_possibile_value = ["good", "not good"]
sleep_node_name ="sleep"
parents = [healt_node, stress_node]
children = []
current_value = None
healt_name = healt_node.get_name()
stress_name = stress_node.get_name()
cpt = [                                                                                                 
    {sleep_node_name: 'good', healt_name: 'good', stress_name: 'stressed', 'prob':0.3},
    {sleep_node_name: 'good', healt_name: 'good', stress_name: 'not stressed', 'prob':0.5},
    {sleep_node_name: 'good', healt_name: 'not good', stress_name: 'stressed', 'prob':0.1}, 
    {sleep_node_name: 'good', healt_name: 'not good', stress_name: 'not stressed', 'prob':0.5},
    {sleep_node_name: 'not good', healt_name: 'good', stress_name: 'stressed', 'prob':0.7},
    {sleep_node_name: 'not good', healt_name: 'good', stress_name: 'not stressed', 'prob':0.5},
    {sleep_node_name: 'not good', healt_name: 'not good', stress_name: 'stressed', 'prob':0.9},
    {sleep_node_name: 'not good', healt_name: 'not good', stress_name: 'not stressed', 'prob':0.5}]
sleep_node = BayesianNode(sleep_node_name, possible_value , cpt, current_value, children, parents)




# ---------------------- NODE TEST ----------------------------
healt_node.set_current_state('not good')
stress_node.set_current_state('not stressed')
z = sleep_node.value_generate()
print(z)



# ------------------------- NET TEST --------------------------------
net = Network([sleep_node, stress_node, healt_node])
order_nodes = net.topological_sort()
for node in order_nodes: 
    print(node.get_name())

