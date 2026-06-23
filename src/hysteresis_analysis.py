"""
Hysteresis Loop Analysis

This script loads a sample magnetic hysteresis dataset, plots the hysteresis loop,
and estimates basic magnetic properties such as coercive field and remanent
magnetization.

The dataset used here is synthetic demo data for learning and portfolio purposes.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path: Path) -> pd.DataFrame:
    """Load hysteresis data from a CSV file."""
    data = pd.read_csv(file_path)

    required_columns = {"magnetic_field_mT", "magnetization"}
    if not required_columns.issubset(data.columns):
        raise ValueError(
            f"CSV file must contain the columns: {required_columns}"
        )

    return data


def estimate_remanent_magnetization(data: pd.DataFrame) -> float:
    """
    Estimate remanent magnetization.

    Remanent magnetization is the magnetization value when the magnetic field is
    closest to zero.
    """
    zero_field_index = data["magnetic_field_mT"].abs().idxmin()
    remanence = data.loc[zero_field_index, "magnetization"]
    return remanence


def estimate_coercive_field(data: pd.DataFrame) -> float:
    """
    Estimate coercive field using linear interpolation.

    The coercive field is the magnetic field where magnetization crosses zero.
    This simple method finds the first sign change in magnetization.
    """
    field = data["magnetic_field_mT"].to_numpy()
    magnetization = data["magnetization"].to_numpy()

    for i in range(len(magnetization) - 1):
        m1 = magnetization[i]
        m2 = magnetization[i + 1]

        if m1 == 0:
            return field[i]

        if m1 * m2 < 0:
            h1 = field[i]
            h2 = field[i + 1]

            coercive_field = h1 - m1 * (h2 - h1) / (m2 - m1)
            return coercive_field

    return np.nan


def plot_hysteresis_loop(data: pd.DataFrame, output_path: Path) -> None:
    """Plot and save the hysteresis loop."""
    plt.figure(figsize=(7, 5))

    plt.plot(
        data["magnetic_field_mT"],
        data["magnetization"],
        marker="o",
        linewidth=1.5,
    )

    plt.axhline(0, linestyle="--", linewidth=1)
    plt.axvline(0, linestyle="--", linewidth=1)

    plt.xlabel("Magnetic Field (mT)")
    plt.ylabel("Normalized Magnetization")
    plt.title("Sample Magnetic Hysteresis Loop")

    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.show()


def main() -> None:
    """Run the hysteresis analysis workflow."""
    project_root = Path(__file__).resolve().parents[1]

    data_path = project_root / "examples" / "sample_hysteresis_data.csv"
    figure_path = project_root / "results" / "figures" / "hysteresis_loop.png"

    data = load_data(data_path)

    remanence = estimate_remanent_magnetization(data)
    coercive_field = estimate_coercive_field(data)

    print("Hysteresis Loop Analysis Results")
    print("--------------------------------")
    print(f"Data file: {data_path}")
    print(f"Estimated remanent magnetization: {remanence:.3f}")
    print(f"Estimated coercive field: {coercive_field:.2f} mT")

    plot_hysteresis_loop(data, figure_path)

    print(f"Figure saved to: {figure_path}")


if __name__ == "__main__":
    main()
