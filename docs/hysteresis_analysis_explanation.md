# Hysteresis Analysis Explanation

This document explains the physical meaning and analysis workflow of the hysteresis loop example in this repository.

## 1. What Is a Hysteresis Loop?

A magnetic hysteresis loop describes how the magnetization of a magnetic material changes when an external magnetic field is applied and swept back and forth.

The horizontal axis is the applied magnetic field, usually written as:

```text
H
```

The vertical axis is the magnetization of the material, usually written as:

```text
M
```

In this repository, the sample dataset uses:

```text
magnetic_field_mT
```

as the magnetic field in millitesla, and:

```text
magnetization
```

as the normalized magnetization.

## 2. Why Is It Important?

A hysteresis loop is important because it shows key magnetic properties of a material.

These properties are useful in areas such as:

- Magnetic materials
- Spintronics
- Magnetic memory devices
- Skyrmion-based devices
- Micromagnetic simulation
- Materials characterization

## 3. Key Magnetic Properties

### 3.1 Remanent Magnetization

Remanent magnetization is the magnetization remaining in the material when the external magnetic field is close to zero.

In simple terms:

```text
Remanent magnetization = magnetization at H ≈ 0
```

A high remanent magnetization means the material can retain magnetization even after the external field is removed.

### 3.2 Coercive Field

The coercive field is the magnetic field required to reduce the magnetization to zero.

In simple terms:

```text
Coercive field = magnetic field where M crosses zero
```

A large coercive field usually means the material is harder to demagnetize.

A small coercive field usually means the material is easier to switch magnetically.

## 4. Analysis Workflow

The Python script in this repository performs the following steps:

1. Load the sample hysteresis data from a CSV file
2. Check whether the required columns exist
3. Estimate remanent magnetization
4. Estimate coercive field using linear interpolation
5. Plot the hysteresis loop
6. Save the generated figure

The script is located at:

```text
src/hysteresis_analysis.py
```

The sample data file is located at:

```text
examples/sample_hysteresis_data.csv
```

## 5. Linear Interpolation for Coercive Field

The script estimates the coercive field by finding where the magnetization changes sign.

For example, if two adjacent data points are:

```text
(H1, M1)
(H2, M2)
```

and the magnetization crosses zero between them, the coercive field can be estimated by linear interpolation:

```text
Hc = H1 - M1 * (H2 - H1) / (M2 - M1)
```

This is a simple approximation suitable for demo data and learning purposes.

For real research data, more careful smoothing, fitting, and uncertainty analysis may be needed.

## 6. Notes on the Current Dataset

The current dataset is synthetic demo data.

It is not experimental data and is not from unpublished research.

The purpose of this dataset is to demonstrate a basic materials data analysis workflow using Python.

## 7. Future Improvements

Possible future improvements include:

- Separating ascending and descending branches of the hysteresis loop
- Calculating both positive and negative coercive fields
- Estimating saturation magnetization
- Adding uncertainty analysis
- Supporting real MuMax3 or experimental output formats
- Creating Jupyter Notebook versions for interactive explanation
