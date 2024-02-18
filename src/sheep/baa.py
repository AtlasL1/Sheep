# Sheep
# Baa.py

import os
global_file_name = None

def create(file_name='index', path=''):
    global global_file_name
    global_file_name = file_name
    if path and not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, f'{file_name}.html'), 'w') as file:
        file.write('<!DOCTYPE html>\n<html>\n')

def set_background(colour='white', image='', repeat='True', attachment='fixed', size='cover'):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            if image:
                bg_repeat = 'repeat' if repeat else 'no-repeat'
                file.write(f'<style>\nbody {{\nbackground-image: url(\'{image}\');\nbackground-repeat: {bg_repeat};\nbackground-attachment: {attachment};\nbackground-size: {size}\n}}\n</style>\n')
            else:
                file.write(f'<style>\nbody {{background-color: {colour};}}\n</style>\n')

def write(style='p', content='DEFAULT TEXT', colour='black', language='en'):
    styles = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P']
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if style in styles:
            with open(f'{global_file_name}.html', 'a') as file:
                file.write(f'<body>\n<{style.lower()} lang=\'{language}\' style=\'color:{colour}\'>{content}</{style.lower()}>\n</body>')
        else:
            raise ValueError('Unknown text style.')
