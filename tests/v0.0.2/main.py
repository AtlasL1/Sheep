# pip install -i https://test.pypi.org/simple/ Sheep==0.0.2
from sheep import page
page.create()
page.set_title('hi')
page.set_icon('https://cdn.discordapp.com/avatars/860794014764105729/404b7a92d2f882705e5b864dcdd807bf.webp?size=1024&format=webp&width=0&height=320')
page.set_background(image='https://i.pinimg.com/736x/cf/92/99/cf9299fb011122c844c904e66c0833cf.jpg', image_repeat=False, image_size='cover')
page.write(language='zh', style='H1', content=f'This is the first Sheep site built with Sheep and atm it\'s horrible anyway check out the code', link_text='code', url='https://github.com/AtlasL1/Sheep', new_tab=True, size='29px', font='Roboto', colour='yellow')
page.style_links(text_colour='yellow', hover_colour='orange', visited_colour='yellow', active_colour='')
page.view_page()
