# 이미지 파일 이름 바꾸기
import os

# 서식변환
def format_str_num(n):
    if n < 10:  return '00' + str(n)
    elif n < 100:   return '0' + str(n)
    else:   return str(n)

target = 'Cardinal_Tetra'   # 폴더명
train_path = "C:/Users/LeeYuho/yolov5/data/images/train/fish"
train_list = os.listdir(train_path)
print(train_list)

for folder in train_list:
    cnt = 1
    file_path = train_path + '/' + folder
    file_list = os.listdir(file_path)
    if 1:
        for file in file_list:
            prev_path = file_path + '/' + file
            if file.split('.')[1] in ['jpg', 'jpeg', 'png']:
                new_name = folder + format_str_num(cnt) + '.' + file.split('.')[1]
            else:
                new_name = folder + format_str_num(cnt) + '.png'
            curr_path = file_path + '/' + new_name
            os.rename(prev_path, curr_path)
            cnt += 1
        print(folder + ' 변환완료')