from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


feedbacks = []

# Home route (IMPORTANT for fixing "Not Found")
@app.route("/")
def home():
    return render_template("index.html", feedbacks=feedbacks)

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    feedback = request.form.get("feedback")

    if name and feedback:
        feedbacks.append((name, feedback))

    return redirect(url_for("home"))  # Redirect to home after submit

# Run app (for local + Render compatibility)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)