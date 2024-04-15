import random
from typing import List
from bayesian_node import *
from network import *

#OSS: the first values of CPT is always the  first states of the variable itself 

# ---------------------- NODE CREATION ----------------------------

# NODE 1: Nutrition node
nutr_possible_value = ["good", "not good"]
nutr_name ="nutrition"
parents = []
children = []
current_value = None
cpt = [                                                                                                 
    {nutr_name: 'good', 'prob':0.5},
    {nutr_name: 'not good', 'prob':0.5}]
nutr_node = BayesianNode(nutr_name, nutr_possible_value , cpt, current_value, children, parents)



# NODE 2: physical exercise node
pysicalex_possible_value = ['good', 'not good']
pysicalex_name = 'pysical exercise'
parents = []
children = []
current_value = None
cpt = [                                                                                                 
    {pysicalex_name: 'good', 'prob':0.6},
    {pysicalex_name: 'not good', 'prob':0.4}]
pysicalex_node = BayesianNode(pysicalex_name, pysicalex_possible_value , cpt, current_value, children, parents)



# NODE 3: healt node
healt_possibile_value = ['good', 'not good']
healt_name = 'healt'
parents = [nutr_node, pysicalex_node]
children = []
current_value = None
nutr_name = nutr_node.get_name()
pysicalex_name = pysicalex_node.get_name()
cpt = [                                                                                                 
    {healt_name: 'good', nutr_name: 'good', pysicalex_name: 'good', 'prob':0.8},
    {healt_name: 'good', nutr_name: 'good', pysicalex_name: 'not good', 'prob':0.7},
    {healt_name: 'good', nutr_name: 'not good', pysicalex_name: 'good', 'prob':0.6}, 
    {healt_name: 'good', nutr_name: 'not good', pysicalex_name: 'not good', 'prob':0.3},
    {healt_name: 'not good', nutr_name: 'good', pysicalex_name: 'good', 'prob':0.2},
    {healt_name: 'not good', nutr_name: 'good', pysicalex_name: 'not good', 'prob':0.3},
    {healt_name: 'not good', nutr_name: 'not good', pysicalex_name: 'good', 'prob':0.4},
    {healt_name: 'not good', nutr_name: 'not good', pysicalex_name: 'not good', 'prob':0.7}]
healt_node = BayesianNode(healt_name, healt_possibile_value, cpt, current_value, children, parents)



# NODE 4: stress node
stress_possibile_value = ['high', 'not high']
stress_name = 'stress'
parents = [healt_node]
children = []
current_value = None
healt_name = healt_node.get_name()
cpt = [                                                                                                 
    {stress_name: 'high', healt_name: 'good', 'prob':0.4},
    {stress_name: 'high', healt_name: 'not good', 'prob':0.8},
    {stress_name: 'not high', healt_name: 'good', 'prob':0.6}, 
    {stress_name: 'not high', healt_name: 'not good', 'prob':0.2}]
stress_node = BayesianNode(stress_name, stress_possibile_value, cpt, current_value, children, parents)



# NODE 5: recovery node
recovery_possibile_value = ['good', 'not good']
recovery_name = 'recovery'
parents = [stress_node]
children = []
current_value = None
stress_name = stress_node.get_name()
cpt = [                                                                                                 
    {recovery_name: 'good', stress_name: 'high', 'prob':0.2},
    {recovery_name: 'good', stress_name: 'not high', 'prob':0.7},
    {recovery_name: 'not good', stress_name: 'high', 'prob':0.8}, 
    {recovery_name: 'not good', stress_name: 'not high', 'prob':0.3}]
recovery_node = BayesianNode(recovery_name, recovery_possibile_value, cpt, current_value, children, parents)



# NODE 6: mood node
mood_possibile_value = ['good', 'not good']
mood_name = 'mood'
parents = [stress_node]
children = []
current_value = None
stress_name = stress_node.get_name()
cpt = [                                                                                                 
    {mood_name: 'good', stress_name: 'high', 'prob':0.2},
    {mood_name: 'good', stress_name: 'not high', 'prob':0.7},
    {mood_name: 'not good', stress_name: 'high', 'prob':0.8}, 
    {mood_name: 'not good', stress_name: 'not high', 'prob':0.3}]
mood_node = BayesianNode(mood_name, mood_possibile_value, cpt, current_value, children, parents)



# NODE 7: energy node
energy_possibile_value = ['high', 'not high']
energy_name = 'energy'
parents = [recovery_node, nutr_node]
children = []
current_value = None
recovery_name = recovery_node.get_name()
nutr_name = nutr_node.get_name()
cpt = [                                                                                                 
    {energy_name: 'high', nutr_name: 'good', recovery_name: 'good', 'prob':0.9},
    {energy_name: 'high', nutr_name: 'good', recovery_name: 'not good', 'prob':0.5},
    {energy_name: 'high', nutr_name: 'not good', recovery_name: 'good', 'prob':0.6}, 
    {energy_name: 'high', nutr_name: 'not good', recovery_name: 'not good', 'prob':0.1},
    {energy_name: 'not high', nutr_name: 'good', recovery_name: 'good', 'prob':0.1},
    {energy_name: 'not high', nutr_name: 'good', recovery_name: 'not good', 'prob':0.4},
    {energy_name: 'not high', nutr_name: 'not good', recovery_name: 'good', 'prob':0.9},
    {energy_name: 'not high', nutr_name: 'not good', recovery_name: 'not good', 'prob':0.9}]
energy_node = BayesianNode(energy_name, energy_possibile_value, cpt, current_value, children, parents)



# NODE 8: productivity node
prod_possibile_value = ['high', 'not high']
prod_name = 'productivity'
parents = [energy_node, mood_node]
children = []
current_value = None
energy_name = energy_node.get_name()
mood_name = mood_node.get_name()
cpt = [                                                                                                 
    {prod_name: 'high', energy_name: 'high', mood_name: 'good', 'prob':0.8},
    {prod_name: 'high', energy_name: 'high', mood_name: 'not good', 'prob':0.6},
    {prod_name: 'high', energy_name: 'not high', mood_name: 'good', 'prob':0.6}, 
    {prod_name: 'high', energy_name: 'not high', mood_name: 'not good', 'prob':0.2},
    {prod_name: 'not high', energy_name: 'high', mood_name: 'good', 'prob':0.2},
    {prod_name: 'not high', energy_name: 'high', mood_name: 'not good', 'prob':0.4},
    {prod_name: 'not high', energy_name: 'not high', mood_name: 'good', 'prob':0.4},
    {prod_name: 'not high', energy_name: 'not high', mood_name: 'not good', 'prob':0.8}]
productivity_node = BayesianNode(prod_name, prod_possibile_value, cpt, current_value, children, parents)



# NODE 9: wellness node
wellness_possibile_value = ['high', 'not high']
wellness_name = 'wellness'
parents = [pysicalex_node, mood_node]
children = []
current_value = None
pysicalex_name = pysicalex_node.get_name()
mood_name = mood_node.get_name()
cpt = [                                                                                                 
    {wellness_name: 'high', pysicalex_name: 'good', mood_name: 'good', 'prob':0.8},
    {wellness_name: 'high', pysicalex_name: 'good', mood_name: 'not good', 'prob':0.6},
    {wellness_name: 'high', pysicalex_name: 'not good', mood_name: 'good', 'prob':0.6}, 
    {wellness_name: 'high', pysicalex_name: 'not good', mood_name: 'not good', 'prob':0.2},
    {wellness_name: 'not high', pysicalex_name: 'good', mood_name: 'good', 'prob':0.2},
    {wellness_name: 'not high', pysicalex_name: 'good', mood_name: 'not good', 'prob':0.4},
    {wellness_name: 'not high', pysicalex_name: 'not good', mood_name: 'good', 'prob':0.4},
    {wellness_name: 'not high', pysicalex_name: 'not good', mood_name: 'not good', 'prob':0.8}]
wellness_node = BayesianNode(wellness_name, wellness_possibile_value, cpt, current_value, children, parents)





# ---------------------- NODE TEST ----------------------------
nutr_node.set_current_state('good')
pysicalex_node.set_current_state('good')
#healt_node.set_current_state('not good')
z = healt_node.value_generate()


mood_node.set_current_state('good')
pysicalex_node.set_current_state('good')
#healt_node.set_current_state('not good')
z = wellness_node.value_generate()



# ------------------------- NET TEST --------------------------------
net = Network([mood_node, nutr_node, healt_node, energy_node, pysicalex_node, stress_node, recovery_node, productivity_node , wellness_node])
x = net.sampling_create()
print(x)
