"""
  Created by Amor on 2018-09-30
  图片处理的脚本
"""
import os
from PIL import Image

__author__ = '骆杨'


def compress_image(file_name):
    image = Image.open('../../media/image/ims/{}'.format(file_name))
    width = image.width
    height = image.height
    rate = 1.0  # 压缩率

    # 根据图像大小设置压缩率
    if width >= 2000 or height >= 2000:
        rate = 0.3
    elif width >= 1000 or height >= 1000:
        rate = 0.5
    elif width >= 500 or height >= 500:
        rate = 0.9

    width = int(width * rate)    # 新的宽
    height = int(height * rate)  # 新的高

    image.thumbnail((width, height), Image.ANTIALIAS)  # 生成缩略图
    cp_im = image.crop((0, 0, width, width/3))
    cp_im.save('../../media/image/ims_cp/{}'.format(file_name))


def get_file():
    pwd = os.walk('../../media/image/ims')
    for item in pwd:
        return item[2]


if __name__ == '__main__':
    file_list = get_file()
    for item in file_list:
        compress_image(item)
