class SimpleReflexAgent:
    def __init__(self, temp):
        self.desired_temp = temp
    
    def percept(self, temp):
        self.current_temp = temp
    
    def act(self):
        if self.current_temp > self.desired_temp:
            return "Turn off the heater"
        else:
            return "Turn on the heater"


room = {
    "Living room": 28,
    "Bed room": 18,
    "Kitchen": 32,
}

agent = SimpleReflexAgent(22)

# Correct loop to go through each room and its temperature
for room_name, temp in room.items():
    agent.percept(temp)  # Pass the temperature to the agent
    print(f"{room_name} (Temp: {temp}) ==> {agent.act()}")
