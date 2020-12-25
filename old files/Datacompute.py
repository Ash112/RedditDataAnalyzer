
from IPython.display import display

import pandas

from Datascrap import I_date,I_frequency,end,start,I_wordtocount,I_sentpolarity,I_sentsubjectivity,I_score,I_type

# --------------------------------------------------------------------------------#
print("Total Posts,Comments & Replies = " + str(len(I_date)) + "\n")

print("There are - " + str(sum(I_frequency)) + " mentions of " + "| " + I_wordtocount + " |" + "\n")

print("Time taken to run =" + str(end - start) + "\n")

# --------------------------------------------------------------#

# Average polarity calculations(Overall)

actualvaluespol = (len(I_sentpolarity) - (I_sentpolarity.count(0)))

sumpolarity = sum(I_sentpolarity)

avgpolarity = sumpolarity / actualvaluespol

print('Average polarity = ' + str(avgpolarity) + "\n")

# Average subjectivity calculations(Overall)

actualvaluessub = (len(I_sentsubjectivity) - (I_sentsubjectivity.count(0)))

sumsubjectivity = sum(I_sentsubjectivity)

avgsubjectivty = sumsubjectivity / actualvaluessub

print('Average Subjectivity = ' + str(avgsubjectivty))

# --------------------------------------------------------------#
# all data
data = {'Dates': I_date, 'Frequency': I_frequency, 'Sentiment_Polarity': I_sentpolarity,
        'SentSubjectivity': I_sentsubjectivity, 'Score': I_score, 'Type': I_type}

table = pandas.DataFrame(data)

with pandas.option_context('display.max_rows', None, 'display.max_columns', None):

   display(table)

print(table)
# --------------------------------------------------------------#
# grouped data for hourly plots

I_hourlydate = []

for date in I_date:
    # I_hourlydate.append(str(date.year)+"."+ str(date.month)+"."+ str(date.day)+"-"+str(date.hour))

    newdate = (str(date.year) + str(date.month) + str(date.day) + str(date.hour))

    I_hourlydate.append(int(newdate))

groupeddata = {'Dates': I_hourlydate, 'Frequency': I_frequency, 'Sentiment_Polarity': I_sentpolarity,
               'SentSubjectivity': I_sentsubjectivity, 'Score': I_score}

tablegrouped = pandas.DataFrame(groupeddata)

grouptedtable = tablegrouped.groupby('Dates').sum()

with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
    display(grouptedtable)

# ---------------------------------------------------------------------------------------#
