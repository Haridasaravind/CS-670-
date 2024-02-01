import heapq

class Anagram:
    num_iterations = 0

    def anagram_expand(self, state, goal):
        node_list = []

        for pos in range(1, len(state)):  # Create each possible state that can be created from the current one in a single step
            new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

            # Calculate the heuristic score (h-score) as the number of mismatched letters
            score = sum(1 for a, b in zip(new_state, goal) if a != b)

            node_list.append((new_state, score))

        return node_list

    def a_star(self, start, goal, expand):
        open_set = []  # Priority queue
        heapq.heappush(open_set, (0, start))  # Add start state with f-score 0
        came_from = {}  # Dictionary to store parent states
        g_score = {start: 0}  # Dictionary to store g-scores
        f_score = {start: self.heuristic(start, goal)}  # Dictionary to store f-scores

        while open_set:
            current_f, current_state = heapq.heappop(open_set)

            if current_state == goal:
                path = [current_state]
                while current_state in came_from:
                    current_state = came_from[current_state]
                    path.append(current_state)
                path.reverse()
                return path

            for neighbor, h_score in expand(current_state, goal):
                tentative_g_score = g_score[current_state] + 1  # Cost for moving to neighbor

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_state
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + h_score
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []  # No solution found

    def heuristic(self, state, goal):
        return sum(1 for a, b in zip(state, goal) if a != b)  # Count mismatched letters

    def solve(self, start, goal):
        self.num_iterations = 0

        # Check if the problem is solvable
        if not self.is_solvable(start, goal):
            print('This is impossible to solve')
            return "IMPOSSIBLE"

        self.solution = self.a_star(start, goal, self.anagram_expand)

        if not self.solution:
            print('No solution found')
            return "NONE"

        print(str(len(self.solution) - 1) + ' steps from start to goal:')

        for step in self.solution:
            print(step)

        print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')

        return str(self.num_iterations)

    def is_solvable(self, start, goal):
        return sorted(start) == sorted(goal)  # Check if both words have the same set of letters

if __name__ == '__main__':
    anagram = Anagram()
    anagram.solve('TEARDROP', 'PREDATOR')



#  class Anagram:
#     num_iterations = 0

#     def anagram_expand(self, state, goal):
#         node_list = []

#         for pos in range(1, len(state)):  # Create each possible state that can be created from the current one in a single step
#             new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

#             # TO DO: c. Improve the scoring function here
#             # Instead of a simple score of 0 or 1, calculate a better heuristic score
#             # based on how close 'new_state' is to the 'goal' state.
#             # Assign this heuristic score to the 'score' variable.
#             # Hint: You can compare the 'new_state' and 'goal' to determine the score.
#             # If they are very similar, the score should be lower.

#             # Example (replace this with your scoring logic):
#             # if new_state == goal:
#             #     score = 0
#             # else:
#             #     score = some_heuristic_function(new_state, goal)

#             node_list.append((new_state, score))

#         return node_list

#     # TO DO: b. Return either the solution as a list of states from start to goal or [] if there is no solution.
#     def a_star(self, start, goal, expand):
#         # TO DO: Implement the A* algorithm here to find the optimal solution.
#         # You need to use the 'expand' function to generate successor states and their h-scores.
#         # Maintain a priority queue (or another data structure) to keep track of the states to explore.
#         # Keep track of the total cost (g-score) for each state and update it as you explore.
#         # Also, be sure to handle cases where no solution is possible.

#         return []  # Replace this with your implementation

#     # TO DO: a. Add code below to check in advance whether the problem is solvable
#     def is_solvable(self, start, goal):
#         # Implement a check to determine if it's possible to transform 'start' into 'goal'
#         # using the given rules. If it's impossible, return False; otherwise, return True.

#         # Hint: You can check if both words have the same set of letters
#         # with the same frequency. If not, it's impossible to transform one into the other.

#          return sorted(start) == sorted(goal) # Replace this with your implementation

#     # Finds a solution, i.e., the set of steps from one word to its anagram
#     def solve(self, start, goal):
#         self.num_iterations = 0

#         # Check if the problem is solvable
#         if not self.is_solvable(start, goal):
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

