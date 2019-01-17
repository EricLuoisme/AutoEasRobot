from FakeRobot import Client

# 超时
# Client.send('{"type":1, "code":0, "data":"对本期完成的凭证进行提交处理"}')
#
# print(Client.receive())
# Client.send('{"type":0, "code":1, "data":{}}')
#
# print(Client.receive())
# # Client.send('{"type":0, "code":1, "data":{}}')
#
# print(Client.receive())
#
# print("已结束")



# # 执行查看
# Client.send('对本期完成的凭证进行提交处理')
# print(Client.receive())
# print(Client.receive())
# Client.send('好')
# print(Client.receive())

Client.send('{"type":1, "code":0, "data":"对本期完成的凭证进行提交处理"}')

print(Client.receive())
Client.send('{"type":0, "code":1, "data":{}}')

print(Client.receive())
Client.send('{"type":0, "code":1, "data":"好"}')

print(Client.receive())

print("已结束")

