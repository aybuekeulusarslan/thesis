from scipy.stats import ks_2samp

def ks_test(data1,data2):
    [stat,p] = ks_2samp(data1,data2)
    return [stat,p]