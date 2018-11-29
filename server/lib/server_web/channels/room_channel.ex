defmodule ServerWeb.RoomChannel do
  use Phoenix.Channel

  def join("room:" <> _id, _params, socket) do
    IO.puts "new user joined!"
    {:ok, socket}
  end
end
