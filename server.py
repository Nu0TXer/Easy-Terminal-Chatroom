import socket
import threading


def handle_client(conn, addr):
    print(f"[连接] 客户端 {addr} 已连接")
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"[客户端] {data}")
            # 回复确认
            conn.send(f"服务器收到: {data}".encode('utf-8'))
        except:
            break
    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET表示IPv4，AF_INET6表示IPv6
    # SOCK_STREAM表示TCP，SOCK_DGRAM表示UDP

    server.bind(('127.0.0.1', 8888))
    server.listen(5)
    print("服务器启动，监听端口 8888 ...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    main()
