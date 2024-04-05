import random


class Node:
    def __init__(self, node_name, possible_value, cpt, current_value=None, parents=[]):
        self.node_name = node_name
        self.possible_value = possible_value
        self.parents = parents
        self.cpt = cpt
        self.current_value = current_value  # Aggiungo l'attributo per memorizzare lo stato corrente

    def set_parents(self, parents):
        self.parents = parents

    def set_current_state(self, value): 
        self.current_value = value

    def get_name(self):
        return self.node_name

    def get_parents(self):
        return self.parents

    def get_states(self):
        return self.states
     
    def get_current_state(self): 
        return self.current_value
    
    def get_cpt(self): 
        return cpt 

    def get_probability(self, node_state, parent_states):
        return 1
    
    def set_state_probabilistically(self):
        for parent in self.parents(): 
            print(parent)
            print(parent.get_current_state())
        print(self.probabilities)


#OSS: the first values of CPT is always the  first states of the variable itself 

# NODE 1:healt_node.get_name()node
possible_value = ["good", "not good"]
healt_node_name = 'healt'
current_value = None
parents = []
cpt = [{healt_node_name:"good", 'prob': 0.7}, 
       {healt_node_name:'not good', 'prob': 0.7}]
healt_node = Node(healt_node_name, possible_value , cpt, current_value, parents)


# NODE 2: stress node 
possibile_value = ["stressed", "not stressed"]
stress_node_name = 'stress'
current_value = None
parents = [healt_node]
healt_name = healt_node.get_name()
cpt =  [{stress_node_name: "stressed", healt_node_name: 'good', 'prob':0.2}, 
        {stress_node_name: "stressed", healt_node_name: 'not good', 'prob':0.7},
        {stress_node_name: "not stressed", healt_node_name: 'good', 'prob':0.8},
        {stress_node_name: "not stressed", healt_node_name: 'good', 'prob':0.3}]
stress_node = Node(stress_node_name, possible_value , cpt, current_value, parents)


# NODE 3: sleep node
sleep_possibile_value = ["good", "not good"]
sleep_node_name ="sleep"
parents = [healt_node, stress_node]
current_value = None
healt_name = healt_node.get_name()
stress_name = stress_node.get_name()
cpt = [                                                                                                 
    {sleep_node_name: 'good', healt_name: 'good', stress_name: 'stressed', 'prob':0.3},
    {sleep_node_name: 'good', healt_name: 'good', stress_name: 'not stressed', 'prob': 0.5},
    {sleep_node_name: 'good', healt_name: 'not good', stress_name: 'stressed', 'prob':0.1}, 
    {sleep_node_name: 'good', healt_name: 'not good', stress_name: 'not stressed', 'prob': 0.5},
    {sleep_node_name: 'not good', healt_name: 'good', stress_name: 'stressed', 'prob': 0.7},
    {sleep_node_name: 'not good', healt_name: 'good', stress_name: 'not stressed', 'prob': 0.5},
    {sleep_node_name: 'not good', healt_name: 'not good', stress_name: 'stressed', 'prob': 0.9},
    {sleep_node_name: 'not good', healt_name: 'not good', stress_name: 'not stressed', 'prob': 0.5}]
sleep_node = Node(sleep_node_name, possible_value , cpt, current_value, parents)


healt_node.set_current_state('not good')
stress_node.set_current_state('not stressed')

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
print("value:", chiave_scelta)
