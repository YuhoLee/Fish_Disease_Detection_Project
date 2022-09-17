# 이미지 파일에는 있고 Labeling txt파일에는 없는 번호 출력
# 파일 형식은 이미지 파일의 경우 물고기명001.png, txt파일의 경우 물고기명001.txt

import os

def format_str_num(n):
    if n < 10:  return '00' + str(n)
    elif n < 100:   return '0' + str(n)
    else:   return str(n)

target = 'Dwarf_Gourami'  # 폴더명
n = len(target)
train_path = "C:/Users/LeeYuho/Desktop/Image_Crawling/lables"
train_list = os.listdir(train_path)
print(train_list)

for folder in train_list:
    file_path = train_path + '/' + folder
    file_list = os.listdir(file_path)
    prev = 0
    if folder == target:
        for file in file_list:
            if file != 'classes.txt':
                curr = int(file[n:n+3])
                diff = curr - prev
                for i in range(diff-1,0,-1):
                    print(format_str_num(curr - i))
                prev = curr
