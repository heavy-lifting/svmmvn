import asyncio
import websockets
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

async def receive_foxdot_code():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            foxdot_code = await websocket.recv()
            logging.info(f"Received: {foxdot_code.strip()}")
            # Optionally execute the received FoxDot code
            # exec(foxdot_code)

asyncio.get_event_loop().run_until_complete(receive_foxdot_code())