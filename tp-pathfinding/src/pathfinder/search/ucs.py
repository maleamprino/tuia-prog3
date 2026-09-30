from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        reached = {}
        reached[root.state] = root.cost

        frontier=PriorityQueueFrontier()
        frontier.add(root, root.cost)
        
        while not frontier.is_empty():
            node=frontier.pop()
            
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                successor_state = grid.result(node.state, action)
                cost=node.cost + grid.individual_cost(node.state, action)
                if successor_state not in reached or cost < reached[successor_state]:
                    child = Node("", state=successor_state, parent=node, action=action, cost=cost)
                    reached[successor_state]=cost
                    frontier.add(child, cost)

        return NoSolution(reached)
