from PIL import Image, ImageDraw, ImageFont
from random import randint, choice
import datetime
from time import sleep
from screeninfo import get_monitors

def delete_others(name):
    from os import listdir, remove
    for f in listdir('images/'):
        if f != name:
            remove('images/' + f)

def get_size():
    m = get_monitors()[0]
    return m.width, m.height

def get_color():
    if 1:
        return randint(0, 255), randint(0, 255), randint(0, 255)
    colors = [
        (255, 254, 197),
        (246, 224, 142),
        (255, 166, 171), 
        (188, 168, 237), 
        (247, 201, 247), 
        (255, 231, 253),
        (95,  230, 208), 
        (216, 243, 198), 
        (244, 244, 224), 
        (205, 215, 239), 
        (238, 219, 242), 
        (195, 216, 136), 
        (251, 161, 197),
        (253, 208, 199), 
        (120, 196, 235),
        (174, 222, 240), 
        (236, 183, 206)
    ]
    alphas = [
        0, 
        1,
        .5,
        .1,
        .7
    ]
    color = choice(colors)
    a = randint(0, 10) / 10
    color = tuple(map(lambda x: int(x * a), color))
    return color


def test_sybs():
    s = ''
    for i in range(55203):
        s += str(i) + ' ' + chr(i) + '\n'
    with open('test.txt', 'w') as t:
        t.write(s)


def get_symbol(chars='all'):
    
    alphabets = {
        'all': (0, 55203),
        'korean': (44032, 55203)
    }
    try:
        a = alphabets[chars]
    except KeyError:
        a = alphabets['all']
    return chr(randint(*a))

def preload():
    global w, h, FONT_SIZE, font
    w, h = get_size()
    FONT_SIZE = 25
    font = ImageFont.truetype("font.ttf", FONT_SIZE, encoding="unic")


def main():
    global w, h, FONT_SIZE, font
    preload()
    ITERATIONS = -1
    while ITERATIONS == -1:
        im = Image.new('RGB', (w, h))
        draw = ImageDraw.Draw(im)
        for y in range(0, h, int(FONT_SIZE * 1.5)):
            for x in range(0, w, int(FONT_SIZE * 1.5)):
                s = get_symbol('all')
                if randint(0, 10) > 3:
                    draw.text((x, y), s, get_color(), font)
        if 0:
            im.show()
        else:
            title = hex(hash(datetime.datetime.now()))[2:] + '.jpg'
            path = 'images/' + title
            im.save(path)
            try:
                ### COMMENT THIS TO MAKE SCRIPT CHANGE YOUR WALLPAPERS
                # raise Exception
                
                from appscript import app, mactypes
                app('Finder').desktop_picture.set(mactypes.File(path))
                delete_others(title)
            except Exception:
                pass
        sleep(5)
        
        ### UNCOMMENT TO DO GENERATION ONLY ONE TIME

        # ITERATIONS += 1

if __name__ == '__main__':
        main()