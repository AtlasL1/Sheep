# Sheep
# Page.py

import os
import webbrowser

global_file_name = None

def create(file_name='index', path=''):
    global global_file_name
    global_file_name = file_name
    if path and not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, f'{file_name}.html'), 'w') as file:
        file.write('<!DOCTYPE html>\n<html>\n')

def set_title(name=''):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<title>{name}</title>')

def set_icon(url=''):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<link rel="icon" href="{url}">')

def set_background(colour='white', image='', image_repeat='True', image_attachment='scroll', image_size='cover'):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            if image:
                bg_repeat = 'repeat' if image_repeat else 'no-repeat'
                file.write(f'<style>\nbody {{\nbackground-image: url(\'{image}\');\nbackground-repeat: {bg_repeat};\nbackground-attachment: {image_attachment};\nbackground-size: {image_size}\n}}\n</style>\n')
            else:
                file.write(f'<style>\nbody {{background-color: {colour};}}\n</style>\n')

def write(style='p', size='', font='Times New Roman', content='DEFAULT TEXT', colour='black', language='en'):
    styles = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P']
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if style in styles:
            if style == 'p':
                size = '12px'
            with open(f'{global_file_name}.html', 'a') as file:
                file.write(f'<body>\n<{style.lower()} lang=\'{language}\' style=\'color:{colour}; font-size: {size}; font-family: "{font}"\'>{content}</{style.lower()}>\n</body>')
        else:
            raise ValueError('Unknown text style.')

def view_page():
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        file_path = f'{global_file_name}.html'
        webbrowser.open(file_path, new=2)

create()
set_title('hi')
set_icon('https://cdn.discordapp.com/avatars/860794014764105729/404b7a92d2f882705e5b864dcdd807bf.webp?size=1024&format=webp&width=0&height=320')
set_background(image='https://i.pinimg.com/736x/cf/92/99/cf9299fb011122c844c904e66c0833cf.jpg', image_repeat=False, image_size='cover')
write(language='zh', style='H1', content='This is the first Sheep site built with Sheep and atm it\'s horrible', size='29px', font='Roboto', colour='yellow')
view_page()
