import socket
import threading
import base64

# 字典存储用户昵称 {客户端socket: '自定义昵称'}
clients = {}

# 消息广播
def broadcast(message):
    # 将明文消息 Base64 编码
    # 字符串转 utf-8 字节流 -> Base64 编码字节流
    encoded_msg = base64.b64encode(message.encode('utf-8'))
    for conn in list(clients.keys()):
        try:
            conn.send(encoded_msg)
        except:
            if conn in clients:
                del clients[conn]
                conn.close()

def handle_client(conn, addr):
    try:
        # 接收加密的昵称并解码
        data = conn.recv(1024)
        nickname = base64.b64decode(data).decode('utf-8')
        clients[conn] = nickname
        print(f"[系统] 客户端 {addr} 已连接，昵称: {nickname}")
        broadcast(f"[系统通知] 欢迎 {nickname} 加入聊天室！")

        while True:
            # 接收加密的聊天内容并解码
            data = conn.recv(1024)
            if not data:
                break
            msg = base64.b64decode(data).decode('utf-8')
            full_msg = f"[{nickname}]: {msg}"
            print(full_msg)  # 服务器端后台打印明文日志
            broadcast(full_msg)  # 重新加密并广播
    except:
        pass
    finally:
        if conn in clients:
            nickname = clients[conn]
            del clients[conn]
            conn.close()
            broadcast(f"[系统通知] {nickname} 退出了聊天室")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET表示IPv4，AF_INET6表示IPv6
    # SOCK_STREAM表示TCP，SOCK_DGRAM表示UDP
    server.bind(('127.0.0.1', 8888))
    server.listen(5)

    print(" 多人网络聊天室服务器已启动，监听端口 8888 ...")
    print(" 等待客户端连接中...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == '__main__':
    main()