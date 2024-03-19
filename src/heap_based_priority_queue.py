class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self._go_up(len(self.heap) - 1)

    def delete_root(self):
        max_priority_node = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._go_down(0)
        return max_priority_node.value

    def show(self):
        if not self.heap:
            return None
        return [node.value for node in self.heap]

    def _go_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[parent_index].priority < self.heap[index].priority:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _go_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            if left_child_index >= len(self.heap):
                break
            right_child_index = 2 * index + 2
            largest = left_child_index
            if (right_child_index < len(self.heap) and self.heap[right_child_index].priority
                    > self.heap[left_child_index].priority):
                largest = right_child_index
            if self.heap[largest].priority > self.heap[index].priority:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break
