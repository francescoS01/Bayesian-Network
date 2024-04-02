class Node:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.probabilities = {}

    def add_parent(self, parent_node):
        self.parents.append(parent_node)

    def add_child(self, child_node):
        self.children.append(child_node)

    def set_probability(self, parents_values, probability):
        self.probabilities[tuple(parents_values)] = probability

    def get_name(self):
        return self.name

    def get_parents(self):
        return self.parents

    def get_children(self):
        return self.children

    def get_probability(self, parents_values):
        return self.probabilities.get(tuple(parents_values), None)

    def __str__(self):
        return f"Node: {self.name}"

# Creazione dei nodi
health_node = Node("Health")
sleep_node = Node("Sleep")
diet_node = Node("Diet")
stress_node = Node("Stress")
mood_node = Node("Mood")
study_time_node = Node("Study Time")
class_attention_node = Node("Class Attention")

# parents definition for every node
sleep_node.add_parent(health_node)
sleep_node.add_parent(stress_node)

diet_node.add_parent(health_node)

stress_node.add_parent(health_node)

mood_node.add_parent(health_node)
mood_node.add_parent(sleep_node)

study_time_node.add_parent(mood_node)

class_attention_node.add_parent(mood_node)
class_attention_node.add_parent(study_time_node)

# Definizione delle probabilità per ogni nodo
health_node.set_probability((), 0.7)

sleep_node.set_probability(("Positivo", "Positivo"), 0.8)
sleep_node.set_probability(("Positivo", "Negativo"), 0.7)
sleep_node.set_probability(("Negativo", "Positivo"), 0.4)
sleep_node.set_probability(("Negativo", "Negativo"), 0.3)

diet_node.set_probability(("Positivo",), 0.8)
diet_node.set_probability(("Negativo",), 0.3)

stress_node.set_probability(("Positivo",), 0.2)
stress_node.set_probability(("Negativo",), 0.7)

mood_node.set_probability(("Positivo", "Positivo"), 0.8)
mood_node.set_probability(("Positivo", "Negativo"), 0.7)
mood_node.set_probability(("Negativo", "Positivo"), 0.4)
mood_node.set_probability(("Negativo", "Negativo"), 0.3)

study_time_node.set_probability(("Positivo",), 0.6)
study_time_node.set_probability(("Negativo",), 0.4)

class_attention_node.set_probability(("Positivo", "Positivo"), 0.7)
class_attention_node.set_probability(("Positivo", "Negativo"), 0.5)
class_attention_node.set_probability(("Negativo", "Positivo"), 0.4)
class_attention_node.set_probability(("Negativo", "Negativo"), 0.2)

# Stampa dei nodi e delle probabilità associate
for node in [health_node, sleep_node, diet_node, stress_node, mood_node, study_time_node, class_attention_node]:
    print(f"{node.get_name()}: {node.probabilities}")

# Output di prova
print("prova")
