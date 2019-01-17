
from NAudioProcess import Server
import AutoWeb
import Message
from Message import ResponseMessage
from Message import CommandMessage


def running():
    """
    总账第三个场景，负责演示对本期提交的凭证进行提交处理，包含查询是否出现
    以及查询错误的子场景

    :return: 不返回任何值
    """
    #Server.send('财务凭证提交处理的机器人手部与口头操作')
    Server.send(CommandMessage.set_commands([
        {'command': 0, 'data': '好的，接下来将对本会计期间内制作的全部凭证进行提交处理，请看屏幕。'},
        {'command': 1, 'data': 2},
        {'command': 0, 'data': '我们将通过“总账凭证提交机器人” 来实现本会计期间的凭证提交处理，同时校验有错的凭证不对其做提交处理。'}
    ]))
    # 等待机器人动作响应
    ResponseMessage.is_success(Server.receive())
    result = AutoWeb.submit_certification()
    if result is not None:
        if result[0] == 1:
            print('全部凭证提交结束')
            Server.send(CommandMessage.set_commands([
                {'command': 0, 'data': result[1]},
                {'command': 1, 'data': 1}
            ]))
            ResponseMessage.is_success(Server.receive())
        else:
            print('有误，是否查看错误原因')
            Server.send(CommandMessage.set_commands([
                {'command': 0, 'data': result[1]}
            ]))

            receive = Message.get_speech(Server.receive(True))

            if receive == '' or receive.__contains__('我不'):
                print('提前结束场景')
                Server.send('场景结束')
                AutoWeb.close_submit_certification_fail_log()
            elif receive.__contains__('好'):
                print('执行查看操作')
                # Server.send('执行查看操作，随后场景结束')
                Server.send(CommandMessage.set_commands([
                    {'command': 0, 'data': '请看凭证提交失败的原因'},
                    {'command': 1, 'data': 2}
                ]))
                ResponseMessage.is_success(Server.receive())
                AutoWeb.show_submit_certification_fail_log()
