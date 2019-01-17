import Message as _this


class Command:
    def __int__(self):
        self.command = 0
        self.data = 0


class CommandMessage(_this.Message):
    def __init__(self, c, d):
        super().__init__(2, c, d)

    def to_json(self):
        cs = []
        for c in self.data:
            cs.append({
                'command': c.command,
                'data': c.data
            })
        j = super().to_json()
        j['data'] = cs
        return j


def set_commands(commands):
    cs = []
    for command in commands:
        c = Command()
        c.command = command['command']
        c.data = command['data']
        cs.append(c)
    return _this.set_message(CommandMessage(0, cs))

