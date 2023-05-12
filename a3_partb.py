from a3_parta import MinHeap

def minimum_spanning_tree(graph):
    mst = []
    is_curr_visited = set()
    new_heap = MinHeap([(0, 0, None)]) 
    
    while not new_heap.is_empty():
        weight, current, previous = new_heap.extract_min()
        
        if current in is_curr_visited:
            continue
        
        is_curr_visited.add(current)
        
        if previous is not None:
            mst.append((previous, current))
            
        for neighbor, weight in graph.graph_obj[current]:
            if neighbor not in is_curr_visited:
                new_heap.insert((weight, neighbor, current))
                
    return mst