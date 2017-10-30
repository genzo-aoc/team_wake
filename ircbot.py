# -*- coding: utf-8 -*-
import sys
import re
import subprocess
import pprint as pp
from functools import reduce

if __name__ == "__main__":
    args = sys.argv
    # text = "tg チーム1： 【6411】 konitan12(2005) AI(876) mjk(1780) genzo(1750)チーム2: 【6549】 Aeon_esuda(1682) sugi-na(2003) cane(1457) sarisari(1407)"
    text = args[1]
    # print(text)

    if not (text[0] == "t" and text[1] == "g"):
        # print("err")
        sys.exit()
    #名前とレートを配列に [konitan12(2005),AI(876),...]
    tmp = [x for x in text.split(" ") if '(' in x]

    # pp.pprint(tmp)
    
    #正規表現
    members = [re.search(r'^(.*)\(([0-9]+)\)', x) for x in tmp]
    
    #名前とレートの配列 [{"name":"konitan12","rate":2005},{"name":"AI",rate:876},...]
    members = [{"name": x.group(1), "rate": int(x.group(2))} for x in members]
    #select すべてのチームの組み合わせ
    select = []
    for i in range(1):
        for i2 in range(i + 1, 6):
            for i3 in range(i2 + 1, 7):
                for i4 in range(i3 + 1, 8):
                    select.append([i, i2, i3, i4])
                    
    #各チーム分けの合計値
    sum_rates = [(sum([members[i]['rate'] for i in s]), s) for s in select]
    #参加メンバーのレートの合計
    sum = sum([x['rate'] for x in members])
    # print("sum=" + str(sum))
    #レート差最小の分け
    result = min(sum_rates, key=lambda x: abs(x[0] - sum / 2))
    
    #表示
    team1 = ""
    team2 = ""
    for i in range(8):
        if i in result[1]:
            team1 += members[i]["name"] + "(" + str(members[i]["rate"]) + ") "
        else:
            team2 += members[i]["name"] + "(" + str(members[i]["rate"]) + ") "
    rtn_txt = "【" + str(result[0]) + "】 チーム1:" + team1 + "【" + str(sum - result[0]) + "】  チーム2:" + team2
    print(rtn_txt)
