require "kemal"
require "socket"

class Listener
  def initialize
    @client = UDPSocket.new
    @client.bind "localhost", 3001
    @listen = true
  end

  def listen_for_packet(socket)
    # puts "before loop"
    if @listen
      message, addr = @client.receive
      # puts "got message: #{message}"
      socket.send message
      listen_for_packet(socket)
    end
  end

  def unlisten
    @listen = false
  end
end

listener = Listener.new

ws "/socket" do |socket|
  socket.on_close do
    listener.unlisten()
  end

  spawn do
    listener.listen_for_packet(socket)
  end
end

Kemal.config.port = 8080
Kemal.run
sleep