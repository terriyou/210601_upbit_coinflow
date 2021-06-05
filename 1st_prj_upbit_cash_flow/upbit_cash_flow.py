chool = []
ipgum = []

fail = []

tmp1 = []
tmp2 = []
tmp3 = []

with open("dwlog.txt", encoding="utf8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        try:
            if len(line) is not 6:        
                if "출금완료" in line:
                    #tmp1 = line.split()
                    #print('tmp1')
                    #print(tmp1)
                    chool.append(int(line.split()[1].replace(",","")))
                elif "입금완료" in line:
                    #tmp2 = line.split()
                    #print('tmp2')
                    #print(tmp2)
                    ipgum.append(int(line.split()[1].replace(",","")))
                else:
                    #tmp3 = line.split()
                    #print('tmp3')
                    #print(tmp3)
                    fail.append(int(line.split()[1].replace(",","")))
        except:
            pass
        line = fp.readline()

chool_t = sum(chool)
ipgum_t = sum(ipgum)

total = ipgum_t - chool_t

print("출금금액:" + str(chool))
print("입금금액:" + str(ipgum))
print("출입금실패:" + str(fail))
print("입금금액:" + str(total))
