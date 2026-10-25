# Machine Learning Programme

Practical supervised machine learning (classification and regression) on structured data, built through hands-on projects.

## Environment

Use one shared conda environment for the whole programme.

### Setup from a fresh clone

Run the following commands in order:

```bash
git clone <repository-url>
cd <repository-folder>
conda create -n mlpath python=3.11
conda activate mlpath
pip install -r requirements.txt
pip install -e .
```

Replace `<repository-url>` with the repository's Git URL and `<repository-folder>` with the name of the cloned directory.

- `conda create -n mlpath python=3.11` creates the environment using Python 3.11.
- `conda activate mlpath` activates the environment.
- `pip install -r requirements.txt` installs the project's dependencies.
- `pip install -e .` installs the project in editable mode from the project root, making `src` importable without manually configuring Python's import path.

Use `pip` rather than `conda install` to install project packages inside the environment.

To reactivate the environment in a future session:

```bash
conda activate mlpath
```

## Project layout

- `data/raw/`: original datasets, never modified
- `data/processed/`: derived datasets produced by code
- `notebooks/`: exploration and learning exercises
- `src/`: reusable code shared across notebooks
- `models/`: trained models and model-related artifacts
- `experiments/`: experiment records and results
- `reports/`: final write-ups and analysis reports

## Data

Datasets are not stored in Git. Each dataset is downloaded from Kaggle and placed in its corresponding `data/raw/` folder.

Raw datasets remain unchanged. Any cleaning, transformation, or feature engineering that produces a new dataset should write the derived data to `data/processed/`.

## Status

**Module 1 — Setup: Complete.**

Remaining: Kaggle API download helper, planned for Module 2.