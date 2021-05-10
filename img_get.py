from urllib import request
import os 
import uuid

path_ = os.path.dirname(str(os.path.realpath(__file__)))

path = f'{path_}/img3_/'
file_list = os.listdir(path)

print(len(file_list))
