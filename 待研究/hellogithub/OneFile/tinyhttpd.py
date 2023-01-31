import http.server
import socketserver
# 设置监听的端口
PORT = 8000
# 设置处理的类
Handler = http.server.SimpleHTTPRequestHandler
# 开启服务
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
# 开启服务
httpd.serve_forever()
