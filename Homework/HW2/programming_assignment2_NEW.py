# # class Anagram:
# #     num_iterations = 0
# #     def anagram_expand(self, state, goal):
# #         node_list = []

# #         for pos in range(1, len(state)):  # Create each possible state that can be created from the current one in a single step
# #             new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

# #             # TO DO: c. Very simple h' function - please improve!
# #             if new_state == goal:
# #                 score = 0
# #             else:
# #                 score = 1

# #             node_list.append((new_state, score))

# #         return node_list

# #     # TO DO: b. Return either the solution as a list of states from start to goal or [] if there is no solution.
# #     def a_star(self, start, goal, expand):


# # #         return []


# # #     # Finds a solution, i.e., the set of steps from one word to its anagram
# # #     def solve(self,start, goal):

# # #         self.num_iterations = 0

# # #         # TO DO: a. Add code below to check in advance whether the problem is solvable

# # #         # if ...
# # #         #    print('This is impossible to solve')
# # #         #    return "IMPOSSIBLE"

# # #         self.solution = self.a_star(start, goal, self.anagram_expand)

# # #         if not self.solution:
# # #             print('No solution found')
# # #             return "NONE"

# # #         print(str(len(self.solution) - 1) + ' steps from start to goal:')

# # #         for step in self.solution:
# # #             print(step)

# # #         print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')

# # #         return str(self.num_iterations)



# # # if __name__ == '__main__':
# # #     anagram = Anagram()
# # #     anagram.solve('TEARDROP', 'PREDATOR')







# # from queue import PriorityQueue

# # def heuristic(word, goal):
# #     # Calculate the heuristic by counting the number of correct positions
# #     return sum(1 for w, g in zip(word, goal) if w == g)

# # def a_star(start, goal):
# #     visited = set()
# #     pq = PriorityQueue()
# #     pq.put((0, start))
    
# #     while not pq.empty():
# #         steps, current_word = pq.get()
        
# #         if current_word == goal:
# #             return steps
        
# #         if current_word in visited:
# #             continue
        
# #         visited.add(current_word)
        
# #         for i in range(len(current_word)):
# #             for j in range(len(current_word)):
# #                 if i != j:
# #                     # Generate a new word by moving the first letter to a different position
# #                     new_word = list(current_word)
# #                     new_word.insert(j, new_word.pop(i))
# #                     new_word = ''.join(new_word)
                    
# #                     if new_word not in visited:
# #                         pq.put((steps + 1 + heuristic(new_word, goal), new_word))
    
# #     return -1  # If no solution is found

# # start_word = "TEARDROP"
# # goal_word = "PREDATOR"
# # min_steps = a_star(start_word, goal_word)
# # print(f"Minimum steps to transform '{start_word}' into '{goal_word}': {min_steps}")



# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# # import heapq  # for priority queue

# # class Anagram:
# #     num_iterations = 0
    
# #     def anagram_expand(self, state, goal):
# #         node_list = []

# #         for pos in range(1, len(state)):
# #             new_state = state[1:pos + 1] + state[0] + state[pos + 1:]
            
# #             # Improved heuristic
# #             h_score = sum(1 if a != b else 0 for a, b in zip(new_state, goal))

# #             node_list.append((new_state, h_score))

# #         return node_list

# #     # Improved heuristic function
# #     def heuristic(self, current, goal):
# #         score = 0
# #         for i, c in enumerate(current):
# #             if c != goal[i]:
# #                 score += 1 + abs(i - goal.index(c))
# #         return score

# #     def a_star(self, start, goal, expand):
# #         open_list = []  # Priority queue with the initial state and g-score
# #         heapq.heappush(open_list, (0, start))

# #         g_scores = {start: 0}  # g-scores for all states
# #         f_scores = {start: self.heuristic(start, goal)}  # f-scores for all states

# #         came_from = {}  # Dictionary to store the previous state for each state

# #         closed_set = set()  # For not revisiting states

# #         while open_list:
# #             self.num_iterations += 1
# #             _, current = heapq.heappop(open_list)  # Get the state with the lowest f-score

# #             if current == goal:
# #                 path = [current]
# #                 while current in came_from:
# #                     current = came_from[current]
# #                     path.append(current)
# #                 path.reverse()
# #                 return path

# #             closed_set.add(current)

# #             for neighbor, h_score in expand(current, goal):
# #                 tentative_g_score = g_scores[current] + 1  # Assuming a cost of 1 for each step

# #                 if neighbor in closed_set:
# #                     continue

# #                 if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
# #                     came_from[neighbor] = current
# #                     g_scores[neighbor] = tentative_g_score
# #                     f_scores[neighbor] = tentative_g_score + h_score
# #                     heapq.heappush(open_list, (f_scores[neighbor], neighbor))

# #         return []

# #     def solve(self, start, goal):
# #         self.num_iterations = 0

# #         # TO DO: a. Add code below to check in advance whether the problem is solvable
# #         if sorted(start) != sorted(goal):
# #             print('This is impossible to solve')
# #             return "IMPOSSIBLE"

# #         self.solution = self.a_star(start, goal, self.anagram_expand)

# #         if not self.solution:
# #             print('No solution found')
# #             return "NONE"

# #         print(str(len(self.solution) - 1) + ' steps from start to goal:')
# #         for step in self.solution:
# #             print(step)

# #         print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')
# #         return str(self.num_iterations)


# # if __name__ == '__main__':
# #     anagram = Anagram()
# #     anagram.solve('TEARDROP', 'PREDATOR')

# # [Running] python -u "d:\Desktop\CS 670\Homework\programming_assignment2_NEW.py"
# # 9 steps from start to goal:
# # TEARDROP
# # EARDROPT
# # ARDROEPT
# # RDROAEPT
# # DROAEPTR
# # ROAEPDTR
# # OAEPRDTR
# # AEPRDTOR
# # EPRDATOR
# # PREDATOR
# # 3989 A* iterations were performed to find this solution.

# # [Done] exited with code=0 in 4.772 seconds


# #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# import heapq

# class Anagram:
#     num_iterations = 0
    
#     def anagram_expand(self, state, goal):
#         node_list = []
#         for pos in range(1, len(state)):
#             new_state = state[1:pos + 1] + state[0] + state[pos + 1:]
#             h_score = self.heuristic(new_state, goal)
#             node_list.append((new_state, h_score))
#         return node_list
    
#     # def heuristic(self, current, goal):
#     #     score = sum(c1 != c2 for c1, c2 in zip(current, goal))
#     #     return score
    
#     def heuristic(self, current, goal):
#     # Count of mismatched characters between current and goal states.
#     mismatches = sum(c1 != c2 for c1, c2 in zip(current, goal))
    
#     # Count of swaps needed to align all letters (ignoring duplicates).
#     swaps = sum(abs(current.index(c) - goal.index(c)) for c in set(current) & set(goal))
    
#     return mismatches + swaps



#     def a_star(self, start, goal, expand):
#         open_list = []  # Priority queue with the initial state and g-score
#         heapq.heappush(open_list, (0, start))

#         g_scores = {start: 0}
#         f_scores = {start: self.heuristic(start, goal)}

#         came_from = {}
#         closed_set = set()

#         while open_list:
#             self.num_iterations += 1
#             _, current = heapq.heappop(open_list) 

#             if current == goal:
#                 path = [current]
#                 while current in came_from:
#                     current = came_from[current]
#                     path.append(current)
#                 path.reverse()
#                 return path
            
#             closed_set.add(current)

#             for neighbor, h_score in expand(current, goal):
#                 tentative_g_score = g_scores[current] + 1 

#                 if neighbor in closed_set:
#                     continue

#                 if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
#                     came_from[neighbor] = current
#                     g_scores[neighbor] = tentative_g_score
#                     f_scores[neighbor] = tentative_g_score + h_score
#                     heapq.heappush(open_list, (f_scores[neighbor], neighbor))
#         return []

#     def solve(self, start, goal):
#         self.num_iterations = 0
#         if sorted(start) != sorted(goal):
#             print('This is impossible to solve')
#             return "IMPOSSIBLE"

#         self.solution = self.a_star(start, goal, self.anagram_expand)

#         if not self.solution:
#             print('No solution found')
#             return "NONE"

#         print(str(len(self.solution) - 1) + ' steps from start to goal:')
#         for step in self.solution:
#             print(step)

#         print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')
#         return str(self.num_iterations)


# if __name__ == '__main__':
#     anagram = Anagram()
#     anagram.solve('TEARDROP', 'PREDATOR')






















import heapq

class Anagram:
    num_iterations = 0
    
    def anagram_expand(self, state, goal):
        node_list = []
        for pos in range(1, len(state)):
            new_state = state[1:pos + 1] + state[0] + state[pos + 1:]
            h_score = sum(a != b for a, b in zip(new_state, goal))  # Admissible heuristic
            node_list.append((new_state, h_score))
        return node_list
    
    def a_star(self, start, goal, expand):
        open_list = []  # Priority queue: [(f_score, state, g_score), ...]
        heapq.heappush(open_list, (0, start, 0))  # (f_score, state, g_score)
        
        g_scores = {start: 0}
        came_from = {}
        
        while open_list:
            self.num_iterations += 1
            
            _, current, g_score_current = heapq.heappop(open_list)
            
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path
            
            for neighbor, h_score in expand(current, goal):
                tentative_g_score = g_score_current + 1
                
                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + h_score
                    heapq.heappush(open_list, (f_score, neighbor, tentative_g_score))
                    came_from[neighbor] = current
        
        return []
    
    def solve(self, start, goal):
        self.num_iterations = 0
        if sorted(start) != sorted(goal):
            print('This is impossible to solve')
            return "IMPOSSIBLE"
        solution = self.a_star(start, goal, self.anagram_expand)
        if not solution:
            print('No solution found')
            return "NONE"
        print(f'{len(solution) - 1} steps from start to goal:')
        for step in solution:
            print(step)
        print(f'{self.num_iterations} A* iterations were performed to find this solution.')
        return str(self.num_iterations)

if __name__ == '__main__':
    anagram = Anagram()
    anagram.solve('TEARDROP', 'PREDATOR')
