# -*- coding: utf-8 -*-

from wxpy import *
import math
from PIL import Image
import os


# Create folder for avatars storing.

def create_filepath():
    avatar_dir = os.getcwd() + "\\wechat\\"
    if not os.path.exists(avatar_dir):
        os.mkdir(avatar_dir)
    return avatar_dir


# Save the avatars.

def save_avatar(avatar_dir):
    # Initial bot and login via swapping the QR code
    bot = Bot()
    friends = bot.friends(update=True)
    num = 0
    for friend in friends:
        friend.get_avatar(avatar_dir + '\\' + str(num) + ".jpg")
        print('Nickname:%s' % friend.nick_name)
        num = num + 1


# Avatars jointing.

def joint_avatar(path):
    # Get the number of avatars in the folder.
    length = len(os.listdir(path))
    # Set
    image_size = 2560
    # Set the size of each avatar.
    each_size = math.ceil(2560 / math.floor(math.sqrt(length)))
    # Count the avatars' number
    x_lines = math.ceil(math.sqrt(length))
    y_lines = math.ceil(math.sqrt(length))
    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            # Add exception handing.
            try:
                with Image.open(path + pic_name) as img:
                    img = img.resize((each_size, each_size))
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print("Failed to load avatars.")
        img = image.save(os.getcwd() + "/wechat.png")
        print('Avatars jointing done!')


if __name__ == '__main__':
    avatar_dir = create_filepath()
    save_avatar(avatar_dir)
    joint_avatar(avatar_dir)
