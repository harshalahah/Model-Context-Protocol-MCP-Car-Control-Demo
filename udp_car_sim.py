# udp_car_sim.py
import socket

UDP_IP = "127.0.0.1"   # Localhost
UDP_PORT = 5005        # Port for car communication

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"🚗 Car simulator listening on {UDP_IP}:{UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(1024)  # Receive data (max 1024 bytes)
    command = data.decode().strip().upper()
    print(f"📩 Received command from {addr}: {command}")

    if command == "UNLOCK":
        reply = "✅ Car unlocked!"
    elif command == "LOCK":
        reply = "🔒 Car locked!"
    else:
        reply = "❌ Unknown command."

    # Send reply back
    sock.sendto(reply.encode(), addr)
    print(f"📤 Sent reply: {reply}")
