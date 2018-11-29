import socket
import soundcard as sc
import sys

# UDP_IP_ADDR = "255.255.255.255"
UDP_IP_ADDR = "192.168.173.191"
UDP_PORT_NO = 3001

def run():
  print("connecting to socket server")
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  print("getting all microphones")
  all_microphones = sc.all_microphones(include_loopback=True)
  print("got all microphones: {}".format(all_microphones))
  loopback = next((microphone for microphone in all_microphones if microphone.isloopback and microphone.name.find('Speakers') != -1), None)
  if loopback is None:
    print("No loopback device detected, exiting...")
    exit(1)
  print("Found a loopback microphone with: {}".format(loopback))
  with loopback.recorder(samplerate=44100, channels=2) as mic:
    while True:
      try:
        data = mic.record()
        byte = data.tobytes()
        print(byte)
        sys.stdout.flush()
        # client.sendto(byte, (UDP_IP_ADDR, UDP_PORT_NO))
        # mic.flush()
      except Exception as e:
        print("Uh oh... failed: {}".format(e))
        exit(1)

if __name__ == "__main__":
  run()