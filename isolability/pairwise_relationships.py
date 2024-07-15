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

