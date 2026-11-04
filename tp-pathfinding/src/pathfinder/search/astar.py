from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        reached = {}
        reached[root.state] = root.cost

        frontier = PriorityQueueFrontier()
        
        #obtener heurística 
        h_root = 0
        if hasattr(grid, "heuristic"):
            h_root = grid.heuristic(root.state)
        elif hasattr(grid, "distance"):
            h_root = grid.distance(root.state, grid.end)

        frontier.add(root, priority=root.cost + h_root)

        while not frontier.is_empty():
            node = frontier.pop()

            #comprobar si se alcanzó el objetivo al extraer de la frontera
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                step_cost = grid.individual_cost(node.state, action)
                new_cost = node.cost + step_cost

                #si el sucesor no fue alcanzado o se encontró un camino con menor costo
                if successor not in reached or new_cost < reached[successor]:
                    reached[successor] = new_cost

                    #crear el nodo hijo
                    son = Node(
                        "",
                        state=successor,
                        cost=new_cost,
                        parent=node,
                        action=action,
                    )

                    #calcular la prioridad f(n) = g(n) + h(n) 
                    h_successor = 0
                    if hasattr(grid, "heuristic"):
                        h_successor = grid.heuristic(successor)
                    elif hasattr(grid, "distance"):
                        h_successor = grid.distance(successor, grid.end)

                    priority = new_cost + h_successor
                    frontier.add(son, priority=priority)

        #si se vacía la frontera sin llegar al objetivo
        return NoSolution(reached)
                          