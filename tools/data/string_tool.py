

# 字典转字符串
def dic_to_str(dic):
    s = ''
    for key in dic:
        s+="{0}: {1}\n".format(key,dic[key])
    return s
