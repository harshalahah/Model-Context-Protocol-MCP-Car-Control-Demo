# mcp_car_server.py
from mcp.server.fastmcp import FastMCP
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

mcp = FastMCP("Car Control MCP Server")

def send_udp_command(command):
    """Send UDP command to car simulator and get reply."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
    try:
        data, _ = sock.recvfrom(1024)
        return data.decode()
    except socket.timeout:
        return "❌ No response from car."
    finally:
        sock.close()

@mcp.tool()
def unlock_car() -> str:
    """Unlocks the car via UDP command."""
    return send_udp_command("UNLOCK")

@mcp.tool()
def lock_car() -> str:
    """Locks the car via UDP command."""
    return send_udp_command("LOCK")

if __name__ == "__main__":
    mcp.run()
