import socket

# New TCP between the two connect
ftcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "0.0.0.0"  
port = 2333
# bind ip and port
ftcp.bind((ip,port))
lists = {}

while True:
    data,conn = ftcp.recvfrom(1024)
    print("连接IP ： " ,conn)
    datac = data[0]
    datac = data.decode()
    # 验证开头是否是^，如果是则为验证码
    # print(datac[0])
    if datac[0] == "^" and len(datac) > 4:
        # 添加字典用于验证
        lists.update({
            datac:{
                "ip":conn[0],
                "port":conn[1]
            }
        })
        # print(lists)
    elif datac[0] != "^" and len(datac) > 4:
        # 获取data[key]
        get_key = lists["^"+datac]

        print("进行NAT的IP: {}:{}  <=  {}:{}  ".format(get_key['ip'],str(get_key['port']),conn[0],conn[1]))
        # 向 建立方 发送 连接方 数据
        ftcp.sendto(str('{"ip":\"'+ conn[0] +'\","port":\"'+ str(conn[1]) +'\"}').encode(),(get_key['ip'],int(get_key['port'])))
        # 向 连接方 发送 建立方 数据
        ftcp.sendto(str('{"ip":\"'+ get_key['ip'] +'\","port":\"'+ str(get_key['port']) +'\"}').encode(),(conn[0],conn[1]))