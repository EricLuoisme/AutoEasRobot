# 总账场景
# 第0个关键词是必须要包含的，否则认为是另外场景

from NAudioProcess.script_interaction import GL_3

def get_scenario(sce):
    return {
        #####################################################################
        # 2. 智能记账-提现凭证新增
        # Q: 小智，请制作一张提现凭证。
        # A: 好的，接下来会根据您的要求制作一张提现的凭证，...
        # ...业务情况是：2018年1月12日，从汇丰银行的账户提取1500元人民币作为库存备用金。
        # A: 已经为您完成了提现凭证的制作，请查看凭证。
        'scenario_2': {
            0: {'提现', '体现', '体先', '提鲜'},
            1: {'制作'},
            2: {'一张'},
            3: {'凭证'}
        },
        #####################################################################
        # 3. 执行提现凭证提交
        # Q: 小智，请对本期完成的凭证进行提交处理
        # A: 好的，接下来将对本会计期间内制作的全部凭证进行提交处理。
        'scenario_3': {
            0: {'提交处理'},
            1: {'本期'},
            2: {'完成'},
            3: {'凭证'}
        },
        # A: 你好，本会计期间内填写正确凭证已经全部提交成功，填写错误的凭证提交失败，需要为您打开查看了解具体失败的原因吗？
        # Q1. 好的，请打开失败记录查看原因
        # Q2. 小智，不用了。
        'scenario_3_sub': {
        },
        #####################################################################
        # 4. 凭证提交设置
        # Q: 小智，我要看看总账凭证提交的机器人是如何设置的。
        # A: 好的，接下来我们看看金蝶软件（中国）有限公司的总账凭证提交是如何设置的。
        # A: 本页面的设置，可以保证金蝶软件（中国）有限公司每天制作好的总账凭证提交一次。
        'scenario_4': {
            0: {'设置'},
            1: {'总账', '肿胀'},
            2: {'凭证'},
            3: {'提交'},
            4: {'机器人'},
            5: {'如何'},
        },
        #####################################################################
        # 5. 执行凭证审核
        # Q: 小智，请对本期提交的凭证进行审核处理
        # A: 好的，接下来将对本会计期间内提交的全部凭证进行审核处理。
        'scenario_5': {
            0: {'审核'},
            1: {'本期'},
            2: {'提交'},
            3: {'凭证'}
        },
        # A: 你好，本会计期间内提交的凭证已经全部审核成功，需要为您打开查看下已经审核成功的凭证信息吗？
        # Q1: 好的，请打开成功审核的记录
        # Q2: 小智，不用了
        'scenario_5_sub': {
        },
        #####################################################################
        # 6. 凭证审核设置
        # Q: 小智，我要看看总账凭证审核的机器人是如何设置的。
        # A: 好的，接下来我们看看金蝶软件（中国）有限公司的总账凭证审核是如何设置的。
        # A: 本页面的设置，可以保证金蝶软件（中国）有限公司每天对制作好的总账凭证进行审核。
        'scenario_6': {
            0: {'审核'},
            1: {'总账'},
            2: {'凭证'},
            3: {'设置'},
            4: {'机器人'},
            5: {'如何'},
        }
    }[sce]


def get_answer(sce):
    return {
        'scenario_2': '制作提现凭证',
        'scenario_3': GL_3.running(),   #'对本期完成的凭证进行提交处理， 随后进入子场景',
        'scenario_3_sub': '打开失败原因',
        'scenario_4': '查看金蝶软件（中国）有限公司的总账凭证提交是如何设置的',
        'scenario_5': '对本期提交的凭证进行审核处理， 随后进入子场景',
        'scenario_5_sub': '打开成功审核记录',
        'scenario_6': '查看金蝶软件（中国）有限公司的总账凭证审核是如何设置的'
    }[sce]
