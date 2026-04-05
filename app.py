from flask import Flask, render_template, request, redirect
from database import init_db, insert_feedback, get_all_feedback

# 👇 FIX TEMPLATE PATH HERE
app = Flask(__name__, template_folder="../templates", static_folder="../static")

db_path = 'feedback.db'

def setup_db():
    init_db(db_path)

@app.route('/', methods=['GET'])
def index():
    feedbacks = get_all_feedback(db_path)
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    feedback = request.form.get('feedback')
    if name and feedback:
        insert_feedback(db_path, name, feedback)
    return redirect('/')

if __name__ == '__main__':
    setup_db()
    app.run(host='0.0.0.0', port=5000, debug=True)