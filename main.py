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