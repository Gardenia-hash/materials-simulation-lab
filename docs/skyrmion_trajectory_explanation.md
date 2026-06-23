# Skyrmion Trajectory Analysis Explanation

This document explains the physical meaning and analysis workflow of the skyrmion trajectory example in this repository.

## 1. What Is a Skyrmion?

A magnetic skyrmion is a nanoscale spin texture that can exist in magnetic materials.

It can be regarded as a stable swirling configuration of magnetic moments.

Skyrmions are studied in spintronics because they may be used as information carriers in future magnetic memory and logic devices.

## 2. What Is Skyrmion Trajectory Analysis?

Skyrmion trajectory analysis studies how the position of a skyrmion changes with time.

In a typical micromagnetic simulation, the skyrmion position may be recorded as:

```text
x_position_nm
y_position_nm
time_ns
```

The trajectory shows how the skyrmion moves under an applied current, magnetic field, or other driving force.

## 3. Dataset Used in This Repository

The demo dataset is located at:

```text
examples/sample_skyrmion_trajectory.csv
```

The dataset contains the following columns:

```text
time_ns
x_position_nm
y_position_nm
current_density_1e11_A_per_m2
```

The current dataset is synthetic demo data.

It is not experimental data and is not from unpublished research.

## 4. Physical Quantities Calculated

The Python script calculates several basic quantities from the skyrmion trajectory.

The script is located at:

```text
src/skyrmion_trajectory_analysis.py
```

### 4.1 Displacement

The displacement in the x direction is calculated as:

```text
dx = x_final - x_initial
```

The displacement in the y direction is calculated as:

```text
dy = y_final - y_initial
```

The total displacement is calculated as:

```text
total displacement = sqrt(dx^2 + dy^2)
```

### 4.2 Average Velocity

The average velocity in the x direction is calculated as:

```text
vx = dx / total_time
```

The average velocity in the y direction is calculated as:

```text
vy = dy / total_time
```

The total average speed is calculated as:

```text
v = total displacement / total_time
```

Since the input units are nm and ns, the velocity unit is nm/ns.

Numerically:

```text
1 nm/ns = 1 m/s
```

### 4.3 Skyrmion Hall Angle

The skyrmion Hall angle describes the transverse deflection of the skyrmion motion.

It can be estimated from the ratio between transverse and longitudinal displacement:

```text
theta = arctan(dy / dx)
```

In the script, this is calculated using:

```text
theta = arctan2(dy, dx)
```

The result is converted from radians to degrees.

## 5. Why Is Skyrmion Hall Angle Important?

The skyrmion Hall angle is important because it describes how much the skyrmion deviates from the current direction.

In skyrmion-based devices, a large Hall angle may cause the skyrmion to move toward the device edge.

This can be undesirable for racetrack memory or logic applications.

Therefore, controlling or reducing the skyrmion Hall angle is an important topic in spintronic device research.

## 6. Analysis Workflow

The script performs the following steps:

1. Load the skyrmion trajectory data from a CSV file
2. Check whether the required columns exist
3. Calculate x and y displacement
4. Calculate average velocity
5. Estimate the skyrmion Hall angle
6. Plot the skyrmion trajectory
7. Plot x and y position as a function of time
8. Save the generated figures

## 7. Expected Figures

The script generates two figures:

```text
results/figures/skyrmion_trajectory.png
```

and:

```text
results/figures/skyrmion_position_vs_time.png
```

The first figure shows the trajectory in the x-y plane.

The second figure shows how x and y positions change with time.

## 8. Future Improvements

Possible future improvements include:

- Analyzing MuMax3 output files directly
- Tracking skyrmion center from magnetization snapshots
- Comparing trajectories under different current densities
- Calculating velocity-current relationships
- Studying the effect of damping constant
- Studying the effect of Dzyaloshinskii-Moriya interaction
- Comparing skyrmion and skyrmionium motion
- Adding uncertainty analysis and fitting
- Creating a Jupyter Notebook version for interactive explanation
