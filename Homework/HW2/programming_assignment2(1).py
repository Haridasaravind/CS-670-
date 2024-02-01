class Anagram:
    num_iterations = 0
    def anagram_expand(self, state, goal):
        node_list = []

        for pos in range(1, len(state)):  # Create each possible state that can be created from the current one in a single step
            new_state = state[1:pos + 1] + state[0] + state[pos + 1:]

            # TO DO: c. Very simple h' function - please improve!
            if new_state == goal:
                score = 0
            else:
                score = 1

            node_list.append((new_state, score))

        return node_list

    # TO DO: b. Return either the solution as a list of states from start to goal or [] if there is no solution.
    def a_star(self, start, goal, expand):


        return []


    # Finds a solution, i.e., the set of steps from one word to its anagram
    def solve(self,start, goal):

        self.num_iterations = 0

        # TO DO: a. Add code below to check in advance whether the problem is solvable

        # if ...
        #    print('This is impossible to solve')
        #    return "IMPOSSIBLE"

        self.solution = self.a_star(start, goal, self.anagram_expand)

        if not self.solution:
            print('No solution found')
            return "NONE"

        print(str(len(self.solution) - 1) + ' steps from start to goal:')

        for step in self.solution:
            print(step)

        print(str(self.num_iterations) + ' A* iterations were performed to find this solution.')

        return str(self.num_iterations)



if __name__ == '__main__':
    anagram = Anagram()
    anagram.solve('TEARDROP', 'PREDATOR')
