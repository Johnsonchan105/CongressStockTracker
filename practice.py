from dotenv import load_dotenv
import os
import websocket
import finnhub

load_dotenv()

stock_api_key = os.getenv('STOCK_API_KEY')

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")


'''
type:
    subscribe
    subscribe-news
    subscribe-pr (premium)

'''
def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')\

if __name__ == "__main__":
    finnhub_client = finnhub.Client(api_key=stock_api_key)
    print(finnhub_client.symbol_lookup('apple'))
    webstring = "wss://ws.finnhub.io?token=" + stock_api_key
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(webstring,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    #ws.on_open = on_open
    #ws.run_forever()