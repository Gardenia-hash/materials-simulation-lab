"""
Skyrmion Trajectory Analysis

This script loads a sample skyrmion trajectory dataset, calculates basic motion
properties, and plots the skyrmion trajectory.

The dataset used here is synthetic demo data for learning and portfolio purposes.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path: Path) -> pd.DataFrame:
    """Load skyrmion trajectory data from a CSV file."""
    data = pd.read_csv(file_path)

    required_columns = {
        "time_ns",
        "x_position_nm",
        "y_position_nm",
        "current_density_1e11_A_per_m2",
    }

    if not required_columns.issubset(data.columns):
        raise ValueError(f"CSV file must contain the columns: {required_columns}")

    return data


def calculate_displacement(data: pd.DataFrame) -> tuple[float, float, float]:
    """
    Calculate total displacement in x, y, and total distance.

    Returns:
        dx: displacement in x direction, in nm
        dy: displacement in y direction, in nm
        total_displacement: total displacement magnitude, in nm
    """
    dx = data["x_position_nm"].iloc[-1] - data["x_position_nm"].iloc[0]
    dy = data["y_position_nm"].iloc[-1] - data["y_position_nm"].iloc[0]

    total_displacement = np.sqrt(dx**2 + dy**2)

    return dx, dy, total_displacement


def calculate_average_velocity(data: pd.DataFrame) -> tuple[float, float, float]:
    """
    Calculate average velocity in x, y, and total direction.

    Since the input units are nm and ns, the velocity unit is nm/ns.
    Numerically, 1 nm/ns is equal to 1 m/s.
    """
    dx, dy, total_displacement = calculate_displacement(data)

    total_time = data["time_ns"].iloc[-1] - data["time_ns"].iloc[0]

    vx = dx / total_time
    vy = dy / total_time
    v_total = total_displacement / total_time

    return vx, vy, v_total


def calculate_skyrmion_hall_angle(data: pd.DataFrame) -> float:
    """
    Calculate the skyrmion Hall angle.

    The skyrmion Hall angle is estimated from the ratio between transverse
    displacement and longitudinal displacement.
    """
    dx, dy, _ = calculate_displacement(data)

    hall_angle_rad = np.arctan2(dy, dx)
    hall_angle_deg = np.degrees(hall_angle_rad)

    return hall_angle_deg


def plot_trajectory(data: pd.DataFrame, output_path: Path) -> None:
    """Plot and save the skyrmion trajectory."""
    plt.figure(figsize=(6, 5))

    plt.plot(
        data["x_position_nm"],
        data["y_position_nm"],
        marker="o",
        linewidth=1.5,
    )

    plt.xlabel("x position (nm)")
    plt.ylabel("y position (nm)")
    plt.title("Sample Skyrmion Trajectory")

    plt.grid(True, alpha=0.3)
    plt.axis("equal")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.show()


def plot_position_vs_time(data: pd.DataFrame, output_path: Path) -> None:
    """Plot x and y positions as functions of time."""
    plt.figure(figsize=(7, 5))

    plt.plot(
        data["time_ns"],
        data["x_position_nm"],
        marker="o",
        linewidth=1.5,
        label="x position",
    )

    plt.plot(
        data["time_ns"],
        data["y_position_nm"],
        marker="s",
        linewidth=1.5,
        label="y position",
    )

    plt.xlabel("Time (ns)")
    plt.ylabel("Position (nm)")
    plt.title("Skyrmion Position vs Time")

    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.show()


def main() -> None:
    """Run the skyrmion trajectory analysis workflow."""
    project_root = Path(__file__).resolve().parents[1]

    data_path = project_root / "examples" / "sample_skyrmion_trajectory.csv"

    trajectory_figure_path = (
        project_root / "results" / "figures" / "skyrmion_trajectory.png"
    )

    position_figure_path = (
        project_root / "results" / "figures" / "skyrmion_position_vs_time.png"
    )

    data = load_data(data_path)

    dx, dy, total_displacement = calculate_displacement(data)
    vx, vy, v_total = calculate_average_velocity(data)
    hall_angle = calculate_skyrmion_hall_angle(data)

    current_density = data["current_density_1e11_A_per_m2"].iloc[0]

    print("Skyrmion Trajectory Analysis Results")
    print("------------------------------------")
    print(f"Data file: {data_path}")
    print(f"Current density: {current_density:.2f} × 10^11 A/m^2")
    print(f"x displacement: {dx:.2f} nm")
    print(f"y displacement: {dy:.2f} nm")
    print(f"Total displacement: {total_displacement:.2f} nm")
    print(f"Average vx: {vx:.2f} nm/ns")
    print(f"Average vy: {vy:.2f} nm/ns")
    print(f"Average speed: {v_total:.2f} nm/ns")
    print(f"Estimated skyrmion Hall angle: {hall_angle:.2f} degrees")

    plot_trajectory(data, trajectory_figure_path)
    plot_position_vs_time(data, position_figure_path)

    print(f"Trajectory figure saved to: {trajectory_figure_path}")
    print(f"Position-time figure saved to: {position_figure_path}")


if __name__ == "__main__":
    main()
