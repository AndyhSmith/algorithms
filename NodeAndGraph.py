class Node:
    def __init__(self, data = None):
        self.data = data
        self.neighbors = []
        self.visited = False
        

    def __str__(self):
        return self.data



class Graph:
    def __init__(self):
        pass

    # depth first search iterative
    def dfs_iterative(root_node):
        stack = [root_node]
        while len(stack) != 0:
            node = stack.pop()
            print(node.data)
            for neighbor in node.neighbors:
                stack.append(neighbor)

    # depth first search recursive
    def dfs(root_node):
        print(root_node.data)
        for neighbor in root_node.neighbors:
            Graph.dfs(neighbor)

    # breadth first search
    def bfs(root_node):
        queue = [root_node]
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data)
            for neighbor in node.neighbors:
                queue.append(neighbor)
            


# Tests
# nodeA = Node("a")
# nodeB = Node("b")
# nodeC = Node("c")
# nodeD = Node("d")
# nodeE = Node("e")
# nodeF = Node("f")
# nodeG = Node("g")


# nodeA.neighbors.append(nodeB)
# nodeA.neighbors.append(nodeC)
# nodeB.neighbors.append(nodeD)
# nodeB.neighbors.append(nodeE)
# nodeC.neighbors.append(nodeF)
# nodeC.neighbors.append(nodeG)

# Graph.dfs_iterative(nodeA)
# Graph.dfs(nodeA)
# Graph.bfs(nodeA)