import random
from a2d import Graph
from a3_partb import minimum_spanning_tree


def generate_maze(number_of_rows, number_of_columns):
    rep_walls_of_maz = []
    
    for i in range(number_of_rows * number_of_columns):
        
        if i < (number_of_rows - 1) * number_of_columns:
            rep_walls_of_maz.append((i, i + number_of_columns))
            
        if (i % number_of_columns) != (number_of_columns - 1):
            rep_walls_of_maz.append((i, i + 1))
        
    
    graph = Graph(number_of_rows * number_of_columns)
    
    for cell_1, cell_2 in rep_walls_of_maz:
        weight = random.randint(1, 50)
        graph.add_edge(cell_1, cell_2, weight)
        graph.add_edge(cell_2, cell_1, weight)


    mst = minimum_spanning_tree(graph)

    remove_walls = []
        
    for edge in mst:
        cell_1, cell_2 = edge
        remove_walls.append((min(cell_1, cell_2), max(cell_1, cell_2)))


    rep_walls_of_maz = list(set(rep_walls_of_maz) - set(remove_walls))

    return rep_walls_of_maz