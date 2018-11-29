defmodule Server.Listener do
  use GenServer

  def start_link(port \\ 3000) do
    IO.puts "starting udp server..."
    GenServer.start_link(__MODULE__, port)
  end

  def init(port) do
    IO.puts "opening UDP port"
    :gen_udp.open(port, [:binary, active: true])
  end

  def handle_info({:udp, _socket, _address, _port, data}, socket) do
    IO.puts "here"
    IO.inspect data
    {:noreply, socket}
  end
end