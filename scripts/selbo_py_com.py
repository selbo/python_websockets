#!/usr/bin/env python

'''
https://pypi.python.org/pypi/websocket-client/
https://github.com/liris/websocket-client
'''


import websocket
import thread
import time

def on_message(ws, message):
	print "### inside on_message ###"
	print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
	print "### opening a new thread that pings the server 3 times"
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    print "### opening web socket ###"
    ws = websocket.WebSocketApp("ws://104.198.196.211:8000",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    print "### web socket successfully opened ###"
    ws.on_open = on_open
    ws.run_forever()
