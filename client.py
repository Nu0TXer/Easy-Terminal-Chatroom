import socket
import threading
import sys

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                break
            # 收到的消息
            print(f"\n{data}")
        except:
            print("\n[系统提示] 与服务器的连接已断开。")
            break

def main():
    # 建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 报错排查（需要先运行 server.py 再运行 client.py ）
    try:
        client.connect(('127.0.0.1', 8888))
    except Exception as e:
        print("连接服务器失败，请确认服务器已启动！")
        return

    # 注册昵称
    nickname = input("请输入你在聊天室的昵称: ")
    client.send(nickname.encode('utf-8'))
    
    print(f" 欢迎来到多人聊天室，{nickname}！")
    print(" (输入文字按回车发送，输入 quit 退出)")
    

    # 启动接收消息的子线程
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # 主线程：负责发送消息
    while True:
        try:
            msg = input()
            if msg.lower() == 'quit':
                break
            client.send(msg.encode('utf-8'))
        except KeyboardInterrupt:
            break

    client.close()
    sys.exit(0)

if __name__ == '__main__':
    main()