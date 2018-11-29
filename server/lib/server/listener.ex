defmodule Server.Listener do
  use GenServer

  def start_link(port \\ 3000) do
    IO.puts "starting udp server..."
    GenServer.start_link(__MODULE__, port)
  end

  def init(port) do
    IO.puts "opening UDP port"
    {:ok, listener} = :gen_udp.open(port, [:binary, active: true])
    {:ok, player} = :gen_udp.open(3001, [:binary, active: true])
    {:ok, %{"listener" => listener, "player" => player}}
  end

  def handle_info({:udp, _socket, _address, _port, data}, %{"listener" => _listener, "player" => player} = state) do
    :gen_udp.send(player, {127,0,0,1}, 3001, data)
    {:noreply, state}
  end
end