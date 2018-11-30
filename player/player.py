import numpy as np
import socket
import soundcard as sc

def play():
  all_speakers = sc.all_speakers()
  output = all_speakers[1]

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('', 3001))
  sock.listen(1)
  conn, addr = sock.accept()

  player = output.player(44100)
  player.__enter__()
  while True:
    data = conn.recv(1024)
    arr = np.frombuffer(data, dtype=np.float32)
    player.play(arr)
  conn.close()

if __name__ == "__main__":
  play()