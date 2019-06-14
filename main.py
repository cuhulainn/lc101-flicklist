from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# a form for crossing off watched movies
crossoff_form = """
    <br>
    <br>
    <form action="/crossoff" method="post">
            <label for="movie-to-cross-off">
                I want to cross off
                <select name="movie-to-cross-off">
                    <option value="Star Wars">Star Wars</option>
                    <option value="Clerks">Clerks</option>
                    <option value="Alien">Alien</option>
                </select>
                from my watchlist.
            </label>
            <input type="submit" value="Cross It Off"/>
        </form>
"""


@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['movie-to-cross-off']
    
    # build response content
    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    sentence = crossed_off_movie_element + " has been crossed off your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer
    
    return content 

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # build the response string
    content = page_header + edit_header + add_form + crossoff_form + page_footer

    return content


app.run()
