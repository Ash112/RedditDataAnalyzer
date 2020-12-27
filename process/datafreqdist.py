
from matplotlib import rcParams

import pandas

from nltk import FreqDist

#inputs----------------------------------------------------------------------------#

from datascraper import I_allwords

# figure size in inches
rcParams['figure.figsize'] = 20, 20

frequentwords = []

frequentwordscount = []

# -------------------------------------------------------------------------------#

fdist = FreqDist(I_allwords)

sorted_dict = {}

sorted_keys = sorted(fdist, key=fdist.get)

for w in sorted_keys:
    sorted_dict[w] = fdist[w]

dictwords = dict(reversed(list(sorted_dict.items())))
# -------------------------------------------------------------------------------#

for keys, values in dictwords.items():

    frequentwords.append(keys)

    frequentwordscount.append(values)

    # print(keys,values)

# -------------------------------------------------------------------------------#

frequencydata = {'Frequency': frequentwordscount[:100], 'Words': frequentwords[:100]}

freqtable = pandas.DataFrame(frequencydata)

with pandas.option_context('display.max_rows', 5, 'display.max_columns', None):
    print(freqtable)

fdist.plot(50, cumulative=False)
