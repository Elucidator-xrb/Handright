from PIL import Image, ImageFont
from handright import Template, handwrite

with open("article/荷塘月色.txt", encoding='utf-8') as f:
    text = f.read()

background = Image.open('background/letter.png')
height = background.height
width = background.width

template = Template(
    # background=background,
    Image.new(mode="1", size=(2480, 3580), color=1),
    font=ImageFont.truetype("font/行书钢笔字体.ttf", size=50),
    line_spacing=50,
    fill=0,  # 字体“颜色”
    left_margin=80,
    top_margin=60,
    right_margin=80,
    bottom_margin=100,
    word_spacing=-1,
    line_spacing_sigma=1,  # 行间距随机扰动
    font_size_sigma=1,  # 字体大小随机扰动
    word_spacing_sigma=1,  # 字间距随机扰动
    end_chars="，。”",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=0.5,  # 笔画横向偏移随机扰动
    perturb_y_sigma=0.5,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.03,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    print("img{}.png generated".format(i))
    im.save("output/img{}.png".format(i))
    if i >= 10:
        break
print("task finished")
