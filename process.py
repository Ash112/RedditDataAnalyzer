import random
import json

# generate intial zero values
def initialvalue():
    initalval =[]
    for x in range(10):
        initalval.append(0)

    return json.dumps(initalval)

# generate random data
def senddata(subredditname,wordname):

    frequency_time_data = []
    word__frequency_data = []
    timeframe__frequency_data = []

    for x in range(len(subredditname)):
        word__frequency_data.append(random.randrange(0, 30, 1))

    for x in range(len(wordname)):
        timeframe__frequency_data.append(random.randrange(0, 10, 1))

    #frequency_time_data=[word__frequency_data,timeframe__frequency_data]

    return json.dumps(word__frequency_data),json.dumps(timeframe__frequency_data)



