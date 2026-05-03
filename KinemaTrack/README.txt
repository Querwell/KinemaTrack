# KinemaTrack v3.1: Autonomous Robotic Trajectory Planning

An advanced robotic navigation suite implementing **A* Pathfinding** and **Cubic B-Spline Interpolation** for smooth, collision-free movement in dynamic environments.[cite: 2, 4]

![Simulation Demo](assets/demo.gif)

## 🚀 Overview
KinemaTrack is designed to solve the problem of robotic motion planning in grid-based environments. Unlike standard A* implementations that produce jagged, "robotic" movements, this engine optimizes the path for kinematic feasibility using high-order spline smoothing.[cite: 3, 4]

## 🛠 Key Features
*   **Modular Architecture**: Clean separation between pathfinding logic, geometric utilities, and visual simulation.[cite: 1]
*   **Precision Masking**: Utilizes Euclidean distance-based circular masking for accurate obstacle representation.[cite: 3]
*   **Trajectory Smoothing**: Integrated Cubic B-Spline interpolation to ensure smooth transitions between waypoints.[cite: 4]
*   **Scalability**: Built to handle variable obstacle densities and grid dimensions.[cite: 3]

## 📂 Project Structure
- `main.py`: Entry point for the simulation.[cite: 1]
- `src/engine.py`: Core A* algorithm and heuristic calculations.[cite: 2]
- `src/utils.py`: Geometric smoothing and spline utilities.[cite: 4]
- `src/simulator.py`: Matplotlib-based environment rendering.[cite: 3]

## ⚙️ Installation & Usage
1. Clone the repository and navigate to the directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt