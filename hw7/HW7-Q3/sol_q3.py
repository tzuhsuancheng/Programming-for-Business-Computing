"""
註解掉的是助教我自己的寫法
"""

# import re

file_path = input()

# processing query, split()也會對 tab 做處理
query = ' '.join(input().lower().split())
# query = re.sub('\s+', ' ', input().lower()).strip()

count = 0

# txt 第一與最後一個element都是空字串
txt = [""]
with open(file_path, encoding='utf-8') as file:
    for line in file:
        txt.append(line.strip())
txt.append("")

# 如果搜尋字串有在該行內，則依照題目輸出，文本內的句子也要忽略多個空白
for i in range(1, len(txt) - 1):
    if query in ' '.join(txt[i].lower().split()):
        count += 1
        print("----Match", count)
        print("    @" + str(i - 1) + ": " + txt[i - 1])
        print("    @" + str(i) + ": " + txt[i])
        print("    @" + str(i + 1) + ": " + txt[i + 1])
        # print("    @{}: {}".format(i - 1, txt[i - 1]))
        # print("    @{}: {}".format(i, txt[i]))
        # print("    @{}: {}".format(i + 1, txt[i + 1]))
