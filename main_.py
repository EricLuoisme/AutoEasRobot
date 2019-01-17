import AutoWeb

import time


def get_common(c):
    return {
        '登录': do_login,
        '提现凭证新增': do_add_certificate,
        '机器人执行凭证提交': do_certificate_submit,
        '机器人执行凭证提交异常查看': do_certificate_submit_fail_log,
        '机器人执行凭证提交信息关闭': do_certificate_submit_close_log,
        '机器人凭证提交设置': do_certificate_setting,
        # '机器人执行凭证审核': do_certificate_check,
        # '机器人执行凭证审核成功查看': do_certificate_check_success_log,
        '结束': do_end
    }.get(c, do_default)


def do_default():
    print('请重新输入有效指令\n')


# 登录
def do_login():
    AutoWeb.login()


# 新增凭证
def do_add_certificate():
    AutoWeb.add_certification()


# 机器人执行凭证提交
def do_certificate_submit():
    AutoWeb.submit_certification()


def do_certificate_submit_fail_log():
    AutoWeb.show_submit_certification_fail_log()


def do_certificate_submit_close_log():
    AutoWeb.close_submit_certification_fail_log()


def do_certificate_setting():
    AutoWeb.show_submit_certification_setting()


# 结束
def do_end():
    exit(0)


if __name__ == '__main__':
    print('Application begin to listen input\n')
    AutoWeb.login()
    while True:
        command = input('Enter a Command : ')
        action = get_common(command)
        time.sleep(2)
        action()
