import numpy as np
import matplotlib.pyplot as plt

# Campus shuttle GPS measurements
time = np.array([0, 5, 10, 15, 20, 25, 30], dtype=float)

# Shuttle position in metres along its route
position = np.array([0, 18, 42, 72, 108, 150, 198], dtype=float)

# Array for estimated speeds
speed = np.zeros_like(position)

# Forward difference at the first measurement
speed[0] = (
    position[1] - position[0]
) / (
    time[1] - time[0]
)

# Central difference for interior measurements
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the final measurement
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

# Display results
print("Campus Shuttle Speed Monitoring")

for t, x, v in zip(time, position, speed):
    print(
        f"Time: {t:.0f}s | "
        f"Position: {x:.1f}m | "
        f"Estimated speed: {v:.2f}m/s"
    )

# Plot estimated speed
plt.plot(time, speed, marker="o")
plt.xlabel("Time (seconds)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Campus Shuttle Speed Monitoring")
plt.grid(True)
plt.show()
