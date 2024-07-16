import numpy as np
from isolability import pairwise_relationships as pr
import conf.delta_weights as dw

def EIM_C_FSM(fsm):
    K = fsm.shape[1]
    eim = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            if pr.RS_C_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_C['S']
            elif pr.RW_C_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_C['W']
            elif pr.RN_C_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_C['N']
    return eim

def C_Delta(eim):
    K = eim.shape[0]
    return eim.sum()/K/(K-1)

def C_star_Delta(eim):
    eim = np.minimum(eim, 1)
    return C_Delta(eim)

def IMES(ess):
    K = len(ess.keys())
    imes = np.zeros((K, K)) 
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            if pr.R_ES_W(ess, k, m):
                imes[k, m] = dw.delta_ES['W']
            elif pr.R_ES_UW(ess, k, m):
                imes[k, m] = dw.delta_ES['UW']
            elif pr.R_ES_N(ess, k, m):
                imes[k, m] = dw.delta_ES['N']
    return imes

def EIM_star_C_FSM(fsm, ess, comp_weights):
    K = fsm.shape[1]
    eim_star = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            eims = [pr.RS_C_FSM(fsm, k, m), pr.RW_C_FSM(fsm, k, m), pr.RN_C_FSM(fsm, k, m)]
            imes = [pr.R_ES_W(ess, k, m), pr.R_ES_UW(ess, k, m), pr.R_ES_N(ess, k, m)]
            eim_index = next((i for i, x in enumerate(eims) if x), None)
            imes_index = next((i for i, x in enumerate(imes) if x), None)
            eim_star[k, m] = comp_weights.iloc[eim_index, imes_index]
    return eim_star

def EIM_R_FSM(fsm):
    K = fsm.shape[1]
    eim = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            if pr.RS_R_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_R['S']
            elif pr.RUS_R_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_R['US']
            elif pr.RW_R_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_R['W']
            elif pr.RUW_R_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_R['UW']
            elif pr.RUN_R_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_R['UN']
            elif pr.RN_R_FSM(fsm, k, m):
                eim[k, m] = dw.delta_FSM_R['N']
    return eim

def EIM_star_R_FSM(fsm, ess, comp_weights):
    K = fsm.shape[1]
    eim_star = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            eims = [pr.RS_R_FSM(fsm, k, m), pr.RUS_R_FSM(fsm, k, m), pr.RW_R_FSM(fsm, k, m), pr.RUW_R_FSM(fsm, k, m), pr.RUN_R_FSM(fsm, k, m), pr.RN_R_FSM(fsm, k, m)]
            imes = [pr.R_ES_W(ess, k, m), pr.R_ES_UW(ess, k, m), pr.R_ES_N(ess, k, m)]
            eim_index = next((i for i, x in enumerate(eims) if x), None)
            imes_index = next((i for i, x in enumerate(imes) if x), None)
            eim_star[k, m] = comp_weights.iloc[eim_index].iloc[imes_index]
    return eim_star

def EIM_C_FIS(fis):
    K = fis.shape[1]
    eim = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            if pr.RS_C_FIS(fis, k, m):
                eim[k, m] = dw.delta_FIS_C['S']
            elif pr.RW_C_FIS(fis, k, m):
                eim[k, m] = dw.delta_FIS_C['W']
            elif pr.RC_C_FIS(fis, k, m):
                eim[k, m] = dw.delta_FIS_C['C']
            elif pr.RUC_C_FIS(fis, k, m):
                eim[k, m] = dw.delta_FIS_C['UC']
            elif pr.RN_C_FIS(fis, k, m):
                eim[k, m] = dw.delta_FIS_C['N']
    return eim

def EIM_star_C_FIS(fis, ess, comp_weights):
    K = fis.shape[1]
    eim_star = np.zeros((K, K))
    for k in range(K):
        for m in range(K):
            if k == m:
                continue
            eims = [pr.RS_C_FIS(fis, k, m), pr.RW_C_FIS(fis, k, m), pr.RC_C_FIS(fis, k, m), pr.RUC_C_FIS(fis, k, m), pr.RN_C_FIS(fis, k, m)]
            imes = [pr.R_ES_W(ess, k, m), pr.R_ES_UW(ess, k, m), pr.R_ES_N(ess, k, m)]
            eim_index = next((i for i, x in enumerate(eims) if x), 4) # pair not fitting any definition are treated as N
            imes_index = next((i for i, x in enumerate(imes) if x), None)
            print(k, m)
            print(eim_index)
            print(imes_index)
            eim_star[k, m] = comp_weights.iloc[eim_index, imes_index]
    return eim_star
            