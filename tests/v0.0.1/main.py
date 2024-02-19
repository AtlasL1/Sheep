# pip install -i https://test.pypi.org/simple/ Sheep==0.0.1
from sheep import baa
baa.create()
baa.set_background(image='https://i.pinimg.com/736x/cf/92/99/cf9299fb011122c844c904e66c0833cf.jpg', image_repeat=False, image_size='cover')
baa.write(language='zh', style='H1', content='This is the first Sheep site built with Sheep and atm it\'s horrible', size='29px', font='Roboto', colour='yellow')
baa.view_page()
