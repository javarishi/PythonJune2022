import stomp
import time

class MyListener:

    def __init__(self, conn):
        self.connection = conn
        print("Connection is created")

    def on_error(self, message):
        print("Error occurred at {}".format(message))

    def on_message(self, message):
        print("Message received ")
        print(message.headers)
        print(message.body)


host = "localhost"
port = 61613

conn = stomp.Connection(host_and_ports=[(host, port)])
conn.set_listener("H2KMessageListener", MyListener(conn))
conn.connect()
conn.subscribe(destination="/queue/TEST.H2KINFOSYS", id=1, ack="auto")
while True:
    time.sleep(2)