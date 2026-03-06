def translate(text):
    # --- 新增：处理短语逻辑 ---
    if " " in text:
        # 将短语按空格切分，每个单词调用一次自己，最后用空格连起来
        return " ".join([translate(word) for word in text.split()])
    # -----------------------

    vowels = "aeiou"
    
    # 规则 1：特殊开头直接加 ay
    if text[0] in vowels or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"

    # 寻找分水岭位置 i
    i = 0
    while i < len(text):
        # 规则 3：处理 qu
        if text[i:i+2] == "qu":
            i += 2
            break
        # 规则 4：处理 y
        if i > 0 and text[i] == "y":
            break
        # 遇到元音
        if text[i] in vowels:
            break
        i += 1
    
    return text[i:] + text[:i] + "ay"