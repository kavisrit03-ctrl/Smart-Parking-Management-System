from flask import Flask, render_template, request, redirect

app = Flask(__name__)

parking_slots = [
    {"id": 1, "status": "Available"},
    {"id": 2, "status": "Available"},
    {"id": 3, "status": "Available"},
    {"id": 4, "status": "Available"},
    {"id": 5, "status": "Available"}
]

@app.route('/')
def home():
    return render_template('index.html', slots=parking_slots)

@app.route('/book/<int:slot_id>')
def book_slot(slot_id):
    for slot in parking_slots:
        if slot["id"] == slot_id and slot["status"] == "Available":
            slot["status"] = "Occupied"
    return redirect('/')

@app.route('/release/<int:slot_id>')
def release_slot(slot_id):
    for slot in parking_slots:
        if slot["id"] == slot_id:
            slot["status"] = "Available"
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    