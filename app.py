import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name1 = request.form["name1"]
        name2 = request.form["name2"]
        prof1 = request.form["prof1"]
        prof2 = request.form["prof2"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name1, name2, prof1, prof2),
            temperature=1,
            max_tokens=256,
            n=1
        )
        result = response.choices[0].text.strip()
        return redirect(url_for("result", result=result))
    
    return render_template("index.html")


@app.route("/result")
def result():
    result = request.args.get("result")
    return render_template("result.html", result=result)


def generate_prompt(name1, name2, prof1, prof2):
    return """Write vows for the marriage of {} and {}, from the perspective of {}.
This is how they met: {}
This is what {} loves about {}: {}
Names:""".format(
        name1.capitalize(),
        name2.capitalize(),
        name1.capitalize(),
        prof1.capitalize(), name1.capitalize(),
        name2.capitalize(), prof2.capitalize()
    )


if __name__ == "__main__":
    app.run()
