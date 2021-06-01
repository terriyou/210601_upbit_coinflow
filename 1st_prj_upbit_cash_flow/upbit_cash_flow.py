chool = []
ipgum = []

fail = []

with open("history.txt", encoding="utf8") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        try:
            if len(line) is not 6:        
                if "출금완료" in line:
                    chool.append(int(line.split()[1].replace(",","")))
                elif "입금완료" in line:
                    ipgum.append(int(line.split()[1].replace(",","")))
                else:
                    fail.append(int(line.split()[1].replace(",","")))
        except:
            pass
        line = fp.readline()


chool_t = sum(chool)
ipgum_t = sum(ipgum)

total = ipgum_t - chool_t

#print("출금금액:" + str(chool))
#print("입금금액:" + str(ipgum))
#print("출입금실패:" + str(fail))
print("입금금액:" + str(total))
