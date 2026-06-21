import socket
import threading
import sys
import base64

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            # 收到 Base64 字节流 -> 解码 -> 转为 utf-8 字符串
            decoded_msg = base64.b64decode(data).decode('utf-8')
            print(f"\n{decoded_msg}")
        except:
            print("\n[系统提示] 与服务器连接断开。")
            break

def main():
    # 建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 报错排查（需要先运行 server.py 再运行 client.py ）
    client.connect(('127.0.0.1', 8888))
    
    # 注册昵称，加密后发送给服务器
    nickname = input("请输入你在聊天室的昵称: ")
    encoded_nickname = base64.b64encode(nickname.encode('utf-8'))
    client.send(encoded_nickname)
    
    print(f" 欢迎来到多人聊天室，{nickname}！")
    print(" (输入文字按回车发送，输入 quit 退出)")

    # 开启接收线程
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # 主线程负责读取键盘输入，加密并发送
    while True:
        try:
            msg = input()
            if msg.lower() == 'quit':
                break
            # 发送前进行 Base64 加密处理
            encoded_msg = base64.b64encode(msg.encode('utf-8'))
            client.send(encoded_msg)
        except KeyboardInterrupt:
            break

    client.close()
    sys.exit(0)

if __name__ == '__main__':
    main()