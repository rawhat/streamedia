import socket
import soundcard as sc
import sys
import wave

TCP_IP_ADDR = "192.168.173.191"
# TCP_IP_ADDR = "127.0.0.1"
TCP_PORT_NO = 3001

def run():
  print("connecting to socket server")
  # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # client.connect((TCP_IP_ADDR, TCP_PORT_NO))
  print("getting all microphones")
  # all_microphones = sc.all_microphones(include_loopback=True)
  # print("got all microphones: {}".format(all_microphones))
  # loopback = next((microphone for microphone in all_microphones if microphone.isloopback and microphone.name.find('Speakers') != -1), None)
  loopback = sc.default_microphone()
  if loopback is None:
    print("No loopback device detected, exiting...")
    exit(1)
  print("Found a loopback microphone with: {}".format(loopback))
  try:
    with loopback.recorder(samplerate=44100, channels=2) as mic:#, wave.open('test.wav', 'wb') as wav:
      # wav.setparams((1, 2, 44100, 0, 'NONE', 'NONE'))
      spk = next(speaker for speaker in sc.all_speakers() if speaker.name.find('ODAC') != -1)
      print(spk)
      # mic.__enter__()
      # while True:
      while True:
        try:
          data = loopback.record(1024, 44100)
          spk.play(data, 44100)
          # byte = data.tobytes()
          # wav.writeframes(byte)
          # mic.flush()
          # byte = bytes('testing', 'utf-8')
          # client.send(byte)
          # sys.stdout.flush()
          # client.sendto(byte, (UDP_IP_ADDR, UDP_PORT_NO))
          # mic.flush()
        except Exception as e:
          print("Uh oh... failed: {}".format(e))
          exit(1)
  except KeyboardInterrupt:
    # client.close()
    wav.close()

if __name__ == "__main__":
  run()