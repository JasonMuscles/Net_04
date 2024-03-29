import socket


def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1.接收浏览器发送过来的请求,即：http请求
    # GET / HTTP/1.1
    # ..........
    request = new_socket.recv(1024)
    print(request)
    # 2.返回http格式数据给到浏览器
    # 2.1准备发送给浏览器的数据header（注意：\r\n => 表示换行，加入\r是为了兼容Windows）
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"  # 格式中海有一个空行
    # 2.2准备发送给浏览器的数据body
    # response += "<h>服务器发的数据...</h1>"
    f = open("/Users/jason/Study/Python高级-全部（html版）/01day/index.html", "rb")
    html_content = f.read()
    f.close()
    # 将response header发送给浏览器
    new_socket.send(response.encode("gbk"))

    # 将response body发送给浏览器
    new_socket.send(html_content)
    # 3.关闭套接字
    new_socket.close()


def main():
    """用于完成整体控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定
    tcp_server_socket.bind(("", 7788))
    # 3.监听套接字
    tcp_server_socket.listen(128)

    while True:

        # 4.等到新客户端链接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5.为客户端服务
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
