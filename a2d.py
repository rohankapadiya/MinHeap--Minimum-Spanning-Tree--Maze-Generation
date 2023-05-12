class Graph:
    def __init__(self, number_of_verts):
        self.graph_obj = [[] for _ in range(number_of_verts)]
    
    def add_vertex(self):
        self.graph_obj.append([])
    
    def add_edge(self, from_idx, to_idx, weight=1):
        if len(self.graph_obj) <= from_idx or len(self.graph_obj) <= to_idx:
            return False
        
        for vertex, i in self.graph_obj[from_idx]:
            if vertex  == to_idx:
                return False
            
        self.graph_obj[from_idx].append((to_idx, weight))
        return True
    
    def num_edges(self):
        cnt = 0
        for i in self.graph_obj:
            cnt += len(i)
            
        return cnt
    
    def num_verts(self):
        return len(self.graph_obj)
    
    def has_edge(self, from_idx, to_idx):
        if len(self.graph_obj) <= from_idx or len(self.graph_obj) <= to_idx:
            return False
        
        for vertex, i in self.graph_obj[from_idx]:
            if vertex == to_idx:
                return True
            
        return False
    
    def edge_weight(self, from_idx, to_idx):
        if len(self.graph_obj) <= from_idx or len(self.graph_obj) <= to_idx:
            return None
        
        for vertex, i in self.graph_obj[from_idx]:
            if vertex == to_idx:
                return i
            
        return None
    
    def get_connected(self, v):
        if v >= len(self.graph_obj):
            return []
        
        return [(index, weight) for index, weight  in self.graph_obj[v]]
