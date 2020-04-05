# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import os

# +
# プレイヤー・ラウンド・その他情報

# プレイヤー1情報
P1_name = 'MKLeo'
P1_fighter = ['Joker', 'Lucina', 'Wolf']
P1_color = [1, 7, 7]

# プレイヤー2情報
P2_name = 'ワニくん'
P2_fighter = ['kkr', 'incineroar',]
P2_color = [1, 1,]

# 左下に表示される文字（ラウンドなど）
Round = 'GRAND FINALS'

# 右下に表示される文字（ルールや大会名など）（変更必須）
Rules = 'とんスマ！ #2'

# +
# 変更が必要な項目

# 背景画像パス（変更必須）
opt_img_path = ''

# 大会アイコンパス（変更必須）
icon_path = ''

# 生成画像の保存場所パス&名前（変更必須）
opt_img_name = ''

# 文字フォントパス（Macは変更しなくてもよい）
opt_font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W7.ttc'

# VSの文字のフォントパス（Macは変更しなくてもよい）
vs_font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W9.ttc'

# 上下の文字が描かれる場所の背景色（RGBA:赤，緑，青，透明度）（変更推奨）
bg_color = (68, 5, 134, 127)

# 上下の文字色（カラーコード，RGBなど）
fg_color = '#FFFFFF'

# VSの色
vs_c = '#FFFFFF'

# vsの影設定
# VSの影を作るかどうか
border = True

# 影の色
vs_b = '#000000'

# 影の位置
bw = 9

# +
# 基本的に変更しなくて良い項目

# 大会アイコンの高さ（0以上1以下の値）
rate = 0.75

# VSの部分に書く文字
vs = 'VS'

# フォントサイズの最大値
opt_max_font_size = 100

# 同名の画像を生成したときに後ろに付ける最初の値
opt_img_name_num = 2

# +
# 変更禁止項目

# ファイター画像保存場所パス
fi_path = './fixing/fighter_image'

# マスク画像保存場所パス
mask_path = './fixing/mask/'

# 画像サイズ（変更すると機能しなくなります）
opt_img_size = (1920, 1080)

# +
# 以下変更不要

opt_text_size = ((opt_img_size[0]/2)*0.95, opt_img_size[1]-opt_img_size[0]/2)

vs_font_size = int(opt_img_size[0]/10)

P1_num = len(P1_fighter)
P2_num = len(P2_fighter)


# -

def image_resize(img, width):
    resize_image = img.resize((width, int(width * img.size[1] / img.size[0])))
    return resize_image


def image_resize_height(img, height):
    resize_image = img.resize((int(height * img.size[0] / img.size[1]), height))
    return resize_image


def mask_fighter_l2(a_fi, b_fi, img):
    mask = Image.open(mask_path + 'mask_l2_1.png')
    original_img_size = a_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(a_fi, (0, 0), mask)
    a_fi = cut.crop((0, 56, 438, 343))

    a_fi = image_resize(a_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(a_fi, (0, int(opt_img_size[1]-opt_img_size[0]/2)), a_fi)

    img = Image.alpha_composite(img, area)
    
    mask = Image.open(mask_path + 'mask_l2_2.png')
    original_img_size = b_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(b_fi, (0, 0), mask)
    b_fi = cut.crop((74, -24, 511, 318))

    b_fi = image_resize(b_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(b_fi, (0, int(opt_img_size[1]-b_fi.size[1])), b_fi)

    img = Image.alpha_composite(img, area)
    return img


def mask_fighter_r2(a_fi, b_fi, img):
    mask = Image.open(mask_path + 'mask_r2_1.png')
    original_img_size = a_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(a_fi, (0, 0), mask)
    a_fi = cut.crop((73, 56, 511, 343))

    a_fi = image_resize(a_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(a_fi, (int(opt_img_size[0]/2), int(opt_img_size[1]-opt_img_size[0]/2)), a_fi)

    img = Image.alpha_composite(img, area)
    
    mask = Image.open(mask_path + 'mask_r2_2.png')
    original_img_size = b_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(b_fi, (0, 0), mask)
    b_fi = cut.crop((0, -24, 438, 318))

    b_fi = image_resize(b_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(b_fi, (int(opt_img_size[0]/2), int(opt_img_size[1]-b_fi.size[1])), b_fi)

    img = Image.alpha_composite(img, area)
    return img


def mask_fighter_l3(a_fi, b_fi, c_fi, img):
    mask = Image.open(mask_path + 'mask_l3_1.png')
    original_img_size = a_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(a_fi, (0, 0), mask)
    a_fi = cut.crop((-86, 85, 426, 309))

    a_fi = image_resize(a_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(a_fi, (0, int(opt_img_size[1]-opt_img_size[0]/2)), a_fi)

    img = Image.alpha_composite(img, area)
    
    mask = Image.open(mask_path + 'mask_l3_2.png')
    original_img_size = b_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(b_fi, (0, 0), mask)
    b_fi = cut.crop((0, -62, 511, 382))

    b_fi = image_resize(b_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(b_fi, (0, int(opt_img_size[1]-opt_img_size[0]/2 + 2)), b_fi)

    img = Image.alpha_composite(img, area)
    
    mask = Image.open(mask_path + 'mask_l3_3.png')
    original_img_size = c_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(c_fi, (0, 0), mask)
    c_fi = cut.crop((85, 10, 597, 298))

    c_fi = image_resize(c_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(c_fi, (0, int(opt_img_size[1]-c_fi.size[1])), c_fi)

    img = Image.alpha_composite(img, area)
    return img


def mask_fighter_r3(a_fi, b_fi, c_fi, img):
    mask = Image.open(mask_path + 'mask_r3_1.png')
    original_img_size = a_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(a_fi, (0, 0), mask)
    a_fi = cut.crop((85, 85, 597, 309))

    a_fi = image_resize(a_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(a_fi, (int(opt_img_size[0]/2), int(opt_img_size[1]-opt_img_size[0]/2)), a_fi)

    img = Image.alpha_composite(img, area)
    
    mask = Image.open(mask_path + 'mask_r3_2.png')
    original_img_size = b_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(b_fi, (0, 0), mask)
    b_fi = cut.crop((0, -62, 511, 382))

    b_fi = image_resize(b_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(b_fi, (int(opt_img_size[0]/2), int(opt_img_size[1]-opt_img_size[0]/2 + 2)), b_fi)

    img = Image.alpha_composite(img, area)
    
    mask = Image.open(mask_path + 'mask_r3_3.png')
    original_img_size = c_fi.size
    
    cut = Image.new('RGBA', original_img_size, (255, 255, 255, 0))
    cut.paste(c_fi, (0, 0), mask)
    c_fi = cut.crop((-86, 10, 426, 298))

    c_fi = image_resize(c_fi, 960)

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(c_fi, (int(opt_img_size[0]/2), int(opt_img_size[1]-c_fi.size[1])), c_fi)

    img = Image.alpha_composite(img, area)
    return img


# +
# 画像読み込み、サイズ取得
img = Image.open(opt_img_path)
original_img_size = img.size

# 縮小
if original_img_size[0] / original_img_size[1] >= opt_img_size[0] / opt_img_size[1]:
    #目標より横長なら、縦横比を維持して、縦を目標まで縮める
    img.thumbnail((original_img_size[0], opt_img_size[1]))
    thumbnail_size = img.size
    #横幅を切り取るための計算をする
    crop_left = int((thumbnail_size[0] - opt_img_size[0]) / 2)
    crop_upper = 0
    crop_right = crop_left + opt_img_size[0]
    crop_lower = opt_img_size[1]
else:
    #目標より縦長なら、縦横比を維持して、横を目標まで縮める
    img.thumbnail((opt_img_size[0], original_img_size[1]))
    thumbnail_size = img.size
    #縦幅を切り取るための計算をする
    crop_left = 0
    crop_upper = int((thumbnail_size[1] - opt_img_size[1]) / 2)
    crop_right = opt_img_size[0]
    crop_lower = crop_upper + opt_img_size[1]

#計算した縦横で切り取る
img = img.crop((crop_left, crop_upper, crop_right, crop_lower))

# P1キャラ表示
# 画像読み込み、サイズ取得
if P1_num == 1:
    P1_fi_path = fi_path + '/' + P1_fighter[0] + '/img_' + str(P1_color[0]) + '.png'

    P1_fi = Image.open(P1_fi_path)
    original_img_size = P1_fi.size
    
    # リサイズ
    P1_fi = P1_fi.resize((int(opt_img_size[0]/2), int(opt_img_size[0]/2)))

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(P1_fi, (0, int(opt_img_size[1]-opt_img_size[0]/2)), P1_fi)

    img = Image.alpha_composite(img, area)

elif P1_num == 2:
    a_fi = Image.open(fi_path + '/' + P1_fighter[0] + '/img_' + str(P1_color[0]) + '.png')
    b_fi = Image.open(fi_path + '/' + P1_fighter[1] + '/img_' + str(P1_color[1]) + '.png')
    img = mask_fighter_l2(a_fi, b_fi, img)
    
elif P1_num == 3:
    a_fi = Image.open(fi_path + '/' + P1_fighter[0] + '/img_' + str(P1_color[0]) + '.png')
    b_fi = Image.open(fi_path + '/' + P1_fighter[1] + '/img_' + str(P1_color[1]) + '.png')
    c_fi = Image.open(fi_path + '/' + P1_fighter[2] + '/img_' + str(P1_color[2]) + '.png')
    img = mask_fighter_l3(a_fi, b_fi, c_fi, img)

# P2キャラ表示
# 画像読み込み、サイズ取得
if P2_num == 1:
    P2_fi_path = fi_path + '/' + P2_fighter[0] + '/img_' + str(P2_color[0]) + '.png'

    P2_fi = Image.open(P2_fi_path)
    original_img_size = P2_fi.size
    
    # リサイズ
    P2_fi = P2_fi.resize((int(opt_img_size[0]/2), int(opt_img_size[0]/2)))

    #塗りつぶし領域作成
    area = Image.new('RGBA', img.size, (255, 255, 255, 0))
    area.paste(P2_fi, (0, int(opt_img_size[1]-opt_img_size[0]/2)), P2_fi)

    img = Image.alpha_composite(img, area)

elif P2_num == 2:
    a_fi = Image.open(fi_path + '/' + P2_fighter[0] + '/img_' + str(P2_color[0]) + '.png')
    b_fi = Image.open(fi_path + '/' + P2_fighter[1] + '/img_' + str(P2_color[1]) + '.png')
    img = mask_fighter_r2(a_fi, b_fi, img)
    
elif P2_num == 3:
    a_fi = Image.open(fi_path + '/' + P2_fighter[0] + '/img_' + str(P2_color[0]) + '.png')
    b_fi = Image.open(fi_path + '/' + P2_fighter[1] + '/img_' + str(P2_color[1]) + '.png')
    c_fi = Image.open(fi_path + '/' + P2_fighter[2] + '/img_' + str(P2_color[2]) + '.png')
    img = mask_fighter_r3(a_fi, b_fi, c_fi, img)

# 大会アイコン表示
# 画像読み込み、サイズ取得
icon = Image.open(icon_path)
original_img_size = icon.size

# リサイズ
icon = image_resize_height(icon, int((opt_img_size[1]/2-opt_text_size[1])*rate))

#塗りつぶし領域作成
area = Image.new('RGBA', img.size, (255, 255, 255, 0))
area.paste(icon, (int((opt_img_size[0]-icon.size[0])/2), int(opt_img_size[1]/2+(opt_img_size[1]/2-opt_text_size[1]-icon.size[1])/2)), icon)

img = Image.alpha_composite(img, area)

# Round, Rules記述
for font_size in range(opt_max_font_size, 9, -1):
    #フォント
    font_l = ImageFont.truetype(opt_font_path, font_size)
    font_size_l = font_size

    # 各行の[幅、高さ]を計算
    lines_size_l = list(font_l.getsize(Round))

    if(lines_size_l[0] <= opt_text_size[0] and lines_size_l[1] <= opt_text_size[1]):
        break;
        
for font_size in range(opt_max_font_size, 9, -1):
    #フォント
    font_r = ImageFont.truetype(opt_font_path, font_size)
    font_size_r = font_size
    
    # 各行の[幅、高さ]を計算
    lines_size_r = list(font_r.getsize(Rules))

    if(lines_size_r[0] <= opt_text_size[0] and lines_size_r[1] <= opt_text_size[1]):
        break;

if font_size_l >= font_size_r:
    font = font_r
    # 各行の[幅、高さ]を計算
    lines_size_l = list(font.getsize(Round))
elif font_size_l < font_size_r:
    font = font_l
    # 各行の[幅、高さ]を計算
    lines_size_r = list(font.getsize(Rules))

#塗りつぶし領域作成
rectangle_img = Image.new('RGBA', img.size)
draw = ImageDraw.Draw(rectangle_img)
draw.rectangle((0, opt_img_size[1]-opt_text_size[1], opt_img_size[0], opt_img_size[1]), bg_color)

#塗りつぶし
org_img = img.convert('RGBA')
new_img = Image.alpha_composite(org_img, rectangle_img)

draw = ImageDraw.Draw(new_img)
_x = int(((opt_img_size[0]/2)-lines_size_l[0])/2)
_y = int(opt_img_size[1]-opt_text_size[1]+(opt_text_size[1]-lines_size_l[1])/2)
draw.text((_x, _y), Round, font=font, fill=fg_color)

_x = int(opt_img_size[0]/2+((opt_img_size[0]/2)-lines_size_r[0])/2)
_y = int(opt_img_size[1]-opt_text_size[1]+(opt_text_size[1]-lines_size_r[1])/2)
draw.text((_x, _y), Rules, font=font, fill=fg_color)

img = new_img

# Player_name記述
for font_size in range(opt_max_font_size, 9, -1):
    #フォント
    font_l = ImageFont.truetype(opt_font_path, font_size)
    font_size_l = font_size

    # 各行の[幅、高さ]を計算
    lines_size_l = list(font_l.getsize(P1_name))

    if(lines_size_l[0] <= opt_text_size[0] and lines_size_l[1] <= opt_text_size[1]):
        break;

for font_size in range(opt_max_font_size, 9, -1):
    #フォント
    font_r = ImageFont.truetype(opt_font_path, font_size)
    font_size_r = font_size

    # 各行の[幅、高さ]を計算
    lines_size_r = list(font_r.getsize(P2_name))

    if(lines_size_r[0] <= opt_text_size[0] and lines_size_r[1] <= opt_text_size[1]):
        break;

if font_size_l >= font_size_r:
    font = font_r
    # 各行の[幅、高さ]を計算
    lines_size_l = list(font.getsize(P1_name))
elif font_size_l < font_size_r:
    font = font_l
    # 各行の[幅、高さ]を計算
    lines_size_r = list(font.getsize(P2_name))

#塗りつぶし領域作成
rectangle_img = Image.new('RGBA', img.size)
draw = ImageDraw.Draw(rectangle_img)
draw.rectangle((0, 0, opt_img_size[0], opt_text_size[1]), bg_color)

#塗りつぶし
org_img = img.convert('RGBA')
new_img = Image.alpha_composite(org_img, rectangle_img)

draw = ImageDraw.Draw(new_img)
_x = int(((opt_img_size[0]/2)-lines_size_l[0])/2)
_y = int((opt_text_size[1]-lines_size_l[1])/2)
draw.text((_x, _y), P1_name, font=font, fill=fg_color)

_x = int(opt_img_size[0]/2+((opt_img_size[0]/2)-lines_size_r[0])/2)
_y = int((opt_text_size[1]-lines_size_r[1])/2)
draw.text((_x, _y), P2_name, font=font, fill=fg_color)

# VSフォント表示
font_vs = ImageFont.truetype(vs_font_path, vs_font_size)
lines_size_vs = list(font_vs.getsize('VS'))

_x = int((opt_img_size[0]-lines_size_vs[0])/2)
_y = int(opt_img_size[1]/2-lines_size_vs[1])

if border:
    draw.text((_x, _y+bw), vs, font=font_vs, fill=vs_b)

draw.text((_x, _y), vs, font=font_vs, fill=vs_c)

if os.path.exists(opt_img_name + '.png'):
    while os.path.exists(opt_img_name + '_' + str(opt_img_name_num) + '.png'):
        opt_img_name_num += 1
    new_img.save(opt_img_name + '_' + str(opt_img_name_num) + '.png')
else:
    new_img.save(opt_img_name + '.png')
# -


