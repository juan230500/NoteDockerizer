from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
NOTES_FILE = "/data/notes.txt"

if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, 'w') as f:
        pass

@app.route('/')
def index():
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    return render_template('index.html', notes=notes)

@app.route('/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        note = request.form.get('note')
        with open(NOTES_FILE, 'a') as f:
            f.write(note + "\n")
        return redirect('/')
    return render_template('create.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
