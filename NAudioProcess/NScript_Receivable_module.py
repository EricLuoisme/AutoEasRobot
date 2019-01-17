from NAudioProcess.data import NSin_Receivable_Module
from NAudioProcess import NCheck_Keywords, Recognition_process


def do_script(result, num, FILE_NUMBER):

    sce = "scenario_" + str(num)
    scenario = NSin_Receivable_Module.get_scenario(sce)

    percentage = NCheck_Keywords.detect_keywords_percentage(result, scenario)
    if percentage > 0.8:
        # 在某个场景下，包含其关键词超过80%既认定为该场景
        print(NSin_Receivable_Module.get_answer(sce))
        # 语音融合
        Recognition_process.doing_voice_comb(NSin_Receivable_Module.get_answer(sce), FILE_NUMBER)
        return False


# def do_sub_script(num):
#     # 只有在用户回答查看原因的时候才会执行子场景
#     sce = "scenario_" + str(num) + "_sub"
#     print(Sin_Receivable_Module.get_answer(sce))
#     return False
