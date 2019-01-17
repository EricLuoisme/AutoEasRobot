menu = {
    '财务会计': {
        '总账': [
            '凭证新增'
        ]
    },
    '财务机器人': {
        '核算机器人': [
            '方案维护',
            '执行日志'
        ]
    }
}


def get_path_by_operation(operation):
    """
    返回对应操作的三级目录
    :param operation: 操作
    :return: 菜单目录
    """
    for (key, value) in menu.items():
        for (key1, value2) in value.items():
            if operation in value2:
                return key, key1, operation
