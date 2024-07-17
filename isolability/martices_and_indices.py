import numpy as np
from isolability import pairwise_relationships as pr
import conf.delta_weights as dw

def create_eim(K, relationship_checks, delta_values):
    """Generic function to create EIM matrices"""
    eim = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            for check, delta in zip(relationship_checks, delta_values):
                if check(k, m):
                    eim[k, m] = delta
                    break
    return eim

def EIM_C_FSM(fsm):
    K = fsm.shape[1]
    checks = [
        lambda k, m: pr.RS_C_FSM(fsm, k, m),
        lambda k, m: pr.RW_C_FSM(fsm, k, m),
        lambda k, m: pr.RN_C_FSM(fsm, k, m)
    ]
    deltas = [dw.delta_FSM_C['S'], dw.delta_FSM_C['W'], dw.delta_FSM_C['N']]
    return create_eim(K, checks, deltas)

def C_Delta(eim):
    K = eim.shape[0]
    return eim.sum()/K/(K-1)

def C_star_Delta(eim):
    eim = np.minimum(eim, 1)
    return C_Delta(eim)

def IMES(ess):
    K = len(ess.keys())
    checks = [
        lambda k, m: pr.R_ES_W(ess, k, m),
        lambda k, m: pr.R_ES_UW(ess, k, m),
        lambda k, m: pr.R_ES_N(ess, k, m)
    ]
    deltas = [dw.delta_ES['W'], dw.delta_ES['UW'], dw.delta_ES['N']]
    return create_eim(K, checks, deltas)

def create_eim_star(K, eims_checks, imes_checks, comp_weights):
    """Generic function to create EIM* matrices"""
    eim_star = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            eim_index = next((i for i, check in enumerate(eims_checks) if check(k, m)), len(eims_checks) - 1)
            imes_index = next((i for i, check in enumerate(imes_checks) if check(k, m)), None)
            eim_star[k, m] = comp_weights.iloc[eim_index, imes_index]
    return eim_star

def EIM_star_C_FSM(fsm, ess, comp_weights):
    K = fsm.shape[1]
    eims_checks = [
        lambda k, m: pr.RS_C_FSM(fsm, k, m),
        lambda k, m: pr.RW_C_FSM(fsm, k, m),
        lambda k, m: pr.RN_C_FSM(fsm, k, m)
    ]
    imes_checks = [
        lambda k, m: pr.R_ES_W(ess, k, m),
        lambda k, m: pr.R_ES_UW(ess, k, m),
        lambda k, m: pr.R_ES_N(ess, k, m)
    ]
    return create_eim_star(K, eims_checks, imes_checks, comp_weights)

def EIM_R_FSM(fsm):
    K = fsm.shape[1]
    checks = [
        lambda k, m: pr.RS_R_FSM(fsm, k, m),
        lambda k, m: pr.RUS_R_FSM(fsm, k, m),
        lambda k, m: pr.RW_R_FSM(fsm, k, m),
        lambda k, m: pr.RUW_R_FSM(fsm, k, m),
        lambda k, m: pr.RUN_R_FSM(fsm, k, m),
        lambda k, m: pr.RN_R_FSM(fsm, k, m)
    ]
    deltas = [dw.delta_FSM_R[key] for key in ['S', 'US', 'W', 'UW', 'UN', 'N']]
    return create_eim(K, checks, deltas)

def EIM_star_R_FSM(fsm, ess, comp_weights):
    K = fsm.shape[1]
    eims_checks = [
        lambda k, m: pr.RS_R_FSM(fsm, k, m),
        lambda k, m: pr.RUS_R_FSM(fsm, k, m),
        lambda k, m: pr.RW_R_FSM(fsm, k, m),
        lambda k, m: pr.RUW_R_FSM(fsm, k, m),
        lambda k, m: pr.RUN_R_FSM(fsm, k, m),
        lambda k, m: pr.RN_R_FSM(fsm, k, m)
    ]
    imes_checks = [
        lambda k, m: pr.R_ES_W(ess, k, m),
        lambda k, m: pr.R_ES_UW(ess, k, m),
        lambda k, m: pr.R_ES_N(ess, k, m)
    ]
    return create_eim_star(K, eims_checks, imes_checks, comp_weights)

def EIM_C_FIS(fis):
    K = fis.shape[1]
    checks = [
        lambda k, m: pr.RS_C_FIS(fis, k, m),
        lambda k, m: pr.RW_C_FIS(fis, k, m),
        lambda k, m: pr.RC_C_FIS(fis, k, m),
        lambda k, m: pr.RUC_C_FIS(fis, k, m),
        lambda k, m: pr.RN_C_FIS(fis, k, m)
    ]
    deltas = [dw.delta_FIS_C[key] for key in ['S', 'W', 'C', 'UC', 'N']]
    return create_eim(K, checks, deltas)

def EIM_star_C_FIS(fis, ess, comp_weights):
    K = fis.shape[1]
    eims_checks = [
        lambda k, m: pr.RS_C_FIS(fis, k, m),
        lambda k, m: pr.RW_C_FIS(fis, k, m),
        lambda k, m: pr.RC_C_FIS(fis, k, m),
        lambda k, m: pr.RUC_C_FIS(fis, k, m),
        lambda k, m: pr.RN_C_FIS(fis, k, m)
    ]
    imes_checks = [
        lambda k, m: pr.R_ES_W(ess, k, m),
        lambda k, m: pr.R_ES_UW(ess, k, m),
        lambda k, m: pr.R_ES_N(ess, k, m)
    ]
    return create_eim_star(K, eims_checks, imes_checks, comp_weights)

def EIM_R_FIS(fis):
    K = fis.shape[1]
    checks = [
        lambda k, m: pr.RS_R_FIS(fis, k, m),
        lambda k, m: pr.RUS_R_FIS(fis, k, m),
        lambda k, m: pr.RW_R_FIS(fis, k, m),
        lambda k, m: pr.RUW_R_FIS(fis, k, m),
        lambda k, m: pr.RC_R_FIS(fis, k, m),
        lambda k, m: pr.RUC_R_FIS(fis, k, m),
        lambda k, m: pr.RUN_R_FIS(fis, k, m),
        lambda k, m: pr.RN_R_FIS(fis, k, m)
    ]
    deltas = [dw.delta_FIS_R[key] for key in ['S', 'US', 'W', 'UW', 'C', 'UC', 'UN', 'N']]
    return create_eim(K, checks, deltas)

def EIM_star_R_FIS(fis, ess, comp_weights):
    K = fis.shape[1]
    eims_checks = [
        lambda k, m: pr.RS_R_FIS(fis, k, m),
        lambda k, m: pr.RUS_R_FIS(fis, k, m),
        lambda k, m: pr.RW_R_FIS(fis, k, m),
        lambda k, m: pr.RUW_R_FIS(fis, k, m),
        lambda k, m: pr.RC_R_FIS(fis, k, m),
        lambda k, m: pr.RUC_R_FIS(fis, k, m),
        lambda k, m: pr.RUN_R_FIS(fis, k, m),
        lambda k, m: pr.RN_R_FIS(fis, k, m)
    ]
    imes_checks = [
        lambda k, m: pr.R_ES_W(ess, k, m),
        lambda k, m: pr.R_ES_UW(ess, k, m),
        lambda k, m: pr.R_ES_N(ess, k, m)
    ]
    return create_eim_star(K, eims_checks, imes_checks, comp_weights)