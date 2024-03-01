
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize an empty list to store notes
notes = []

@app.route('/', methods=["GET", "POST"])  # Allow POST method for form submission
def index():
    if request.method == "POST":
        # Retrieve note from form submission
        note = request.form.get("note")
        if note:
            # Append note to the notes list
            notes.append(note)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
