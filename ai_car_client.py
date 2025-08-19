import requests
from openai import OpenAI

# 1. OpenAI API setup (replace with your key)
client = OpenAI(api_key="YOUR_API_KEY")

# 2. Function to send AI a prompt
def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Small, fast model
            messages=[
                {"role": "system", "content": "You are a car control AI. Reply only with 'lock' or 'unlock'."},
                {"role": "user", "content": prompt}
            ]
        )
        ai_reply = response.choices[0].message.content.strip().lower()
        return ai_reply
    except Exception as e:
        return "error"

# 3. Function to call your car server
def control_car(action):
    # Construct the URL for the car control server and pass the action as payload
    url = f"http://127.0.0.1:8000/set_car_state"  # Local Stage 1 server URL
    try:
        r = requests.post(url, json={"state": action.capitalize()})
        print(f"Car {action} command sent. Server says: {r.text}")
    except Exception as e:
        print(f"Failed to send car command: {e}")

# 4. Main loop
while True:
    user_input = input("\nAsk AI (or type 'quit'): ")
    if user_input.lower() == "quit":
        break

    decision = ask_ai(user_input)
    if decision in ["lock", "unlock"]:
        control_car(decision)
    else:
        print("AI did not understand. Got:", decision)
