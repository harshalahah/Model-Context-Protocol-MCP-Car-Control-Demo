from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Car MCP Server")

# Store car state (locked/unlocked)
car_state = {"locked": True}

@mcp.tool()
def get_state() -> str:
    """
    Returns the current lock state of the car.
    """
    return "locked" if car_state["locked"] else "unlocked"

@mcp.tool()
def set_state(state: str) -> str:
    """
    Changes the lock state of the car.
    Accepted values: "locked" or "unlocked".
    """
    state = state.lower()
    if state not in ["locked", "unlocked"]:
        return "Invalid state. Use 'locked' or 'unlocked'."

    car_state["locked"] = (state == "locked")
    return f"Car is now {state}."

if __name__ == "__main__":
    mcp.run()
