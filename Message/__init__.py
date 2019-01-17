import json


class Message:
    def __init__(self, t, c, d):
        self.type = t
        self.code = c
        self.data = d

    def to_json(self):
        return {
            'type': self.type,
            'code': self.code,
            'data': self.data
        }


def get_message(jsonText):
    """
    获取消息对象
    :param jsonText:
    :return:
    """
    try:
        obj = json.loads(jsonText)
    except:
        return ''
    return Message(obj['type'], obj['code'], obj['data'])


def __message_to_json__(message):
    return message.to_json()


def set_message(message):
    """
    构建消息对象
    :param message:
    :return:
    """
    return json.dumps(message, default=__message_to_json__, ensure_ascii=False)


def set_message_o(t, c, d):
    """
    构建消息对象
    :param t:类型
    :param c:状态码
    :param d:数据（字典类型）
    :return:
    """
    return set_message(Message(t, c, d))


def get_speech(jsonText):
    message = get_message(jsonText)
    if type(message) is str:
        return message
    if message.type == 1:
        return message.data
    else:
        return ''

