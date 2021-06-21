#btc_x = [buy,sell]

jung_san = [[],[],[],[]]

#d_cash = [minus,plus]
d_cash = [[],[]]

buy_sell_flag = 5

with open("jhj_btc2.txt", encoding="utf8") as fp:
    line = True
    cnt = 0
    while line:
        for i in range(cnt,10):
            line = fp.readline()
            #print(i)
            #print(line.strip())
            if i == 3:
                if "매수" in line:
                    buy_sell_flag = 0
                elif "매도" in line:
                    buy_sell_flag = 1
                elif "입금" in line:
                    buy_sell_flag = 2
                elif "출금" in line:
                    buy_sell_flag = 3
                else:
                    buy_sell_flag = 4
            elif i == 6:
                if buy_sell_flag == 2:
                    jung_san[2].append(line.strip()[:-3].replace(",",""))
                    buy_sell_flag = 4
                elif buy_sell_flag == 3:
                    jung_san[3].append(line.strip()[:-3].replace(",",""))
                    buy_sell_flag = 4

            elif i == 8:
                if buy_sell_flag == 0:
                    jung_san[0].append(line.strip()[:-3].replace(",",""))
                    buy_sell_flag = 4
                elif buy_sell_flag == 1:
                    jung_san[1].append(line.strip()[:-3].replace(",",""))            
                    buy_sell_flag = 4
                
        line = fp.readline()
        print("end_readline")
        print(line.strip())
        cnt = 1

for j in range(len(jung_san[0])):
    d_cash[0].append(int(jung_san[0][j]))

for j in range(len(jung_san[1])):
    d_cash[1].append(int(jung_san[1][j]))

print(sum(d_cash[1])-sum(d_cash[0]))

print(197640-159630)
