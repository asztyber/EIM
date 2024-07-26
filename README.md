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


* Directory four_tanks contain input data for the example:
    - fis.csv - Fault Information System
    - fsm.csv - Fault Signature Matrix
    - es.py - Elementary Sequences

* Directory conf contains weight:
    - delta_weights.py - weights for different types of pairwise relationships
    - IMES_weights_* - weight for the conjunction of EIM and IMES matrices

* Directory isolability contains code for the computation of indices:
    - pairwise_relationships.py - contains a set of boolean functions, checking for the existence of particular isolability relation 
    - matrices_and_indices.py - computation of EIM and IMES matrices and isolability metrics

