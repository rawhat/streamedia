import numpy as np
import socket
import soundcard as sc

def play():
  all_speakers = sc.all_speakers()
  # print(all_speakers)
  output = all_speakers[1]
  # output = sc.default_speaker()
  print(output)
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind(('', 3001))
  player = output.player(44100)
  player.__enter__()
  while True:
    data, addr = sock.recvfrom(1024)
    # arr = np.frombuffer(data, dtype=np.dtype('d'))
    arr = np.frombuffer(data, dtype=np.float32)
    player.play(arr)
    # output.play(arr, 44100)

if __name__ == "__main__":
  play()