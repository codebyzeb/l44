from scipy import stats

f1 = input()
f2 = input()

def get_microscores(filename):
    scores = []
    for line in open(filename, 'r'):
        if line[0:2] == "11":
            scores.append(float("0."+line.split('0.')[-1].strip())*100)
    return scores[:-1]

def get_macroscores(filename):
    scores = []
    for line in open(filename, 'r'):
        if line[0:2] == "12":
            scores.append(float("0."+line.split('0.')[-1].strip())*100)
    return scores[:-1]

print("micro:")
tStat, pValue = stats.ttest_ind(get_microscores(f1), get_microscores(f2), equal_var=False)
print("t: {}, p: {}".format(tStat, pValue))

print("macro:")
tStat, pValue = stats.ttest_ind(get_macroscores(f1), get_macroscores(f2), equal_var=False)
print("t: {}, p: {}".format(tStat, pValue))
