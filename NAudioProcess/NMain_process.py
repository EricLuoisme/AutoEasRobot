from NAudioProcess import NScript_process


def identify_execute(string, FILE_NUMBER, check=False):

    if check is False:
        arousing_status = NScript_process.arouse_recognize(string)
        # if arousing_status is not None:
        return arousing_status
    else:
        script_status = NScript_process.script_recognize(string, FILE_NUMBER)
        # if script_status is not None:
        return script_status

    return None
