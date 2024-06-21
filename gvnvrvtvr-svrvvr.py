import random
from FoxDot import *
import asyncio
import websockets
import logging
import sys
import nest_asyncio


# Define some musical patterns
patterns = [
    P[0, 2, 4, 5],
    P[0, 3, 7, 10],
    P[0, 1, 5, 8]
]


# Define a function to generate FoxDot code
def generate_foxdot_code():
    pattern = random.choice(patterns)
    dur = random.choice([0.25, 0.5, 1])
    amp = random.choice([0.5, 0.7, 1])
    synth = random.choice(['pluck', 'pads', 'bass'])
    
    foxdot_code = f"""
{random.choice(['p1', 'p2', 'p3'])} >> {synth}(var({pattern}, {dur}), amp={amp})
"""
    return foxdot_code


# Generate and print some FoxDot code
print(generate_foxdot_code())

# WebSocket handler
async def send_foxdot_code(websocket, path):
    while True:
        foxdot_code = generate_foxdot_code()
        logging.info(f"Sending: {foxdot_code.strip()}")
        await websocket.send(foxdot_code)
        await asyncio.sleep(10)  # Adjust the interval as needed

# Start the WebSocket server
start_server = websockets.serve(send_foxdot_code, "localhost", 8765)

# Run the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()