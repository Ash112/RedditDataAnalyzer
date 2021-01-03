
from flask import Flask,request,render_template,flash,session

# imports the python definition from file
from process import initialvalue,defaulttreedata

from datascraper import scrapedata

# creates a Flask application, named app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'jf5j8gr54i8yjfei48687594rit8e496i9it'

# a route where we will intially render the main page with random values?
@app.route("/")
def hello():
    return render_template("index.html",
                           word_frequency = initialvalue,
                           time_frequency =initialvalue,
                           sentiment_frequency = initialvalue,
                           score_frequency= initialvalue,
                           allword_frequency = defaulttreedata,
                           allnumber_frequency = defaulttreedata,
                           allflair_frequency = defaulttreedata)

# a route that takes user inpur(Subreddit and Word) returns frequency over time data
@app.route('/', methods =["GET", "POST"])
def userinput():

    session.pop('_flashes', None)

    subreddit = ""
    word = "@#"
    ffilter = ""
    postcount = ""
    commentcount = ""
    replycount = ""

    word_time_frequency_data = [initialvalue,initialvalue,initialvalue,initialvalue,defaulttreedata,defaulttreedata,defaulttreedata]

    if request.method == "POST":
        #inputs

        # getting input with subredditname in HTML form
        subreddit = request.form.get("sname")
        # getting input with word name HTML form
        word = request.form.get("wname")
        # getting input with flari filter HTML form
        ffilter = request.form.get("ffilter")
        # getting input with post count HTML form
        postcount = request.form.get("pcount")
        # getting input with comment count HTML form
        commentcount = request.form.get("ccount")
        # getting input with reply count HTML form
        replycount = request.form.get("rcount")
        # to display on top of first chart
        worddata = " (" + str(word) + ")"

        #interger for comparison


        if word == "":

            word = "-None-"

        worddata = " (" + str(word) + ")"

        if (subreddit == "") or (postcount == "") or (commentcount == "") or (replycount == ""):

            outputmsg = "Enter Values to Proceed"

            flash("Enter Values to Proceed")

            print("Enter Values to Proceed")

            return render_template("index.html",
                           word_frequency = word_time_frequency_data[0],
                           time_frequency = word_time_frequency_data[1],
                           sentiment_frequency = word_time_frequency_data[2],
                           score_frequency = word_time_frequency_data[3],
                           allword_frequency = word_time_frequency_data[4],
                           allnumber_frequency = word_time_frequency_data[5],
                           allflair_frequency = word_time_frequency_data[6],
                           worddata = worddata,
                           outputmsg =outputmsg)


        if (int(postcount) > 5) or (int(commentcount) > 100) or (int(replycount) > 100):

            outputmsg = "Please keep Post,Comments & Reply counts within max limit"

            print("Please keep Post,Comments & Reply counts within max limit")

            flash("Please keep Post,Comments & Reply counts within max limit")

            render_template("index.html",
                           word_frequency = word_time_frequency_data[0],
                           time_frequency = word_time_frequency_data[1],
                           sentiment_frequency = word_time_frequency_data[2],
                           score_frequency = word_time_frequency_data[3],
                           allword_frequency = word_time_frequency_data[4],
                           allnumber_frequency = word_time_frequency_data[5],
                           allflair_frequency = word_time_frequency_data[6],
                           worddata = worddata,
                           outputmsg =outputmsg)

        else:
            #return processed output word frequency and timerange
            word_time_frequency_data = scrapedata(subreddit,word,postcount,commentcount,replycount,ffilter)

            outputmsg = "Success"

            flash("Success")

    return render_template("index.html",
                           word_frequency = word_time_frequency_data[0],
                           time_frequency = word_time_frequency_data[1],
                           sentiment_frequency = word_time_frequency_data[2],
                           score_frequency = word_time_frequency_data[3],
                           allword_frequency = word_time_frequency_data[4],
                           allnumber_frequency = word_time_frequency_data[5],
                           allflair_frequency = word_time_frequency_data[6],
                           worddata = worddata,
                           outputmsg =outputmsg)

# run the application
if __name__ == "__main__":

    # turn off debug when deploying
    app.run(debug=True)