# 확장자가 .txt인 파일만 옮기기
import shutil
import os

path = 'C:/Users/LeeYuho/Documents/카카오톡 받은 파일/Dwarf_Gourami'
file_list = os.listdir(path)
cnt = 1
for file in file_list:
    l = len(file.split('.')) - 1
    if file.split('.')[l] == 'txt':
        src = path + '/' + file
        dir = 'C:/Users/LeeYuho/Desktop/Image_Crawling/lables/Dwarf_Gourami/' + file
        shutil.move(src,dir)