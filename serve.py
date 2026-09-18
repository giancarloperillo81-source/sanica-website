from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser
root = Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(root),**kwargs)
server=ThreadingHTTPServer(('127.0.0.1',8000),Handler)
print('Sa.Ni.Ca. locale: http://127.0.0.1:8000/')
server.serve_forever()
