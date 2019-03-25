# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    hemisphere_img = ["featured_image_url", "final_app_part1.png", "final_app_part2.png"]
    return render_template("index.html", list=team_list)


if __name__ == "__main__":
    app.run(debug=True)