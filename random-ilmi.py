#continue and break
data_suhu = [35,33,33,34,30,29,27,26,27,26,24,27]
for i in data_suhu:
    if i < 25 :
        continue
    print("data_suhu ", i,"\u00B0")
batas_angka = 5 
jumlah = 100
i = 1
print("10: ")
while i <= batas_angka :
    break 


    print(i)
    jumlah=jumlah+i
    i=100+1

print("jumlah=", jumlah)
