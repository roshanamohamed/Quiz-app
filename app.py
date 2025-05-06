from flask import Flask, render_template, request # type: ignore
import json

app = Flask(__name__)

# Load questions from JSON file
def load_questions():
    with open('quiz_data.json', 'r') as f:
        return json.load(f)

@app.route('/')
def quiz():
    quiz_data = load_questions()
    return render_template("quiz.html", quiz=quiz_data)

@app.route('/submit', methods=['POST'])
def submit():
    quiz_data = load_questions()
    score = 0
    results = []

    for i, question in enumerate(quiz_data):
        selected = request.form.get(f'q{i}')
        correct = selected == question["answer"]
        results.append({
            "question": question["question"],
            "selected": selected,
            "correct": question["answer"],
            "is_correct": correct
        })
        if correct:
            score += 1

    return render_template("result.html", score=score, total=len(quiz_data), results=results)

if __name__ == "__main__":
    app.run(debug=True)
