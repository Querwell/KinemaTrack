from src.simulator import KinemaTrackEngine

def main():
    """Project entry point for KinemaTrack Simulation."""
    sim = KinemaTrackEngine(width=250, height=250)
    
    # Environment Setup
    sim.generate_obstacles(count=15)
    
    # Execute Pathfinding
    start_pos = (20, 20)
    goal_pos = (230, 230)
    
    sim.run_simulation(start=start_pos, goal=goal_pos)

if __name__ == "__main__":
    main()