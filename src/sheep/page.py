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

def set_icon(path=''):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<link rel="icon" href="{path}">')

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

def add_font(src=''):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<head>\n<link href="{src}" rel="stylesheet" type="text/css">\n</head>\n')

def style_links(text_colour='blue', visited_colour='purple', hover_colour='darkblue', active_colour='blue'):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<style>\na:link {{color: {text_colour};}}\na:visited {{color: {visited_colour};}}\na:hover {{color: {hover_colour};}}\na:active {{color: {active_colour};}}\n</style>\n')

def write(style='P', size='', font='Times New Roman', content='DEFAULT TEXT', colour='black', language='en', link_text='', url='', new_tab=False, bold_text='', italic_text='', subscript_text='', superscript_text=''):
    styles = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P']
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if style in styles:
            if style == 'P':
                size = '12px'
            if link_text in content:
                if new_tab:
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

def add_image(path='', alt_text='', url=None, new_tab=False):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write('<body>\n')
            if url is not None:
                if new_tab:
                    file.write(f'<a href="{url}" target="_blank">')
                else:
                    file.write(f'<a href="{url}">')
            file.write(f'<img src="{path}" alt="{alt_text}">')
            if url is not None:
                file.write('</a>')
            file.write('\n</body>\n')

def add_button(text='Button', onclick='alert(\'Default Response\')', border='none', border_after='none', colour='black', colour_after='black', padding='15px 32px', text_align='center', text_decoration='none', text_decoration_colour='black', text_decoration_style='solid', text_decoration_thickness='auto', text_decoration_after='none', text_decoration_colour_after='black', text_decoration_style_after='solid', text_decoration_thickness_after='auto', display='inline', font_size='16px', margin='4px 2px', transition_duration='0.2s', cursor='pointer', background_colour='#D8D8D8', background_colour_after='#D8D8D8', url='', new_tab='False'):
    text_aligns = ['left', 'center', 'right']
    text_decorations = ['none', 'underline', 'overline', 'line-through']
    text_decoration_styles = ['solid', 'double', 'dotted', 'dashed', 'wavy', 'initial', 'inherit']
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if text_align in text_aligns and text_decoration in text_decorations and text_decoration_style in text_decoration_styles and text_decoration_after in text_decorations and text_decoration_style_after in text_decoration_styles and url:
            if new_tab is True:
                with open(f'{global_file_name}.html', 'a') as file:
                    file.write(f'<style>\n.button {{\nborder: {border_after};\ncolor: {colour};\npadding: {padding};\ntext-align: {text_align};\ntext-decoration: {text_decoration_after};\ntext-decoration-color: {text_decoration_colour_after};\ntext-decoration-style: {text_decoration_style_after};\ntext-decoration-thickness: {text_decoration_thickness_after};\ndisplay: {display};\nfont-size: {font_size};\nmargin: {margin};\ntransition-duration: {transition_duration};\ncursor: {cursor};\n}}\n.button1 {{\nbackground-color: {background_colour};\ncolor: {colour};\nborder: {border};\ntext-decoration: {text_decoration};\ntext-decoration-style: {text_decoration_style};\ntext-decoration-color: {text_decoration_colour};\ntext-decoration-thickness: {text_decoration_thickness}\n}}\n.button1:hover {{\nborder: {border_after};\nbackground-color: {background_colour_after};\ncolor: {colour_after};\ntext-decoration: {text_decoration_after};\ntext-decoration-color: {text_decoration_colour_after};\ntext-decoration-style: {text_decoration_style_after};\ntext-decoration-thickness: {text_decoration_thickness_after};\n}}\n</style>\n<body>\n<a href="{url}" target="_blank"><button type="button" class="button button1" onclick="{onclick}">{text}</button></a>\n</body>\n')
            elif new_tab is not True:
                with open(f'{global_file_name}.html', 'a') as file:
                    file.write(f'<style>\n.button {{\nborder: {border_after};\ncolor: {colour};\npadding: {padding};\ntext-align: {text_align};\ntext-decoration: {text_decoration_after};\ntext-decoration-color: {text_decoration_colour_after};\ntext-decoration-style: {text_decoration_style_after};\ntext-decoration-thickness: {text_decoration_thickness_after};\ndisplay: {display};\nfont-size: {font_size};\nmargin: {margin};\ntransition-duration: {transition_duration};\ncursor: {cursor};\n}}\n.button1 {{\nbackground-color: {background_colour};\ncolor: {colour};\nborder: {border};\ntext-decoration: {text_decoration};\ntext-decoration-style: {text_decoration_style};\ntext-decoration-color: {text_decoration_colour};\ntext-decoration-thickness: {text_decoration_thickness}\n}}\n.button1:hover {{\nborder: {border_after};\nbackground-color: {background_colour_after};\ncolor: {colour_after};\ntext-decoration: {text_decoration_after};\ntext-decoration-color: {text_decoration_colour_after};\ntext-decoration-style: {text_decoration_style_after};\ntext-decoration-thickness: {text_decoration_thickness_after};\n}}\n</style>\n<body>\n<a href="{url}"><button type="button" class="button button1" onclick="{onclick}">{text}</button></a>\n</body>\n')
        elif text_align in text_aligns and text_decoration in text_decorations and text_decoration_style in text_decoration_styles and text_decoration_after in text_decorations and text_decoration_style_after in text_decoration_styles:
            with open(f'{global_file_name}.html', 'a') as file:
                file.write(f'<style>\n.button {{\nborder: {border_after};\ncolor: {colour};\npadding: {padding};\ntext-align: {text_align};\ntext-decoration: {text_decoration_after};\ntext-decoration-color: {text_decoration_colour_after};\ntext-decoration-style: {text_decoration_style_after};\ntext-decoration-thickness: {text_decoration_thickness_after};\ndisplay: {display};\nfont-size: {font_size};\nmargin: {margin};\ntransition-duration: {transition_duration};\ncursor: {cursor};\n}}\n.button1 {{\nbackground-color: {background_colour};\ncolor: {colour};\nborder: {border};\ntext-decoration: {text_decoration};\ntext-decoration-style: {text_decoration_style};\ntext-decoration-color: {text_decoration_colour};\ntext-decoration-thickness: {text_decoration_thickness}\n}}\n.button1:hover {{\nborder: {border_after};\nbackground-color: {background_colour_after};\ncolor: {colour_after};\ntext-decoration: {text_decoration_after};\ntext-decoration-color: {text_decoration_colour_after};\ntext-decoration-style: {text_decoration_style_after};\ntext-decoration-thickness: {text_decoration_thickness_after};\n}}\n</style>\n<body>\n<button type="button" class="button button1" onclick="{onclick}">{text}</button>\n</body>\n')
        elif text_align not in text_aligns:
            raise ValueError(f'The value {text_align} is not found.')
        elif text_decoration not in text_decorations:
            raise ValueError(f'The value {text_decoration} is not found.')
        elif text_decoration_style not in text_decoration_styles:
            raise ValueError(f'The value {text_decoration_style} is not found.')
        elif text_decoration_after not in text_decorations:
            raise ValueError(f'The value {text_decoration_after} is not found.')
        elif text_decoration_style_after not in text_decoration_styles:
            raise ValueError(f'The value {text_decoration_style_after} is not found.')

def line_break(number='1'):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<p>')
            for _ in range(int(number)):
                file.write('<br>')
            file.write('</p>')

class List:
    def __init__(self, file_name, list_id, list_type='unordered'):
        self.file_name = file_name
        self.list_id = list_id
        self.list_type = list_type

    def add_item(self, size='', font='Times New Roman', content='DEFAULT TEXT', colour='black', link_text='', url='', new_tab=False):
        if link_text in content:
            if new_tab:
                content = content.replace(link_text, f'<a href="{url}" target="_blank">{link_text}</a>')
            else:
                content = content.replace(link_text, f'<a href="{url}">{link_text}</a>')
            link_text = ''
        else:
            content += f' <a href="{url}">{link_text}</a>'
        with open(f'{self.file_name}.html', 'a') as file:
            file.write(f'<li style="font-size: {size}; font-family: {font}; color: {colour};">{content}</li>\n')

    def close_list(self):
        with open(f'{self.file_name}.html', 'a') as file:
            if self.list_type == 'unordered':
                file.write('</ul>\n</body>\n')
            elif self.list_type == 'ordered':
                file.write('</ol>\n</body>\n')

def add_list(type='unordered'):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        types = ['ordered', 'unordered']
        if type in types:
            with open(f'{global_file_name}.html', 'a') as file:
                if type == 'unordered':
                    file.write(f'<body>\n<ul>\n')
                elif type == 'ordered':
                    file.write(f'<body>\n<ol>\n')
        else:
            raise ValueError('Invalid list type.')
    return List(global_file_name, id, type)

def add_iframe(src='', height='200', width='300', title=''):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<body>\n<iframe src="{src}" height="{height}" width="{width}" title="{title}"></iframe>\n</body>\n')

def add_audio(src='', type='mpeg', unsupported_text='Your browser does not support the audio element.', autoplay=False):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if autoplay is True:
            with open(f'{global_file_name}.html', 'a') as file:
                file.write(f'<body>\n<audio controls autoplay>\n<source src="{src}" type="audio/{type}">\n{unsupported_text}\n</audio>\n</body>\n')
        else:
            with open(f'{global_file_name}.html', 'a') as file:
                file.write(f'<body>\n<audio controls>\n<source src="{src}" type="audio/{type}">\n{unsupported_text}\n</audio>\n</body>\n')

def add_video(src='', width='320', height='240', type='mp4', unsupported_text='Your browser does not support the video element.', autoplay=False, controls=True, muted=False):
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        attributes = f'width="{width}" height="{height}"'
        if autoplay is True:
            attributes += ' autoplay'
        if controls is True:
            attributes += ' controls'
        if muted is True:
            attributes += ' muted'
        with open(f'{global_file_name}.html', 'a') as file:
            file.write(f'<body>\n<video{attributes}>\n<source src="{src}" type="video/{type}"{unsupported_text}\n</video>\n</body>\n')

def add_blocked_text(text_style='P', text_size='12px', block_thickness='1px', block_style='solid', text='DEFAULT TEXT', block_colour='black', font='Times New Roman', text_colour='black'):
    text_styles = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'P']
    block_styles = ['dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset', 'none', 'hidden']
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        if text_style in text_styles:
            if text_style == 'P':
                size = '12px'
            if block_style in block_styles:
                with open(f'{global_file_name}.html', 'a') as file:
                    file.write(f'<body>\n<{text_style.lower()} style="font-size: {text_size}; border: {block_thickness} {block_style} {block_colour}; font-family: {font}; color: {text_colour}">{text}</{text_style.lower()}>\n</body>\n')
            else:
                raise ValueError('Unknown block style.')
        else:
            raise ValueError('Unknown text style.')

def view_page():
    global global_file_name
    if global_file_name is None:
        raise ValueError('File not found.')
    else:
        file_path = f'{global_file_name}.html'
        webbrowser.open(file_path, new=2)
        
