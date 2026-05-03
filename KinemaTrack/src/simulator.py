import matplotlib.pyplot as plt
import numpy as np
from .engine import PathFinder
from .utils import smooth_trajectory

class KinemaTrackEngine:
    """Manages environment generation and visual simulation."""
    def __init__(self, width=250, height=250):
        self.width = width
        self.height = height
        self.grid = np.zeros((width, height))
        self.obstacles = []
        self.path_finder = PathFinder(self.grid, width, height)

    def generate_obstacles(self, count=15):
        """Generates random circular obstacles with precise grid masking."""
        for _ in range(count):
            x = np.random.randint(40, 210)
            y = np.random.randint(40, 210)
            r = np.random.randint(15, 25)
            self.obstacles.append((x, y, r))
            
            # Precise circular masking on the grid for A* accuracy
            y_coords, x_coords = np.ogrid[:self.height, :self.width]
            distance_mask = (x_coords - x)**2 + (y_coords - y)**2 <= r**2
            self.grid[distance_mask] = 1

    def run_simulation(self, start, goal):
        """Executes the planning pipeline and renders the final trajectory."""
        print(f"[INFO] Calculating trajectory from {start} to {goal}...")
        raw_path = self.path_finder.get_path(start, goal)
        
        if raw_path:
            print("[SUCCESS] Path found. Applying spline smoothing...")
            path = smooth_trajectory(raw_path)
            self._display(path)
        else:
            print("[ERROR] No valid path found. Check obstacle density.")

    def _display(self, path):
        """Renders the environment, obstacles, and the optimized path."""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_title("KinemaTrack v3.1 | Autonomous Trajectory Planning", fontsize=14)
        
        # Draw circular obstacles as defined in generate_obstacles
        for (x, y, r) in self.obstacles:
            circle = plt.Circle((x, y), r, color='tomato', alpha=0.6, label='Obstacle' if 'Obstacle' not in [l.get_label() for l in ax.get_lines()] else "")
            ax.add_patch(circle)
            
        # Extract X and Y coordinates from the smoothed path
        px, py = zip(*path)
        
        # Plotting the optimized spline path
        ax.plot(px, py, color='#007acc', linewidth=2.5, label='Optimized Path')
        
        # Marking Start and Goal points
        ax.scatter(*path[0], color='forestgreen', s=100, edgecolors='black', zorder=5, label='Start Point')
        ax.scatter(*path[-1], color='crimson', s=150, marker='X', edgecolors='black', zorder=5, label='Target Goal')
        
        # Final visual adjustments
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.grid(True, linestyle='--', alpha=0.4)
        
        # Clean up legend (removing duplicate obstacle labels)
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc='upper right')
        
        plt.tight_layout()
        plt.show()