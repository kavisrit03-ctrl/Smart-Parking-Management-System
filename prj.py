from flask import Flask, render_template, request, redirect

app = Flask(__name__)

slots = {
    "P1": {"status": "Available", "vehicle": "", "fee": 0},
    "P2": {"status": "Available", "vehicle": "", "fee": 0},
    "P3": {"status": "Available", "vehicle": "", "fee": 0},
    "P4": {"status": "Available", "vehicle": "", "fee": 0},
    "P5": {"status": "Available", "vehicle": "", "fee": 0},
    "P6": {"status": "Available", "vehicle": "", "fee": 0},
    "P7": {"status": "Available", "vehicle": "", "fee": 0},
    "P8": {"status": "Available", "vehicle": "", "fee": 0},
    "P9": {"status": "Available", "vehicle": "", "fee": 0},
    "P10": {"status": "Available", "vehicle": "", "fee": 0}
}

@app.route('/')
def dashboard():
    occupied = 0

    for slot in slots.values():
        if slot["status"] == "Occupied":
            occupied += 1

    available = len(slots) - occupied

    return render_template(
        'dashboard.html',
        slots=slots,
        available=available,
        occupied=occupied
    )

@app.route('/book/<slot>', methods=['POST'])
def book(slot):
    vehicle = request.form['vehicle']
    hours = int(request.form['hours'])

    fee = hours * 20

    slots[slot]["status"] = "Occupied"
    slots[slot]["vehicle"] = vehicle
    slots[slot]["fee"] = fee

    return redirect('/')

@app.route('/release/<slot>')
def release(slot):
    slots[slot]["status"] = "Available"
    slots[slot]["vehicle"] = ""
    slots[slot]["fee"] = 0

    return redirect('/')

@app.route('/search', methods=['POST'])
def search():
    vehicle = request.form['vehicle']

    for slot, details in slots.items():
        if details["vehicle"] == vehicle:
            return f"Vehicle {vehicle} found in {slot}"

    return "Vehicle not found"

@app.route('/admin')
def admin():
    occupied = 0

    for slot in slots.values():
        if slot["status"] == "Occupied":
            occupied += 1

    available = len(slots) - occupied
    total_slots = len(slots)

    return render_template(
        'admin.html',
        available=available,
        occupied=occupied,
        total_slots=total_slots
    )

if __name__ == '__main__':
    app.run(debug=True)
