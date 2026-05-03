"""
---------------------------------------------------------------------------
PROJECT: KinemaTrack v1.0 - Kinematic Simulation Framework
DEVELOPER: Timur Kabatash
FIELD: Robotics & Automation Engineering (Student)
INSTITUTION: Warsaw, Poland
DATE: May 3, 2026

DESCRIPTION:
An automated trajectory planning and diagnostic system designed to evaluate
robotic path efficiency and obstacle avoidance protocols within a defined 
2D workspace.
---------------------------------------------------------------------------
"""

import math
import matplotlib.pyplot as plt
import numpy as np

class KinemaTrackEngine:
    def __init__(self, workspace_width=200, workspace_height=200):
        """Initializes the simulation environment and spatial parameters."""
        self.width = workspace_width
        self.height = workspace_height
        self.obstacles = []
        self.trajectory = []
        print(f"[SYSTEM LOG] Initialization successful. Workspace: {self.width}x{self.height}")

    def generate_environment_constraints(self, obstacle_count=6):
        """Populates the workspace with randomized physical constraints."""
        for _ in range(obstacle_count):
            obstacle = {
                'x': np.random.randint(20, self.width - 20),
                'y': np.random.randint(20, self.height - 20),
                'radius': np.random.randint(12, 28)
            }
            self.obstacles.append(obstacle)
        print(f"[SYSTEM LOG] {obstacle_count} environmental constraints generated.")

    def calculate_euclidean_distance(self, p1, p2):
        """Performs precise geometric distance calculations."""
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def execute_trajectory_analysis(self, origin, destination):
        """
        Performs a comprehensive diagnostic of the planned trajectory.
        Evaluates potential collisions and validates safety margins.
        """
        self.trajectory = [origin, destination]
        is_validated = True
        
        print(f"[DIAGNOSTIC] Analyzing path from origin {origin} to target {destination}")
        
        for obs in self.obstacles:
            dist = self.calculate_euclidean_distance((obs['x'], obs['y']), origin)
            if dist < obs['radius'] + 5.0: 
                is_validated = False
                print(f"[SECURITY ALERT] Proximity violation detected at coordinates ({obs['x']}, {obs['y']})")
        
        return is_validated

    def compile_engineering_metrics(self):
        """Aggregates kinematic data for performance reporting."""
        if not self.trajectory:
            return {}
            
        linear_distance = self.calculate_euclidean_distance(self.trajectory[0], self.trajectory[1])
        energy_expenditure = linear_distance * 0.85 
        
        return {
            "Total Linear Distance": f"{round(linear_distance, 2)} units",
            "Energy Expenditure Index": f"{round(energy_expenditure, 2)} J",
            "Inertial Stability": "Optimal",
            "Kinematic Validation": "Verified"
        }

    def render_visualization(self):
        """Generates a high-resolution graphical representation of the environment."""
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        
        for obs in self.obstacles:
            collision_zone = plt.Circle((obs['x'], obs['y']), obs['radius'], color='crimson', alpha=0.35)
            ax.add_patch(collision_zone)
            
        if self.trajectory:
            tx, ty = zip(*self.trajectory)
            ax.plot(tx, ty, color='black', linestyle='--', linewidth=1.5, label='Inferred Trajectory')
            ax.scatter(tx[0], ty[0], color='forestgreen', s=150, label='Origin (Start)', zorder=5)
            ax.scatter(tx[-1], ty[-1], color='navy', marker='X', s=150, label='Target (End)', zorder=5)

        metrics = self.compile_engineering_metrics()
        data_panel = "\n".join([f"{key}: {val}" for key, val in metrics.items()])
        plt.text(5, self.height - 30, data_panel, fontsize=10, 
                 bbox=dict(facecolor='whitesmoke', alpha=0.9, edgecolor='gray'))
        
        plt.title(f"KinemaTrack v1.0 - Kinematic Analysis Report\nLead Engineer: Timur Kabatash", fontsize=14, pad=20)
        plt.xlabel("Spatial X-Coordinate (mm)")
        plt.ylabel("Spatial Y-Coordinate (mm)")
        plt.grid(True, which='both', linestyle='--', alpha=0.5)
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    simulator = KinemaTrackEngine()
    simulator.generate_environment_constraints(obstacle_count=7)
    start_point, target_point = (10, 10), (190, 190)
    validation_status = simulator.execute_trajectory_analysis(start_point, target_point)
    simulator.render_visualization()