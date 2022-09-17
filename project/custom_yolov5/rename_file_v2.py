# Yolo Labeling txt파일 이름 바꾸기
import os

def format_str_num(n):
    if n < 10:  return '00' + str(n)
    elif n < 100:   return '0' + str(n)
    else:   return str(n)

target = 'Dwarf_Gourami'    # 물고기명(폴더명)
n = len(target)             # 물고기 문자열 길이
train_path = "C:/Users/LeeYuho/Desktop/Image_Crawling/lables"
train_list = os.listdir(train_path)
print(train_list)

for folder in train_list:
    cnt = 1
    file_path = train_path + '/' + folder
    file_list = os.listdir(file_path)
    if folder == target:
        for file in file_list:
            if file != 'classes.txt':
                prev_path = file_path + '/' + file
                new_name = folder + file[n:n+3] + '.txt'
                curr_path = file_path + '/' + new_name
                os.rename(prev_path, curr_path)
                cnt += 1
        print(folder + ' 변환완료')