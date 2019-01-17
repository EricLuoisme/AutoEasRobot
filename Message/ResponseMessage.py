import Message as _this


class ResponseMessage(_this.Message):
    def __init__(self, c, d):
        super().__init__(0, c, d)

    def to_json(self):
        return super().to_json()


def __message_to_json__(message):
    return message.to_json()


def success():
    return _this.set_message(ResponseMessage(1, {}))


def fail():
    return _this.set_message(ResponseMessage(0, {}))


def is_success(jsonText):
    message = _this.get_message(jsonText)
    if message.code == 1:
        return True
    else:
        return False
