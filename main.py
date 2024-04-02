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

# Aggiunta dei nodi alla rete bayesiana
bayesian_network = BayesianNetwork()
bayesian_network.add_node(health_node)
bayesian_network.add_node(sleep_node)
bayesian_network.add_node(diet_node)
bayesian_network.add_node(stress_node)
bayesian_network.add_node(mood_node)
bayesian_network.add_node(study_time_node)
bayesian_network.add_node(class_attention_node)

print("prova")