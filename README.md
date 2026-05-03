# KinemaTrack v3.1: Autonomous Robotic Trajectory Planning

An advanced robotic navigation suite implementing **A* Pathfinding** and **Cubic B-Spline Interpolation** for smooth, collision-free movement in dynamic environments.

![Simulation Demo](assets/demo.gif)

## 🚀 Overview
KinemaTrack is designed to solve the complex problem of robotic motion planning in grid-based environments.

## 🛠 Key Features
* **Modular Architecture**: Clean separation between pathfinding logic, geometric utilities, and visual simulation.
* **Precision Masking**: Utilizes Euclidean distance-based circular masking for accurate obstacle representation.
* **Trajectory Smoothing**: Integrated Cubic B-Spline interpolation to ensure $C^2$ continuity.

## 📂 Project Structure
* `main.py`: Entry point for the simulation.
* `src/engine.py`: Core A* algorithm and heuristic calculations.
* `src/utils.py`: Geometric smoothing and spline utilities.
* `src/simulator.py`: Matplotlib-based environment rendering.

## ⚙️ Installation & Usage
1. Clone the repository and navigate to the directory.
2. Install dependencies & run:
   
   pip install -r requirements.txt

   python main.py

---

## 🎓 Academic Roadmap
This framework serves as a foundational tool for upcoming research into **Mechatronics and Robotics Engineering**, focusing on the intersection of automated planning and real-world environmental risk assessment.

### 👨‍💻 Developer

**Timur Kabatash**  

*Robotics & Automation Engineering Student* 

📍 Warsaw, Poland
