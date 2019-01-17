

def detect_keywords_percentage(string, keywords):

    # 对输入的场景的keywords进行检测，获得百分比
    inside = 0

    key = keywords.get(0)
    main_key_check = True
    for j in key:
        if string.__contains__(j):
            main_key_check = False
            # 如果包含主要关键词中的一个，既为包含主要关键词
            break

    if main_key_check:
        # 如果没有包含主要关键词，直接返回为0
        return 0

    for i in range(1, len(keywords)):
        have = False
        this_keywords = keywords.get(i)
        for j in this_keywords:
            if string.__contains__(j):
                have = True
                break
        if have:
            inside += 1
            continue

    return (inside+1)/keywords.__len__()




# string = str("请制作一张体先凭证")
# string = str("随便测试体现凭证")
# keywords = {
#     0: {'制作', '生成'},
#     1: {'提现', '体现', '体先', '提鲜'},
#     2: {'凭证'}
# }
#
# print(detect_keywords_percentage(string, keywords))



