import numpy as np
from scipy.interpolate import splprep, splev

def smooth_trajectory(raw_path):
    """
    Applies Cubic B-Spline interpolation for smooth robotic motion.
    Filters out redundant waypoints to ensure numerical stability.
    """
    # Spline calculation requires at least 4 unique points
    if len(raw_path) < 4:
        return raw_path
    
    try:
        # Filter duplicates or very close points to prevent 'singular matrix' errors
        unique_path = [raw_path[0]]
        for p in raw_path[1:]:
            # Use Euclidean distance to check if the next point is far enough
            if np.linalg.norm(np.array(unique_path[-1]) - np.array(p)) > 1.0:
                unique_path.append(p)
        
        # If after filtering we have too few points, return the raw path
        if len(unique_path) < 4:
            return raw_path
                
        x, y = zip(*unique_path)
        
        # s parameter controls smoothing. Higher s = smoother but less accurate to points.
        # len(unique_path) * 0.3 is a balanced choice for robotic paths.
        tck, u = splprep([x, y], s=len(unique_path) * 0.3)
        
        # Generate 150 points for a high-resolution smooth curve[cite: 4]
        u_new = np.linspace(0, 1, 150)
        smoothed_x, smoothed_y = splev(u_new, tck)
        
        return list(zip(smoothed_x, smoothed_y))
        
    except Exception as e:
        # If spline fails for any reason, fall back to the original path[cite: 4]
        print(f"[WARNING] Trajectory smoothing failed: {e}")
        return raw_path