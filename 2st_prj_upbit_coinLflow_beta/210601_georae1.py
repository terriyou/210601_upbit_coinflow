
btc_amount = []
btc_pyongdan = []
with open("210601_zdwlog.txt", encoding="utf8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        for i in range(cnt,9):
            line = fp.readline()
            #print(i)
            if i == 4:
                btc_amount.append(line.strip()[:-3])
            elif i == 5:
                btc_pyongdan.append(line.strip()[:-3].replace(",",""))
        line = fp.readline()
        cnt = 0

print(btc_amount)
print(btc_pyongdan)

for j in range(3):
    print(float(float(btc_amount[j])) * int(btc_pyongdan[j]))