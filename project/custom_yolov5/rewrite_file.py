import os
path = 'C:/Users/LeeYuho/Desktop/Image_Crawling/lables/Koifish'
file_list = os.listdir(path)

for file in file_list:
    cnt = 1
    s = ''
    with open(path + '/' + file,'r') as f:
        lines = f.readlines()
        for line in lines:
            s = s + '8' + line[1:]

    with open(path + '/' + file,'w') as f:
        f.write(s)
