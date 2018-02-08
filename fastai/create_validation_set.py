from random import shuffle
import os
import sys

path = sys.argv[1]
train_path = f'{path}train/'
valid_path = f'{path}valid/'

def split_valid_set(dir,new_dir,per=0.2):
    files = os.listdir(dir)
    shuffle(files)
    n = len(files)
    num = int(per*n)
    for i in range(num):
        file = files[i]
        os.rename(dir+file, new_dir+file)


for dir in os.listdir(train_path):
    # Create a new directory in valid/
    os.makedirs(f'{valid_path}{dir}/', exist_ok=True)
    split_valid_set(f'{train_path}{dir}/', f'{valid_path}{dir}/')