
from aip import AipSpeech
from playsound import playsound
from NAudioProcess.data import Recognition_Setting, File_Setting

#####################################################
# """ 你的 APPID AK SK """
APP_ID = Recognition_Setting.APP_ID
API_KEY = Recognition_Setting.API_KEY
SECRET_KEY = Recognition_Setting.SECRET_KEY


#################################################################
# forRecognition
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 读取paudio录制好的音频文件, 调用百度语音API, 设置api参数, 完成语音识别
#    client:AipSpeech对象
#    afile:音频文件
#    afmt:音频文件格式(wav)
def aip_get_asrresult(client, afile, afmt):
    # 选项参数:
    # cuid    String  用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
    # dev_pid String  语言类型(见下表), 默认1537(普通话 输入法模型)
    # 识别结果已经被SDK由JSON字符串转为dict
    result = client.asr(get_file_content(afile), afmt, 16000)
    # print('original result')
    # print(result)
    # 如果err_msg字段为"success."表示识别成功, 直接从result字段中提取识别结果, 否则表示识别失败
    if result["err_msg"] == "success.":
        # print(result["result"])
        return result["result"]
    else:
        # print(result["err_msg"])
        return ""


def doing_recog(outfile, check):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    if check:
        result = aip_get_asrresult(client, outfile + '_denoise.wav', 'wav')
    else:
        result = aip_get_asrresult(client, outfile + '_cut.wav', 'wav')
    # print('one attribute result')

    if result is '':
        print("识别结果为: 空" + "\n")
        return result
    else:
        print('识别结果为: ' + result[0] + "\n")
        return result[0]


def doing_voice_comb(sentence, FILE_NUMBER):

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(sentence)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(File_Setting.outPath_Combin + 'answer' + str(FILE_NUMBER) + '.mp3', 'wb') as f:
            f.write(result)
    play_sound(FILE_NUMBER)


def play_sound(FILE_NUMBER):
    playsound(File_Setting.outPath_Combin + 'answer' + str(FILE_NUMBER) + '.mp3')
