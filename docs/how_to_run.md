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

The main libraries used in this repository include:

- NumPy
- Pandas
- Matplotlib
- SciPy
- Jupyter

## 3. Run the Hysteresis Analysis Example

The first example script is:

```text
src/hysteresis_analysis.py
```

It reads the sample dataset:

```text
examples/sample_hysteresis_data.csv
```

To run the script, use:

```bash
python src/hysteresis_analysis.py
```

## 4. Expected Output

The script will print basic analysis results, including:

- Estimated remanent magnetization
- Estimated coercive field

It will also generate a hysteresis loop figure and save it to:

```text
results/figures/hysteresis_loop.png
```

## 5. Notes

The current dataset is synthetic demo data.

It is used only for learning, testing, and portfolio demonstration.

No unpublished research data or confidential experimental data should be uploaded to this repository.
