import random


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
"""