# car_control_server.py
from flask import Flask, jsonify, request
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

app = Flask(__name__)

def send_udp_command(command):
    """Send a command to the car simulator and return its reply."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
    try:
        data, _ = sock.recvfrom(1024)
        response = data.decode()
        return response
    except socket.timeout:
        return "❌ No response from car."
    finally:
        sock.close()

@app.route("/set_car_state", methods=["POST"])
def set_car_state():
    data = request.json
    state = data.get("state")
    if state == "Lock":
        result = send_udp_command("LOCK")
    elif state == "Unlock":
        result = send_udp_command("UNLOCK")
    else:
        return jsonify({"error": "Invalid state. Use 'Lock' or 'Unlock'."}), 400
    return jsonify({"status": result})

if __name__ == "__main__":
    print("🚀 Car Control Server running at http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000)