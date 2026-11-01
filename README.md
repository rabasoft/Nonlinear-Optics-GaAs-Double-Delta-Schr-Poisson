# Nonlinear-Optics-GaAs-Double-Delta-Schrödinger-Poisson
Python 2D contour maps for self-consistent Schrödinger-Poisson equation and nonlinear optical responses in double delta-doped GaAs structures.
# Data and Visualization Scripts: Nonlinear Optical Responses in Double $\delta$-doped GaAs Structures

This repository contains the numerical datasets and Python visualization scripts associated with the manuscript: 
**"A Self-consistent Schrödinger-Poisson Study of the Maximum Nonlinear Optical Responses in Double $\delta$-doped GaAs Structures Tuned by Asymmetry and Layer Separation"** (Submitted to *Computational Materials Science*).

## Overview
This repository shares the direct output datasets from the self-consistent Schrödinger-Poisson calculations and the routines to visualize them. The provided Python scripts generate high-quality 2D contour maps and 3D surface plots for the optical coefficients, subband energy differences, and dipole matrix elements.

## Repository Structure

### 1. Data Files (`/data`)
* **`optical_coefficients.npz`**: Contains the computed numerical results for the Nonlinear Optical Responses: Optical Rectification (NOR), Second-Harmonic Generation (SHG), and Third-Harmonic Generation (THG).
* **`energies_and_matrix_elements.npz`**: Contains the subband energy differences ($E_{ij}$) and their respective transition dipole matrix elements ($M_{ij}$) associated with each optical coefficient.

### 2. Visualization Scripts (`/src`)
* **`plot_2D_contours.py`**: Generates 2D contour maps for the optical coefficients, $E_{ij}$, and $M_{ij}$ across different asymmetry and layer separation parameters.
* **`plot_3D_surfaces.py`**: Generates 3D surface projections for every coefficients.

## Prerequisites
To run the visualization scripts, you need Python 3 and the following libraries:
* `numpy`
* `matplotlib`

Install them via:
```bash
pip install numpy matplotlib
