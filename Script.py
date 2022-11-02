f = open('file.txt')
a = f.readlines()
j=1
for i in range(2, 135):
    if (a[i][1] == '\t' or a[i][1] == ' '):
        continue
    if j % 2 ==1:
        a[i] = a[i].replace('\t',' '+str((j+1)//2)+'\t', 2)
    else:
        a[i] = a[i].replace('\t', ' ' + str((j) // 2) + '+\t', 2)
    j+=1

    if j == 15: j = 1

f = open('fileNEW.txt', 'w')
for i in range(len(a)):
    f.writelines(a[i])
    print(a[i])