import socket
import threading

# 使用字典存储客户端连接和对应的昵称，格式：{conn: '昵称'}
clients = {}

# 消息广播
# 如果指定了 sender_conn，可以选择不把消息发给发送者本人
def broadcast(message, sender_conn=None):
    for conn in list(clients.keys()):
        try:
            conn.send(message.encode('utf-8'))
        except:
            # 如果发送失败，说明该客户端已断开，清理掉
            remove_client(conn)

#退出聊天处理
def remove_client(conn):
    if conn in clients:
        nickname = clients[conn]
        del clients[conn]
        conn.close()
        print(f"[系统] {nickname} 退出了聊天室")
        broadcast(f"[系统通知] {nickname} 退出了聊天室")

def handle_client(conn, addr):
    try:
        # 客户端连接后的第一条消息规定为“昵称”
        nickname = conn.recv(1024).decode('utf-8')
        clients[conn] = nickname
        print(f"[系统] 客户端 {addr} 已连接，昵称注册为: {nickname}")
        
        # 广播欢迎消息
        broadcast(f"[系统通知] 欢迎 {nickname} 加入聊天室！")

        # 持续接收该客户端的消息
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            # 格式化消息并广播
            msg = f"[{nickname}]: {data}"
            print(msg) # 服务器控制台也打印一份日志
            broadcast(msg)
            
    except Exception as e:
        pass
    finally:
        remove_client(conn)

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