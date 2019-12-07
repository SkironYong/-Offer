list = []
file = open(r'C:\Users\HP\Desktop\output.txt','w+')
with open(r'C:\Users\HP\Desktop\rpc_MasterProvisional2_2.out', 'r') as f:
   for line in f:
       ls = line.replace(',','\n').replace(' ','')
       list.append(ls)
file.write(''.join(list))