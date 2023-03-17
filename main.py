from flask import Flask, render_template
import requests
import json


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        response = get_response() # gets the json response
        if is_up(response): # checks if response is valid
            meme_pic, subreddit, title = get_meme(response) # gets values out of response
            # Sets values in html of the response
            return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, title=title)
        else:
            return render_template("apidown.html") # if the api is down show error page
    return app


# Checks if Api is up by checking if there is a code in response
# Also checks if the values needed in the reps once is included in the response
def is_up(response):
    if 'code' in response:
        return False
    elif 'preview' and 'subreddit' and 'title' in response:
        return True
    else:
        return False


# Gets Response from the meme api located at meme-api.com
def get_response():
    # Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddt
    # sr = "/wholesomememes"
    # url = "<https://meme-api.herokuapp.com/gimme>" + sr
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    return response


# Decodes the json response into variables
def get_meme(response):
    meme_large = response["preview"][2]
    subreddit = response["subreddit"]
    title = response["title"]
    return meme_large, subreddit, title
