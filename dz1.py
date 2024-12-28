import networkx as nx

def create_graph():
    G = nx.DiGraph()

    # Add edges with capacities
    edges = [
        ('Terminal 1', 'Warehouse 1', 25),
        ('Terminal 1', 'Warehouse 2', 20),
        ('Terminal 1', 'Warehouse 3', 15),
        ('Terminal 2', 'Warehouse 3', 15),
        ('Terminal 2', 'Warehouse 4', 30),
        ('Terminal 2', 'Warehouse 2', 10),
        ('Warehouse 1', 'Shop 1', 15),
        ('Warehouse 1', 'Shop 2', 10),
        ('Warehouse 1', 'Shop 3', 20),
        ('Warehouse 2', 'Shop 4', 15),
        ('Warehouse 2', 'Shop 5', 10),
        ('Warehouse 2', 'Shop 6', 25),
        ('Warehouse 3', 'Shop 7', 20),
        ('Warehouse 3', 'Shop 8', 15),
        ('Warehouse 3', 'Shop 9', 10),
        ('Warehouse 4', 'Shop 10', 20),
        ('Warehouse 4', 'Shop 11', 10),
        ('Warehouse 4', 'Shop 12', 15),
        ('Warehouse 4', 'Shop 13', 5),
        ('Warehouse 4', 'Shop 14', 10)
    ]

    G.add_weighted_edges_from(edges, weight='capacity')
    return G

def compute_max_flow(G, source, sink):
    flow_value, flow_dict = nx.maximum_flow(G, source, sink, capacity='capacity')
    return flow_value, flow_dict

def main():
    # Create the graph
    G = create_graph()

    # Add a super-source and super-sink
    G.add_node('Super Source')
    G.add_node('Super Sink')

    # Connect super-source to terminals and shops to super-sink
    G.add_edge('Super Source', 'Terminal 1', capacity=100)
    G.add_edge('Super Source', 'Terminal 2', capacity=100)

    for shop in ['Shop 1', 'Shop 2', 'Shop 3', 'Shop 4', 'Shop 5', 'Shop 6', 'Shop 7', 'Shop 8', 'Shop 9', 'Shop 10', 'Shop 11', 'Shop 12', 'Shop 13', 'Shop 14']:
        G.add_edge(shop, 'Super Sink', capacity=100)

    # Compute maximum flow
    max_flow, flow_dict = compute_max_flow(G, 'Super Source', 'Super Sink')

    # Display results
    print(f"Maximum flow from Super Source to Super Sink: {max_flow}")
    print("Flow distribution:")
    for u, v_dict in flow_dict.items():
        for v, flow in v_dict.items():
            if flow > 0:
                print(f"{u} -> {v}: {flow}")

if __name__ == "__main__":
    main()

# Maximum flow from Super Source to Super Sink: 115
# Flow distribution:
# Terminal 1 -> Warehouse 1: 25
# Terminal 1 -> Warehouse 2: 20
# Terminal 1 -> Warehouse 3: 15
# Warehouse 1 -> Shop 1: 15
# Warehouse 1 -> Shop 2: 10
# Warehouse 2 -> Shop 4: 15
# Warehouse 2 -> Shop 5: 10
# Warehouse 2 -> Shop 6: 5
# Warehouse 3 -> Shop 7: 20
# Warehouse 3 -> Shop 8: 10
# Terminal 2 -> Warehouse 3: 15
# Terminal 2 -> Warehouse 4: 30
# Terminal 2 -> Warehouse 2: 10
# Warehouse 4 -> Shop 10: 20
# Warehouse 4 -> Shop 11: 10
# Shop 1 -> Super Sink: 15
# Shop 2 -> Super Sink: 10
# Shop 4 -> Super Sink: 15
# Shop 5 -> Super Sink: 10
# Shop 6 -> Super Sink: 5
# Shop 7 -> Super Sink: 20
# Shop 8 -> Super Sink: 10
# Shop 10 -> Super Sink: 20
# Shop 11 -> Super Sink: 10
# Super Source -> Terminal 1: 60
# Super Source -> Terminal 2: 55

# Які термінали забезпечують найбільший потік товарів до магазинів? 
# Найбільший потік забезпечує той термінал, 
# який має найбільше з'єднань із складами з високою пропускною здатністю. 
# Аналіз результатів програми покаже, які саме термінали є такими.

# Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік? 
# Найменші пропускні здатності обмежують загальний потік, створюючи «вузькі місця». 
# Їх легко знайти, аналізуючи результати потоків у графі.

# Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів? 
# Магазини з найменшим обсягом постачання можна визначити за потоком до них. 
# Збільшення пропускної здатності на певних маршрутах 
# (наприклад, від складів до магазинів) може вирішити проблему.

# Чи є вузькі місця, які можна усунути для покращення ефективності логістичної мережі? 
# Такі місця можна ідентифікувати в графі за допомогою аналізу залишкової пропускної здатності. 
# Усунення вузьких місць, наприклад, за рахунок збільшення пропускної здатності або додавання нових маршрутів, 
# покращить ефективність.