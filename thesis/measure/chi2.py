from scipy.stats import chi2_contingency

def chi2_test(data):
    def get_contingency(data):
        contingency = []
        for label in set(data):
            contingency.append(len([i for i in data if i == label]))

    contingency = get_contingency(data)
    [stat,p] = chi2_contingency(contingency)
    return [stat,p]