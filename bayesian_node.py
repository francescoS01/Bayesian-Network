import random
from typing import List

class BayesianNode:
    def __init__(self, node_name, possible_value, cpt, current_value=None, children=[], parents=[]):
        self.node_name = node_name
        self.possible_value = possible_value
        self.children = children
        self.parents = parents
        self.cpt = cpt
        self.current_value = current_value  # Aggiungo l'attributo per memorizzare lo stato corrente
        self.children_update()  # Chiamata al metodo update al momento dell'inizializzazione

    def children_update(self):
        for parent in self.parents:
            parent.set_children(self)

    def set_children(self, new_child: 'BayesianNode'):
        self.children.append(new_child)

    def set_parents(self, parents):
        self.parents = parents

    def set_current_state(self, value): 
        self.current_value = value

    def get_name(self):
        return self.node_name

    def get_parents(self):
        return self.parents
    
    def get_children(self): 
        return self.children
     
    def get_current_state(self): 
        return self.current_value
    
    def get_cpt(self): 
        return self.cpt 
    
    def value_generate(self):
        # create a dictionary with paretns and them value
        parent_value_dict = {}
        for parent in self.parents :
            parent_name = parent.get_name()
            value = parent.get_current_state()
            parent_value_dict[parent_name] = value
        
        # create a dictionary of probability fo self node knowing parents and them values 
        probability_distribution = {}
        for value in self.possible_value:
            new = parent_value_dict.copy()
            new[self.node_name] = value
            for dict in self.cpt: 
                new['prob'] = dict['prob']
                if dict == new:
                    probability_distribution[value] = dict['prob']
        
        # foloowing the probility, extract one value of the self node 
        numero_random = random.random() # 0 -1 
        accumulate = 0
        for key, prob in probability_distribution.items():
            accumulate += prob
            if accumulate >= numero_random:
                self.current_value = key
                return key