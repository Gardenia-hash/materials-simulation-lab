# How to Run This Project

This document explains how to run the example analysis scripts in this repository.

## 1. Clone the Repository

To download this repository to a local computer, use:

```bash
git clone https://github.com/Gardenia-hash/materials-simulation-lab.git
```

Then enter the project folder:

```bash
cd materials-simulation-lab
```

## 2. Install Python Dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

On Windows, if `python` or `pip` is not recognized, use:

```bash
py -m pip install -r requirements.txt
```

The main libraries used in this repository include:

- NumPy
- Pandas
- Matplotlib
- SciPy
- Jupyter

## 3. Run All Analysis Scripts

The easiest way to run all current demo analyses is:

```bash
python src/run_all.py
```

On Windows, you can use:

```bash
py src/run_all.py
```

This script will run:

```text
src/hysteresis_analysis.py
src/skyrmion_trajectory_analysis.py
```

## 4. Run Individual Scripts

You can also run each analysis script separately.

### Hysteresis Loop Analysis

```bash
python src/hysteresis_analysis.py
```

On Windows:

```bash
py src/hysteresis_analysis.py
```

### Skyrmion Trajectory Analysis

```bash
python src/skyrmion_trajectory_analysis.py
```

On Windows:

```bash
py src/skyrmion_trajectory_analysis.py
```

## 5. Expected Output

The scripts will print basic analysis results in the terminal.

The hysteresis analysis will estimate:

- Remanent magnetization
- Coercive field

The skyrmion trajectory analysis will estimate:

- x and y displacement
- Average velocity
- Skyrmion Hall angle

The generated figures will be saved to:

```text
results/figures/
```

Expected output figures include:

```text
results/figures/hysteresis_loop.png
results/figures/skyrmion_trajectory.png
results/figures/skyrmion_position_vs_time.png
```

## 6. Notes

The current datasets are synthetic demo data.

They are used only for learning, testing, and portfolio demonstration.

No unpublished research data or confidential experimental data should be uploaded to this repository.
