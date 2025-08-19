# Model-Context-Protocol-MCP-Car-Control-Demo
A learning project exploring how to bridge AI with external systems.  Includes two versions:  
  1) A simple OpenAI API → UDP bridge
  2) A full MCP server tested with Claude Desktop.

# What is MCP?

Model Context Protocol (MCP) is a new open standard (created by Anthropic, late 2024) that allows AI models to connect to external tools and data sources in a structured way.
Think of it like a USB port for AI assistants -- instead of custom code for every tool, MCP provides a standard interface.
AI can then call functions like 'unlock car' or 'check database' safely and consistently.

# 🚗 Model Context Protocol (MCP) Car Control Demo

This project is a **learning showcase** of how to connect AI models to external systems using both a simple bridge and a real MCP server.  
The example: a *fake car* that can be locked or unlocked.

We built it in **two stages**:

## 🔑 Version 1 — OpenAI API → UDP Bridge
In this stage, we created:
- A **UDP Car Simulator** — a Python program acting as a fake car listening for `LOCK`/`UNLOCK` commands.
- A **Flask HTTP → UDP Bridge** — so that AI (or even `curl`) could call a simple HTTP endpoint, which then talks to the UDP car.

### Test Commands
Run the UDP car simulator:
```bash
python udp_car_sim.py
````

In another terminal, unlock the car:

```bash
python -c "import socket; s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.sendto(b'UNLOCK',( '127.0.0.1',5005 )); print(s.recvfrom(1024)[0].decode())"
```

Run the bridge server:

```bash
python car_control_server.py
```

Then try:

```bash
curl http://127.0.0.1:8000/unlock_car
```

> 📝 We used **Flask** because it makes Python functions callable via HTTP without heavy setup.

---

## 🔑 Version 2 — Real MCP Server with Claude

In this stage, we upgraded to a **proper MCP server** using the [`fastmcp`](https://github.com/modelcontextprotocol/fastmcp) library.
This let us connect directly with **Claude Desktop (MCP-enabled)**, so the AI could issue `LOCK`/`UNLOCK` commands natively.

### Files

* `server.py` → the MCP server implementation
* `mcp.json` → config file used by Claude Desktop

### How it Works

1. Claude asks the MCP server to run a command.
2. The server sends UDP messages to the fake car.
3. The car simulator responds back with success/failure.

## ⚠️ Notes

* **API Keys:** If you experiment with OpenAI API, never hardcode your keys into code. Use environment variables.
* This is **for learning/demo purposes only** (simulated car, not a real one).
* MCP is a new standard — this project is meant as an introduction, not production code.

## 📚 What I Learned

* Basics of **TCP vs UDP networking**
* How to build a **Flask bridge server**
* How **MCP servers integrate with AI tools**
* Safe handling of **API keys and configs**

## 🚀 Next Steps

* Expand to more car commands (start/stop, lights, etc.)
* Try connecting other devices via MCP
* Explore multi-client handling with threading

✨ *This repo is part of my learning journey with AI, networking, and the new MCP ecosystem.*
