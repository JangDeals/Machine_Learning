# Machine Learning Programme

Practical supervised machine learning (classification and regression) on structured data, built through hands-on projects.

## Environment

One shared conda environment for the whole programme:

    conda activate mlpath

Python 3.11. Install packages inside it with `pip` only (not `conda install`).
To rebuild the environment elsewhere: `pip install -r requirements.txt`

## Project layout

- `data/raw/`: original datasets, never modified
- `data/processed/`: derived datasets produced by code
- `notebooks/`: exploration and learning exercises
- `src/`: reusable code shared across notebooks
- `models/`, `experiments/`, `reports/`: model work, experiment records, final write-ups

## Data

Datasets are not stored in Git. Each one is downloaded from Kaggle and placed in the matching `data/raw/` folder.

## Status

Module 1 (setup) in progress.