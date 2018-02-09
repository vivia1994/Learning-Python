# 切片、旋转、滤镜、输出文字、调色板

# 缩放图像
# from PIL import Image
# # 打开一个jpg图像文件，注意是当前路径:
# im = Image.open(r'_Data\images\cat.jpg')
# # 获得图像尺寸:
# w, h = im.size
# print('Resize image to: {} x {}'.format(w, h))
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# print('Resize image to: {} x {}'.format(w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save(r'_Data\images\thumbnail.jpg', 'jpeg')


#模糊
# from PIL import Image,ImageFilter
# im = Image.open(r'_Data\images\cat.jpg')
# im2=im.filter(ImageFilter.BLUR)
# im2.save(r'_Data\images\blur.jpg',"jpeg")


# 生成字母验证码图片
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
#
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype(r'C:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_10.0.14393.0_none_9ff7dbaac40db853\Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save(r'_Data\images\vertification_code.jpg', 'jpeg')