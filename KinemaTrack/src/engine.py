import math
import heapq

class PathFinder:
    """Handles A* path planning logic and heuristics."""
    def __init__(self, grid, width, height):
        self.grid = grid
        self.width = width
        self.height = height

    def heuristic(self, p1, p2):
        """Standard Euclidean distance."""
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def get_path(self, start, goal):
        """Calculates the shortest path using A* algorithm."""
        open_set = []
        heapq.heappush(open_set, (0.0, start))
        came_from = {}
        g_score = {start: 0.0}
        
        # 8-way movement: (dx, dy, cost)
        motions = [(0,1,1), (1,0,1), (0,-1,1), (-1,0,1), 
                   (1,1,1.414), (-1,1,1.414), (1,-1,1.414), (-1,-1,1.414)]

        while open_set:
            _, current = heapq.heappop(open_set)
            
            if self.heuristic(current, goal) < 1.5:
                path = [goal, current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return path[::-1]

            for dx, dy, cost in motions:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height:
                    if self.grid[int(neighbor[0]), int(neighbor[1])] == 1:
                        continue
                    
                    tentative_g = g_score[current] + cost
                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + self.heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f_score, neighbor))
        return None