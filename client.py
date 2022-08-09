import socket,json

def B():
    # 创建socket
    B = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    Key = "HOWAREYOU"
    B.sendto(Key.encode("GBK"),('47.100.234.158',2333))
    recv_data = B.recvfrom(1024)
    print(recv_data[0])
    datas = json.loads(recv_data[0].decode())
    while True:
        B.sendto("".encode(),(datas['ip'],int(datas['port'])))
        recv_datas,addrs = B.recvfrom(1024)
        print(recv_datas.decode())
        if len(recv_datas.decode()) > 0:
            B.sendto('Hello World'.encode(),(datas['ip'],int(datas['port'])))

def A():
    # 创建socket
    A = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    Key = "^HOWAREYOU"
    A.sendto(Key.encode("GBK"),('47.100.234.158',2333))
    recv_data = A.recvfrom(1024)
    print(recv_data[0])
    datas = json.loads(recv_data[0].decode())
    while True:
        A.sendto("".encode(),(datas['ip'],int(datas['port'])))
        recv_datas,addrs = A.recvfrom(1024)
        print(recv_datas.decode())
        text = input("请输入内容: ")
        if len(text) > 0:
            A.sendto(text.encode(),(datas['ip'],int(datas['port'])))
if __name__ == "__main__":
    print(" - - - - A客户 : A - B客户 : B - - - -")
    bools = input("输入您的客户字母: ")
    if bools == "A": A()
    if bools == "B": B()