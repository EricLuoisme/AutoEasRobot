import os
from NAudioProcess.data import File_Setting
from NAudioProcess import NMain_process, Server
import AutoWeb
import Message


# 用于对存储的语音合成的mp3文件进行命名，由于在win10中覆盖音频文件权限不足
FILE_NUMBER = 0


def determine_scenario(string):
    """
    函数接受 string 字符串并进行场景判断，最后调用 NAudioProcess.data 中的
    :param string: robot端传输的字符串
    :return: None
    """
    global FILE_NUMBER
    return_state = NMain_process.identify_execute(string, FILE_NUMBER, True)
    if return_state is not None:
        FILE_NUMBER = FILE_NUMBER + 1

##########################################################################################


# real executing point #
if os.path.exists(File_Setting.outPath_Combin) is False:    # 判断是否存在路径，没有则创建
    os.makedirs(File_Setting.outPath_Combin)

AutoWeb.login()

# string = str("对本期完成的凭证进行提交处理")
while True:
    string = Message.get_speech(Server.receive())
    determine_scenario(string)

