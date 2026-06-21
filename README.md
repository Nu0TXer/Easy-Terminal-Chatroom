# Easy-Terminal-Chatroom

基于 Python 原生 Socket 与多线程实现的轻量级局域网命令行聊天室。

## 📖 项目简介
本项目是一个运行在终端（Terminal）下的简易聊天室。通过 Python 标准库中的 `socket` 和 `threading` 模块，实现了基础的 C/S（客户端/服务端）架构。项目主要用于验证 TCP 协议的连接过程、多线程解决网络 I/O 阻塞的方法，以及局域网内的多点数据广播。


## ✨ 实现功能
- **TCP 通信**：基于 IPv4 与 TCP 协议进行网络数据传输。
- **多客户端并发连接**：服务端引入多线程（Threading）机制，为每个接入的客户端分配独立线程，支持多人同时在线群聊。
- **动态昵称绑定**：客户端接入时要求注册自定义昵称，服务端在广播时会自动拼接身份标识及系统上下线通知。
- **Base64加密**：为防止局域网内直接以明文形式被抓包嗅探，在应用层传输前对中英文字符串及 payload 进行了简单的 Base64 编码处理。

## 🛠️ 技术与环境
- **开发语言**：Python 3.x
- **依赖库**：Python 标准库（`socket`, `threading`, `base64`, `sys`）
- **测试环境**：Windows 11 、 Visual Studio Code

## 🚀 快速运行

### 1. 获取代码
```bash
git clone https://github.com/Nu0TXer/Easy-Terminal-Chatroom.git
cd Easy-Terminal-Chatroom
```

### 2. 启动服务端
首先开启服务端进行本地端口监听：
```bash
python server.py
```
*(默认监听 127.0.0.1:8888)*

### 3. 启动客户端
打开新的终端窗口（推荐使用 VS Code 的拆分终端功能开启多个窗口以测试群聊），运行：
```bash
python client.py
```
根据提示输入昵称后即可开始聊天。输入 `quit` 退出程序。

## 📸 运行截图
![Demo](Demo%20Screenshot.png)
---
**License:** MIT