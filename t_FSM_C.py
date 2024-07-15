#%%
import pandas as pd
from isolability import pairwise_relationships as pr
import isolability.martices_and_indices as ind
from four_tanks.es import ess

import importlib
importlib.reload(pr)
importlib.reload(ind)

#%%
fsm_df = pd.read_csv('four_tanks/fsm.csv', sep=';', index_col=0)
fsm_df
# %%
fsm = fsm_df.to_numpy()
fsm
# %%
pr.R_ES_W(ess, 1, 2)
# %%
eim = ind.EIM_C_FSM(fsm)
eim
# %%
c_delta = ind.C_Delta(eim)
print(f"{c_delta:.3f}")
# %%
c_star_delta = ind.C_star_Delta(eim)
print(f"{c_star_delta:.3f}")
# %%
imes = ind.IMES(ess)
imes
# %%
comp_weights = pd.read_csv('conf/IMES_weights.csv', sep=';', index_col=0)
comp_weights
# %%
eim_star = ind.EIM_star_C_FSM(eim, ess,comp_weights)
eim_star
# %%