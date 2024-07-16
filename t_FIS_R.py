#%%
import pandas as pd
from isolability import pairwise_relationships as pr
import isolability.martices_and_indices as ind
from four_tanks.es import ess

import importlib
importlib.reload(pr)
importlib.reload(ind)

# %%
fis_df = pd.read_csv('four_tanks/fis.csv', sep=';', index_col=0, dtype=str)
fis_df
# %%
fis_df = fis_df.map(lambda x: set(a.strip() for a in x.split(',')))
fis_df
# %%
pr.RS_R_FIS(fis_df, 7, 8)
# %%
eim = ind.EIM_R_FIS(fis_df)
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
eim_star = ind.EIM_star_R_FIS(fis_df, ess, comp_weights)
eim_star
# %%
c_delta = ind.C_Delta(eim_star)
print(f"{c_delta:.3f}")
# %%
c_star_delta = ind.C_star_Delta(eim_star)
print(f"{c_star_delta:.3f}")
# %%
