import numpy as np

def RN_C_FSM(fsm, k, m):
    # indices starting from 0
    return np.array_equal(fsm[:, k], fsm[:, m])

def RW_C_FSM(fsm, k, m):
    return not RN_C_FSM(fsm, k, m)

def RS_C_FSM(fsm, k, m):
    return np.sum(fsm[:, k] != fsm[:, m]) > 1

def R_ES_UW(ess, k, m):
    ess_k = ess[k]
    ess_m = ess[m]
    for es1, es2 in ess_k:
        if (es2, es1) not in ess_k:
            if (es2, es1) in ess_m:
                return True
    return False

def R_ES_W(ess, k, m):
    ess_k = ess[k]
    ess_m = ess[m]
    for es1, es2 in ess_k:
        if (es2, es1) not in ess_k: 
            if (es2, es1) in ess_m and (es1, es2) not in ess_m:
                return True
    return False

def R_ES_N(ess, k, m):
    return not R_ES_UW(ess, k, m)

def RN_R_FSM(fsm, k, m):
    return RN_C_FSM(fsm, k, m)

def RUN_R_FSM(fsm, k, m):
    return (fsm[fsm[:, k] == 1, m] == 1).all()

def RUW_R_FSM(fsm, k, m):
    return (fsm[fsm[:, k] == 1, m] == 0).any()

def RW_R_FSM(fsm, k, m):
    return RUW_R_FSM(fsm, m, k) and RUW_R_FSM(fsm, k, m)

def RUS_R_FSM(fsm, k, m):
    return (fsm[fsm[:, k] == 1, m] == 0).sum() > 1

def RS_R_FSM(fsm, k, m):
    return RUS_R_FSM(fsm, m, k) and RUS_R_FSM(fsm, k, m)

def RN_C_FIS(fis, k, m):
    return fis.iloc[:, k].equals(fis.iloc[:, m])

def RUC_C_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    cond_incl = all(v_m.issubset(v_k) for v_k, v_m in zip(col_k, col_m))
    cond_neq = any(v_k != v_m for v_k, v_m in zip(col_k, col_m))
    return cond_incl and cond_neq

def RC_C_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    cond1 = all(not v_m.isdisjoint(v_k) for v_k, v_m in zip(col_k, col_m))
    cond2 = any(v_k.issubset(v_m) and v_k != v_m for v_k, v_m in zip(col_k, col_m))
    cond3 = any(v_m.issubset(v_k) and v_m != v_k for v_k, v_m in zip(col_k, col_m))
    return cond1 and cond2 and cond3

def RW_C_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    return any(v_m.isdisjoint(v_k) for v_k, v_m in zip(col_k, col_m))

def RS_C_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    return sum(v_k.isdisjoint(v_m) for v_k, v_m in zip(col_k, col_m)) > 1

def RN_R_FIS(fis, k, m):
    return RN_C_FIS(fis, k, m)

def RUN_R_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    return all(v_k == v_m for v_k, v_m in zip(col_k, col_m) if '0' not in v_k)

def RUW_R_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    return any('0' in v_m for v_k, v_m in zip(col_k, col_m) if '0' not in v_k)

def RW_R_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    cond1 = any(v_k.isdisjoint(v_m) for v_k, v_m in zip(col_k, col_m) if '0' not in v_m and '0' not in v_k)
    cond2 = RUW_R_FIS(fis, m, k) and RUW_R_FIS(fis, k, m)
    return cond1 or cond2

def RUC_R_FIS(fis, k, m):
    return RUC_C_FIS(fis, k, m)

def RC_R_FIS(fis, k, m):
    return RC_C_FIS(fis, k, m)

def RUS_R_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    return sum('0' in v_m for v_k, v_m in zip(col_k, col_m) if '0' not in v_k) > 1

def RS_R_FIS(fis, k, m):
    col_k = fis.iloc[:, k]
    col_m = fis.iloc[:, m]
    cond1 = sum(v_k.isdisjoint(v_m) for v_k, v_m in zip(col_k, col_m) if '0' not in v_m and '0' not in v_k)
    return cond1 > 1 # definicja do dyskusji