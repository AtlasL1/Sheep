# pip install -i https://test.pypi.org/simple/ Sheep==0.0.3
from sheep import page
page.create()
page.set_title('sheep??????')
page.set_icon('https://i.pinimg.com/564x/66/a0/6d/66a06d5f33a803738c7747618c94e4d8.jpg')
page.set_background(image='https://i.pinimg.com/736x/cf/92/99/cf9299fb011122c844c904e66c0833cf.jpg', image_repeat=False, image_size='cover')
page.write(language='zh', style='H1', content=f'This is the first Sheep site built with Sheep and atm it\'s horrible anyway check out the code', link_text='code', url='https://github.com/AtlasL1/Sheep', new_tab=True, size='29px', font='Roboto', colour='yellow')
page.style_links(text_colour='yellow', hover_colour='orange', visited_colour='yellow', active_colour='')
page.add_button(text='link to code again but it\'s a button this time', onclick='alert(\'hideous repo with hideous code incoming\')', border='none', border_after='none', text_decoration='underline', text_decoration_style='wavy', text_decoration_thickness='2px', text_decoration_colour='orange', background_colour='yellow', text_decoration_after='underline', text_decoration_colour_after='yellow', text_decoration_style_after='wavy', text_decoration_thickness_after='2px', background_colour_after='orange', url='https://github.com/AtlasL1/Sheep', new_tab=True)
page.view_page()
