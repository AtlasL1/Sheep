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

def style_links(text_colour='blue', visited_colour='purple', hover_colour='darkblue', active_colour='blue'):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<style>\na:link {{color: {text_colour};}}\na:visited {{color: {visited_colour};}}\na:hover {{color: {hover_colour};}}\na:active {{color: {active_colour};}}</style>\n')

def write(style='p', size='', font='Times New Roman', content='DEFAULT TEXT', colour='black', language='en', link_text='', url='', new_tab='False'):
    styles = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P']
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if style in styles:
            if style == 'p':
                size = '12px'
            if link_text in content:
                if new_tab is True:
                    content = content.replace(link_text, f'<a href="{url}" target="_blank">{link_text}</a>')
                else:
                    content = content.replace(link_text, f'<a href="{url}">{link_text}</a>')
                link_text = ''
            else:
                content += f' <a href="{url}">{link_text}</a>'
            with open(f'{global_file_name}.html', 'a') as file:
                file.write(f'<body>\n<{style.lower()} lang=\'{language}\' style=\'color:{colour}; font-size: {size}; font-family: "{font}"\'>{content}</{style.lower()}>\n</body>\n')
        else:
            raise ValueError('Unknown text style.')

def view_page():
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        file_path = f'{global_file_name}.html'
        webbrowser.open(file_path, new=2)
