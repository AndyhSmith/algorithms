import random
import math

class Node:
    def __init__(self, marbles = None, turn = "player"):
        self.marbles = marbles
        self.neighbors = []
        self.visited = False
        self.turn = turn
        self.best_node = None
        
    def find_best_child(self):
        if self.marbles == 0 and self.turn == "AI":
            self.score = 10
            self.best_child = None
            return

        if self.marbles == 0 and self.turn == "player":
            self.score = -10
            self.best_child = None
            return

        for node in self.neighbors:
            node.find_best_child()

        best_node = None
        best_score = None
        if self.turn == "AI":
            best_score = math.inf
            for node in self.neighbors:
                if node.score < best_score:
                    best_score = node.score
                    best_node = node

        if self.turn == "player":
            best_score = -math.inf
            for node in self.neighbors:
                if node.score > best_score:
                    best_score = node.score
                    best_node = node
        
        self.best_node = best_node
        self.score = best_score


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
            

class MarblesGameAI():
    def __init__(self, num_marbles = 10, max_marbles = 3, first_player = "player"):
        self.num_marbles = num_marbles
        self.max_marbles = max_marbles
        self.first_player = first_player
        self.turn = first_player

        
        print("Loading Game")
        self.create_root_node()
        self.build_game_tree(self.root_node)
        self.root_node.find_best_child()
        self.play()

    def create_root_node(self):
        self.root_node = Node(self.num_marbles)
        self.root_node.turn = self.first_player

    def switch_turn(self, current_turn):
        if current_turn == "player":
            return "AI"
        return "player"

    def build_game_tree(self, node):
        if node.marbles == 0:
            return 
        
        possible_states = []
        for i in range(1, self.max_marbles + 1):
            potential_state = node.marbles - i
            if potential_state >= 0:
                possible_states.append(potential_state)
        
        for state in possible_states:
            new_child = Node(state, self.switch_turn(node.turn))
            node.neighbors.append(new_child)
            if state > 0:
                self.build_game_tree(new_child)

    def turn_player(self, current_node):
        selected_marbles = int(input("How many marbles would you like to pick up?"))
        for node in current_node.neighbors:
            if node.marbles == current_node.marbles - selected_marbles:
                return node
        print("The number of marbles you selected is invalid! Try again!")
        return self.turn_player(current_node)

    def turn_AI(self, current_node):
        # choice = random.choice(current_node.neighbors)
        print(f"The AI has taken {current_node.marbles - current_node.best_node.marbles} marbles.")
        return current_node.best_node


    def play(self):
        print("Welcome to the Marble Game! You are competing against an AI to pick up marbles in a pile. You can only pick up 1 to " + str(self.max_marbles) + " marbles at a time. Whoever picks up the last marble wins!")
        input("Press Enter to Continue...")
        print()
        current_node = self.root_node
        
        while current_node.marbles > 0:
            print("Number of Marbles Remaining: " + str(current_node.marbles))
            if current_node.turn == "player":
                current_node = self.turn_player(current_node)
                if current_node.marbles == 0:
                    print("You have won!")
            elif current_node.turn == "AI":
                current_node = self.turn_AI(current_node)
                if current_node.marbles == 0:
                    print("The AI won!")

            print()

        again = input("Play Again?").lower()
        yes = ["yes", "y", "sure", "ok"]
        if again in yes:
            self.play()


game = MarblesGameAI(10)