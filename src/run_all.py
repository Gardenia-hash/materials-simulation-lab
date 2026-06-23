"""
Run All Analysis Scripts

This script runs all current analysis workflows in the Materials Simulation Lab
repository.

It is designed as a simple entry point for checking whether the demo analyses
can run successfully.
"""

from hysteresis_analysis import main as run_hysteresis_analysis
from skyrmion_trajectory_analysis import main as run_skyrmion_trajectory_analysis


def main() -> None:
    """Run all available analysis workflows."""
    print("=" * 60)
    print("Running Materials Simulation Lab Analyses")
    print("=" * 60)

    print("\n[1/2] Running hysteresis loop analysis...\n")
    run_hysteresis_analysis()

    print("\n[2/2] Running skyrmion trajectory analysis...\n")
    run_skyrmion_trajectory_analysis()

    print("\n" + "=" * 60)
    print("All analyses completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
