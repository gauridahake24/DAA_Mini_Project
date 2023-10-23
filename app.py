# app.py
from flask import Flask, render_template, request
from processing_code import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        jobs = int(request.form['jobs'])
        length = int(request.form['length'])
        all_cases = request.form['all_cases'] == 'Y'

        conclusion = []
        print(f"Using {jobs} cores\n")

        if all_cases:
            l = 1
            while l < 10 ** 5:
                main(jobs, l, conclusion)
                l *= 10
        else:
            main(jobs, length, conclusion)

        return render_template('index.html', conclusion=conclusion)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
