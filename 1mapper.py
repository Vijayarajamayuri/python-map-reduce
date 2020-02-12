input = open("purchases.txt", "r")
output = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time,store, item, cost, purchaseType = datalist
    output.write(purchaseType + "\t" + item + "\n")

input.close()
output.close()