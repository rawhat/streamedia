import asyncio
import json
import numpy as np
import soundcard as sc
import websockets

async def play():
  output = sc.default_speaker()
  # hard-coding the IP for now... this would obv need to be configured
  async with websockets.connect('ws://localhost:3000/') as ws:
    while True:
      message = await ws.recv()
      data = json.loads(message)
      arr = np.asarray(data, dtype=np.float32)
      output.play(data, samplerate=44100)

if __name__ == "__main__":
  asyncio.get_event_loop().run_until_complete(play())