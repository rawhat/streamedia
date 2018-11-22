import asyncio
import json
import soundcard as sc
import websockets

async def run():
    async with websockets.connect('ws://localhost:3000/') as ws:
        print("getting all microphones")
        all_microphones = sc.all_microphones(include_loopback=True)
        print("got all microphones: {}".format(all_microphones))
        loopback = next((microphone for microphone in all_microphones if microphone.isloopback and microphone.name.find('Speakers') != -1), None)
        if loopback is None:
                print("No loopback device detected, exiting...")
                exit(1)
        print("Found a loopback microphone with: {}".format(loopback))
        with loopback.recorder(samplerate=44100) as mic:
                while True:
                        try:
                                data = mic.record()
                                # print("Got data: {}".format(data))
                                print("sending data")
                                await ws.send(json.dumps(data.tolist()))
                        except Exception as e:
                                print("Uh oh... failed: {}".format(e))
                                exit(1)

if __name__ == "__main__":
        asyncio.get_event_loop().run_until_complete(run())
