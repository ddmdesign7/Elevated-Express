from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/track', methods=['POST'])
def track():
    tracking_number = request.form['tracking_number']
    
    if tracking_number == "gm123456770":
        status = "Package is on its way 🚚"
        checkpoints = [
            {"date": "2026-08-25", "location": "Lagos Facility", "message": "Shipment accepted"},
            {"date": "2026-08-26", "location": "Ibadan Hub", "message": "In transit"},
            {"date": "2026-08-27", "location": "Oyo State", "message": "Out for delivery"},
        ]
    else:
        status = "Tracking number not found ❌"
        checkpoints = []
    
    return render_template("result.html", tracking_number=tracking_number, status=status, checkpoints=checkpoints)

if __name__ == "__main__":
    app.run(debug=True)
