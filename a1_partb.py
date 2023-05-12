class SetList:
    class Node:
        def __init__(self, data=None, set_list=None, next_node=None, prev_node=None):
            self.data = data
            self.set_list = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def get_previous(self):
            return self.prev_node

        def get_set(self):
            return self.set_list


    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def make_set(self, data):
        if self.front is None:
            n_node = self.Node(data, self, None, None)
            self.front = n_node
            self.back = n_node
            return n_node
        else:
            return None

    def union_set(self, other_set):
        
        new_set = other_set.front
        
        while new_set is not None:
            new_set.set_list = self
            new_set = new_set.get_next()
            
        if self.back is None:
            self.front = other_set.front
            self.back = other_set.back
        else:
            self.back.next_node = other_set.front
            self.back = other_set.back
            
            
        other_set.front = None
        other_set.back = None
        return len(other_set)

    def find_data(self, data):
        set_list = self.front
        
        while set_list is not None:
            
            if set_list.get_data() == data:
                return set_list
            
            set_list = set_list.get_next()
        return None

    def representative_node(self):
        return self.front

    def representative(self):
        if self.front is not None:
            return self.front.get_data()
        else:
            return None

    def __len__(self):
        num_of_items = 0
        set_list = self.get_front()
        while (set_list is not None):
            num_of_items = num_of_items + 1
            set_list = set_list.get_next()
        return num_of_items