# EIM

This is repository accompanying the paper: 
Jan Maciej Kościelny and Anna Sztyber-Betley, Definitions and comprehensive assessment of fault isolability in expert-based diagnostic systems

It contains Python code to compute metrices and indices proposed in the paper.

## File structure:


* Notebooks present results of the computation for the four tanks system:
    - FSM_C.ipynb - Fault Signature Matirc, column inference
    - FSM_R.ipynb - Fault Signature Matrix, row inference
    - FIS_C.ipynb - Fault Information System, columns inference
    - FIS_R.ipynb - Fault Information System, row inference


## Dataset (`four_tanks` directory)
The example notebooks use data describing the four tank system:
- `fis.csv` – Fault Information System where rows are symptoms and columns are faults. Values `-1`, `0` and `+1` indicate the expected symptom behaviour.
- `fsm.csv` – binary Fault Signature Matrix used in the FSM based calculations.
- `es.py` – a dictionary of elementary sequences required for IMES calculations.
The notebooks load these files to build matrices and compute the proposed indices.

## Dataset (`example5` directory)
This directory contains data for simple illustrative Example 5:
- `fis.csv` – Fault Information System where rows are symptoms and columns are faults. Values `-1`, `0` and `+1` indicate the expected symptom behaviour.

## Weight configuration (conf directory)
The folder `conf/` stores numeric weights used when computing the isolability metrics.
- `delta_weights.py` defines the coefficients assigned to different pairwise relationships for the EIM and IMES matrices.
- `IMES_weights_*.csv` contain matrices used when combining EIM with IMES (EIM*).
You can modify the numeric values in these files to perform alternative weighting schemes before running the calculations.

* Directory isolability contains code for the computation of indices:
    - pairwise_relationships.py - contains a set of boolean functions, checking for the existence of particular isolability relation 
    - matrices_and_indices.py - computation of EIM and IMES matrices and isolability metrics

## Example usage
To reproduce the calculations with the default configuration open one of the notebooks (e.g. `FIS_C.ipynb`) and execute all cells.

## Using your own data

You can run the scripts with a different dataset by adding your own files in
new directory.
Prepare the following files:

1. `fis.csv` – fault information system, where rows are symptoms and columns are
   faults.
2. `fsm.csv` – fault signature matrix with binary values.
3. `es.py` – a Python module exposing a dictionary named `ess` with elementary
   sequences.

Place them in a directory of your choice and update the read calls, e.g.

```python
fis_df = pd.read_csv('my_experiment/fis.csv', sep=';', index_col=0, dtype=str)
fsm_df = pd.read_csv('my_experiment/fsm.csv', sep=';', index_col=0)
from my_experiment.es import ess
```

If you wish to experiment with alternative weighting schemes, edit the values in
`conf/delta_weights.py` or the `IMES_weights_*.csv` files before executing the
calculations.