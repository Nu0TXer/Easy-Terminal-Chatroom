import socket
import threading


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"[服务器] {data}")
        except:
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))
    print("已连接到服务器！输入文字发送，输入 quit 退出。")

    # 启动接收线程
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == 'quit':
            break
        client.send(msg.encode('utf-8'))


if __name__ == '__main__':
    main()
