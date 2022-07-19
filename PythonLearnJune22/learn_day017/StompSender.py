import stomp

host = "localhost"
port = 61613

message_body = "This is my first test message from Python"

conn = stomp.Connection(host_and_ports=[(host, port)])
conn.connect()
conn.send(destination="/queue/TEST.H2KINFOSYS", body=message_body, persistent='true')
conn.disconnect()