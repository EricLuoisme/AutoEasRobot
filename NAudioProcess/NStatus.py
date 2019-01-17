class Status:
    def __init__(self, the_type, the_num=None, the_state=None):
        # type, state, num 分别对应 主类型，是否为子场景，场景编号
        self.type = the_type
        self.num = the_num
        self.state = the_state

        # type: 'General_Ledger', 'Receivable_Module', 'Arousing', 'Mis_operation'
