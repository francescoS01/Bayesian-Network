import random


class Node:
    def __init__(self, name, states=["Positive", "Negative"], parents=[], probabilities={}):
        self.name = name
        self.states = states
        self.parents = parents
        self.probabilities = probabilities
        self.current_state = None  # Aggiungo l'attributo per memorizzare lo stato corrente

    def set_parents(self, parents):
        self.parents = parents

    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
    
    def set_current_state(self, value): 
        self_current_state = value

    def get_name(self):
        return self.name

    def get_parents(self):
        return self.parents

    def get_states(self):
        return self.states
     
    def get_current_state(self): 
        return  self.current_state

    def get_probability(self, node_state, parent_states):
        parent_key = tuple(sorted(parent_states.items()))
        probability = self.probabilities[node_state][parent_key]
        return probability

    def get_probability_by_values(self, node_value, parent_values):
        parent_key = tuple(sorted(parent_values.items()))
        probability = self.probabilities[node_value][parent_key]
        return probability
    
    def set_state_probabilistically(self):
        for parent in self.parents(): 
            print(parent)
            print(parent.get_current_state())
        print(self.probabilities)

# node 1
health_node = Node(name="Health", probabilities={
    "Positive": {
        (): 0.7,
    }
})

# node 2
sleep_node = Node(name="Sleep", parents=["Health", "Stress"], probabilities= {
    "Positive": {
        (("Health", "Positive"), ("Stress", "Positive")): 0.8,
        (("Health", "Positive"), ("Stress", "Negative")): 0.7,
        (("Health", "Negative"), ("Stress", "Positive")): 0.4,
        (("Health", "Negative"), ("Stress", "Negative")): 0.3,
    }
})

# node 3
diet_node = Node(name="Diet", parents=["Health"], probabilities={
    "Positive": {
        (("Health", "Positive"),): 0.8,
        (("Health", "Negative"),): 0.3,
    }
})

# node 4
stress_node = Node(name="Stress", parents=["Health"], probabilities={
    "Positive": {
        (("Health", "Positive"),): 0.2,
        (("Health", "Negative"),): 0.7,
    }
})

# node 5
mood_node = Node(name="Mood", parents=["Health", "Sleep"], probabilities={
    "Positive": {
        (("Health", "Positive"), ("Sleep", "Positive")): 0.8,
        (("Health", "Positive"), ("Sleep", "Negative")): 0.7,
        (("Health", "Negative"), ("Sleep", "Positive")): 0.4,
        (("Health", "Negative"), ("Sleep", "Negative")): 0.3,
    }
})

# node 6
study_time_node = Node(name="Study Time", parents=["Mood"], probabilities={
    "Positive": {
        (("Mood", "Positive"),): 0.6,
        (("Mood", "Negative"),): 0.3,
    }
})

# node 7
class_attention_node = Node(name="Class Attention", parents=["Mood", "Study Time"], probabilities={
    "Positive": {
        (("Mood", "Positive"), ("Study Time", "Positive")): 0.7,
        (("Mood", "Positive"), ("Study Time", "Negative")): 0.5,
        (("Mood", "Negative"), ("Study Time", "Positive")): 0.4,
        (("Mood", "Negative"), ("Study Time", "Negative")): 0.2,
    }
})

# node 8
workload_node = Node(
    name="Workload",
    states=["Positive", "Negative"],
    parents=["Stress"],
    probabilities={
        "Positive": {
            (("Stress", "Positive"),): 0.8,
            (("Stress", "Negative"),): 0.4,
        }
    }
)

# node 9
interest_study_node = Node(
    name="Interest",
    states=["Positive", "Negative"],
    parents=["Mood"],
    probabilities={
        "Positive": {
            (("Mood", "Positive"),): 0.6,
            (("Mood", "Negative"),): 0.3,
        }
    }
)

# node 10
study_frequency_node = Node(
    name="Study Frequency",
    states=["Positive", "Negative"],
    parents=["Interest"],
    probabilities={
        "Positive": {
            (("Interest", "Positive"),): 0.7,
            (("Interest", "Negative"),): 0.3,
        }
    }
)

# Esempio di utilizzo
# Imposta lo stato del nodo health_node in modo probabilistico
health_node.set_state_probabilistically()
health_node.set_current_state('Positive')
stress_node.set_state_probabilistically()


# ---------------------------- MAIN2 ----------------------
import random
from typing import List

class Node:
    def __init__(self, sleep_name, possible_value, cpt, current_value=None, parents=[]):
        self.sleep_name = sleep_name
        self.possible_value = possible_value
        self.parents = parents
        self.cpt = cpt
        self.current_value = current_value  # Aggiungo l'attributo per memorizzare lo stato corrente

    def set_parents(self, parents):
        self.parents = parents

    def set_current_state(self, value): 
        self.current_value = value

    def get_name(self):
        return self.sleep_name

    def get_parents(self):
        return self.parents
     
    def get_current_state(self): 
        return self.current_value
    
    def get_cpt(self): 
        return cpt 
    
    def set_state_probabilistically(self):
        for parent in self.parents(): 
            print(parent)
            print(parent.get_current_state())
        print(self.probabilities)


class Netowork:
    def __init__(self, nodes:List[Node]):
        self.net_nodes = nodes

        
    def topological_sort(self):
        visited = []
        parents_count = {node: 0 for node in self.net_nodes}

        # Conta i genitori di ciascun nodo
        for node in self.net_nodes:
            for parent in node.get_parents():
                parents_count[parent] += 1

        # Trova i nodi senza genitori
        no_parents = [node for node in self.net_nodes if parents_count[node] == 0]

        # Itera sui nodi senza genitori e visita i loro figli
        
        while no_parents:
            print(2)
            node = no_parents.pop(0)
            visited.append(node)
            for child in node.children:
                parents_count[child] -= 1
                if parents_count[child] == 0:
                    no_parents.append(child)


        return visited
        






#OSS: the first values of CPT is always the  first states of the variable itself 

# NODE 1:healt_node.get_name()node
possible_value = ["good", "not good"]
healt_node_name = 'healt'
current_value = None
parents = []

cpt = {0.7: {healt_node_name:"good"}, 
       0.3: {healt_node_name:'not good'}}
healt_node = Node(healt_node_name, possible_value , cpt, current_value, parents)


# NODE 2: stress node 
possibile_value = ["stressed", "not stressed"]
stress_node_name = 'stress'
current_value = None
parents = [healt_node]
healt_name = healt_node.get_name()
cpt =  {0.2: {stress_node_name: "stressed", healt_node_name: 'good'}, 
        0.7: {stress_node_name: "stressed", healt_node_name: 'not good'},
        0.8: {stress_node_name: "not stressed", healt_node_name: 'good'},
        0.3: {stress_node_name: "not stressed", healt_node_name: 'good'}}
stress_node = Node(stress_node_name, possible_value , cpt, current_value, parents)


# prova 
"""
cpt_stress = stress_node.get_cpt()
for chiave, valore in cpt_stress.items():
    print(valore) 
"""



# NODE 3: sleep node
possibile_value = ["good", "not good"]
sleep_name ="sleep"
parents = [healt_node, stress_node]
current_value = None
cpt = { 0.3: {sleep_name: 'good', healt_node.get_name(): 'good', stress_node.get_name():'stressed'}, 
        0.5: {sleep_name: 'good', healt_node.get_name(): 'good', stress_node.get_name():'not stressed'}, 
        0.1: {sleep_name: 'good', healt_node.get_name(): 'not good', stress_node.get_name():'stressed'}, 
        0.3: {sleep_name: 'good', healt_node.get_name(): 'not good', stress_node.get_name():'not stressed'},
        0.7: {sleep_name: 'not good', healt_node.get_name(): 'good', stress_node.get_name():'stressed'},
        0.5: {sleep_name: 'not good', healt_node.get_name(): 'good', stress_node.get_name():'not stressed'}, 
        0.9: {sleep_name: 'not good', healt_node.get_name(): 'not good', stress_node.get_name():'stressed'}, 
        0.7: {sleep_name: 'not good', healt_node.get_name(): 'not good', stress_node.get_name():'not stressed'}}
sleep_node = Node(sleep_name, possible_value , cpt, current_value, parents)


healt_node.set_current_state('good')
stress_node.set_current_state('not stressed')



current = {}
parents = sleep_node.get_parents()
for parent in parents :
   parent_name = parent.get_name()
   value = parent.get_current_state()
   #print(value)
   current[parent_name]=value
cpt_sleep = sleep_node.get_cpt()

#print(current)

probability_distribution = {}

for value in possibile_value:
    print(value)
    new = current.copy()
    new[sleep_name] = value
    #chiave = [chiave for chiave, valore in cpt_sleep.items() if valore == new][0]
    for chiave, value2 in cpt_sleep.items(): 
        if value2 == new:
            print(1)
            probability_distribution[value] = chiave

print(probability_distribution)


def scegli_chiave(prob_dict):
    # Genera un numero casuale tra 0 e 1
    numero_random = random.random()
    
    # Inizializza la variabile per accumulare la probabilità
    accumulato = 0
    
    # Itera attraverso il dizionario
    for chiave, probabilita in prob_dict.items():
        # Aggiungi la probabilità corrente all'accumulatore
        accumulato += probabilita
        
        # Se l'accumulatore supera o è uguale al numero casuale generato,
        # restituisci la chiave corrispondente
        if accumulato >= numero_random:
            return chiave

# Esempio di utilizzo


# Esegui la funzione per scegliere una chiave
chiave_scelta = scegli_chiave(probability_distribution)
print("Chiave scelta:", chiave_scelta)


net = Netowork([sleep_node, stress_node, healt_node])
net.topological_sort()





"""


# node 2
sleep_node = Node(sleep_name="Sleep", parents=["Health", "Stress"], probabilities= {
    "Positive": {
        (("Health", "Positive"), ("Stress", "Positive")): 0.8,
        (("Health", "Positive"), ("Stress", "Negative")): 0.7,
        (("Health", "Negative"), ("Stress", "Positive")): 0.4,
        (("Health", "Negative"), ("Stress", "Negative")): 0.3,
    }
})

#  def __init__(self, sleep_name, possible_value, cpt, current_value=None, parents=[]):
# node 2
possible_value = ["good", "not good"]
sleep_name = 'sleep'
current_value = None
parents = [health_node]

# creo cpt 
cpt = { {}}
sleep_node = Node(sleep_name, possible_value , cpt, current_value, parents)

# node 3
diet_node = Node(sleep_name="Diet", parents=["Health"], probabilities={
    "Positive": {
        (("Health", "Positive"),): 0.8,
        (("Health", "Negative"),): 0.3,
    }
})

# node 4
stress_node = Node(sleep_name="Stress", parents=["Health"], probabilities={
    "Positive": {
        (("Health", "Positive"),): 0.2,
        (("Health", "Negative"),): 0.7,
    }
})

# node 5
mood_node = Node(sleep_name="Mood", parents=["Health", "Sleep"], probabilities={
    "Positive": {
        (("Health", "Positive"), ("Sleep", "Positive")): 0.8,
        (("Health", "Positive"), ("Sleep", "Negative")): 0.7,
        (("Health", "Negative"), ("Sleep", "Positive")): 0.4,
        (("Health", "Negative"), ("Sleep", "Negative")): 0.3,
    }
})

# node 6
study_time_node = Node(sleep_name="Study Time", parents=["Mood"], probabilities={
    "Positive": {
        (("Mood", "Positive"),): 0.6,
        (("Mood", "Negative"),): 0.3,
    }
})

# node 7
class_attention_node = Node(sleep_name="Class Attention", parents=["Mood", "Study Time"], probabilities={
    "Positive": {
        (("Mood", "Positive"), ("Study Time", "Positive")): 0.7,
        (("Mood", "Positive"), ("Study Time", "Negative")): 0.5,
        (("Mood", "Negative"), ("Study Time", "Positive")): 0.4,
        (("Mood", "Negative"), ("Study Time", "Negative")): 0.2,
    }
})

# node 8
workload_node = Node(
    sleep_name="Workload",
    states=["Positive", "Negative"],
    parents=["Stress"],
    probabilities={
        "Positive": {
            (("Stress", "Positive"),): 0.8,
            (("Stress", "Negative"),): 0.4,
        }
    }
)

# node 9
interest_study_node = Node(
    sleep_name="Interest",
    states=["Positive", "Negative"],
    parents=["Mood"],
    probabilities={
        "Positive": {
            (("Mood", "Positive"),): 0.6,
            (("Mood", "Negative"),): 0.3,
        }
    }
)

# node 10
study_frequency_node = Node(
    sleep_name="Study Frequency",
    states=["Positive", "Negative"],
    parents=["Interest"],
    probabilities={
        "Positive": {
            (("Interest", "Positive"),): 0.7,
            (("Interest", "Negative"),): 0.3,
        }
    }
)

# Esempio di utilizzo
# Imposta lo stato del nodo health_node in modo probabilistico
health_node.set_state_probabilistically()
health_node.set_current_state('Positive')
stress_node.set_state_probabilistically()



--------------------------------------------------

parent_value_dict = {}
parents = sleep_node.get_parents()
# prendo un dizionario = {genitore1_name: fixed_value, genitore2_name: fixed_value, ... }
for parent in parents :
   parent_name = parent.get_name()
   value = parent.get_current_state()
   #print(value)
   parent_value_dict[parent_name]=value
cpt_sleep = sleep_node.get_cpt()


probability_distribution = {}

# scorro possibili valori del nodo corrente 
for value in sleep_possibile_value:
    new = parent_value_dict.copy()
    new[sleep_node_name] = value
    #chiave = [chiave for chiave, valore in cpt_sleep.items() if valore == new][0]
    for dict in cpt_sleep: 
        new['prob'] = dict['prob']
        if dict == new:
            probability_distribution[value] = dict['prob']




def scegli_chiave(prob_dict):
    # Genera un numero casuale tra 0 e 1
    numero_random = random.random()
    
    # Inizializza la variabile per accumulare la probabilità
    accumulate = 0
    
    # Itera attraverso il dizionario
    for chiave, probabilita in prob_dict.items():
        # Aggiungi la probabilità corrente all'accumulatore
        accumulate += probabilita
        
        # Se l'accumulatore supera o è uguale al numero casuale generato,
        # restituisci la chiave corrispondente
        if accumulate >= numero_random:
            return chiave
"""



# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""
class Node:
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

    def set_children(self, new_child: 'Node'):
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
        return cpt 
    

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







---------------------------------------------------------------



# NODE 4: healt node
possible_value = ["good", "not good"]
healt_node_name = 'healt'
current_value = None
parents = []
children = []
cpt = [{healt_node_name:"good", 'prob': 0.7}, 
       {healt_node_name:'not good', 'prob': 0.7}]
healt_node = BayesianNode(healt_node_name, possible_value , cpt, current_value, children, parents)

# NODE 5: stress node 
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
nutr_node_name ="sleep"
parents = [healt_node, stress_node]
children = []
current_value = None
healt_name = healt_node.get_name()
stress_name = stress_node.get_name()
cpt = [                                                                                                 
    {nutr_node_name: 'good', healt_name: 'good', stress_name: 'stressed', 'prob':0.3},
    {nutr_node_name: 'good', healt_name: 'good', stress_name: 'not stressed', 'prob':0.5},
    {nutr_node_name: 'good', healt_name: 'not good', stress_name: 'stressed', 'prob':0.1}, 
    {nutr_node_name: 'good', healt_name: 'not good', stress_name: 'not stressed', 'prob':0.5},
    {nutr_node_name: 'not good', healt_name: 'good', stress_name: 'stressed', 'prob':0.7},
    {nutr_node_name: 'not good', healt_name: 'good', stress_name: 'not stressed', 'prob':0.5},
    {nutr_node_name: 'not good', healt_name: 'not good', stress_name: 'stressed', 'prob':0.9},
    {nutr_node_name: 'not good', healt_name: 'not good', stress_name: 'not stressed', 'prob':0.5}]
sleep_node = BayesianNode(nutr_node_name, possible_value , cpt, current_value, children, parents)

# NODE 4: diet node 
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



"""