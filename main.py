
from getHtml import GetHtml
import PIL.Image as image
from io import BytesIO
import math

header = {}
# ********SETTINGS********
prd_ser = 480796
max_loop = 20
header['Cookie'] = "YOUR_COOKIE_HERE"
# Manga URL
base_url = "http://dre-ap-pc2.papy.co.jp/sc/view_jsimg2/0c720e43cc4ce9067d/9-480796-84/FIX001/%d?type=6"
sum_page = 204
# ********SETTINGS********


def f_shuffle_r(ar_number, snum, x_idx, y):
    gn = kn = int(y / 2)
    if(y % 2 != 0):
        gn += 1
        kn += 1
    ar_g = [-1 for i in range(gn)]
    ar_k = [-1 for i in range(kn)]
    g_cnt = k_cnt = 0

    ar_tmp = [-1 for i in range(y)]
    cnt = 0
    if(snum % 2 == 0):
        for i in range(y):
            if (i % 2 == 0):
                ar_g[g_cnt] = ar_number[i][x_idx]
                g_cnt += 1
            else:
                ar_k[k_cnt] = ar_number[i][x_idx]
                k_cnt += 1
        for i in range(gn):
            if(ar_k[i] != -1):
                ar_tmp[cnt] = ar_k[i]
                cnt += 1
            if(ar_g[i] != -1):
                ar_tmp[cnt] = ar_g[i]
                cnt += 1
    else:
        for i in range(y):
            if(i < gn):
                ar_g[g_cnt] = ar_number[i][x_idx]
                g_cnt += 1
            else:
                ar_k[k_cnt] = ar_number[i][x_idx]
                k_cnt += 1
        for i in range(gn):
            if(ar_g[i] != -1):
                ar_tmp[cnt] = ar_g[i]
                cnt += 1
            if(ar_k[i] != -1):
                ar_tmp[cnt] = ar_k[i]
                cnt += 1

    for i in range(y):
        ar_number[i][x_idx] = ar_tmp[i]

    del ar_tmp
    del ar_g
    del ar_k
    return ar_number


getter = GetHtml()

header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
header['Host'] = 'dre-ap-pc2.papy.co.jp'
header['Accept-Encoding'] = 'gzip, deflate, br'
header['Connection'] = 'keep-alive'
header['Upgrade-Insecure-Requests'] = '1'
header['Accept-Language'] = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'

for page in range(1, sum_page):
    x = 7
    y = 7
    url = base_url % page

    getter.set(url, header=header, retryTimes=5)
    data = bytearray(getter.get())

    head_length = int(data[:9])

    s_data = str(data[9:9 + head_length].decode("ascii")).split("|")
    img_data = data[head_length + 9:]

    width = int(s_data[0])
    height = int(s_data[1])

    diff_w_idx = s_data[2]
    diff_h_idx = s_data[3]

    s_data = s_data[4:]

    after_width = int(width / x)
    after_height = int(height / y)
    diff_w = (width % x)
    diff_h = (height % y)

    FinalImage = image.new('RGB', (width, height))
    if(diff_w != 0 or diff_h != 0):
        if(diff_w != 0 and diff_h == 0):
            location, length = diff_w_idx.split(',')
            src_img = img_data[int(location):int(location) + int(length)]
            file_data = BytesIO(src_img)
            og_img = image.open(file_data)
            FinalImage.paste(og_img, (0, 0))
        elif(diff_w == 0 and diff_h != 0):
            location, length = diff_h_idx.split(',')
            src_img = img_data[int(location):int(location) + int(length)]
            file_data = BytesIO(src_img)
            og_img = image.open(file_data)
            FinalImage.paste(og_img, (0, 0))
        else:
            location, length = diff_w_idx.split(',')
            src_img = img_data[int(location):int(location) + int(length)]
            file_data = BytesIO(src_img)
            og_img = image.open(file_data)
            FinalImage.paste(og_img, (0, 0))

            location, length = diff_h_idx.split(',')
            src_img = img_data[int(location):int(location) + int(length)]
            file_data = BytesIO(src_img)
            og_img = image.open(file_data)
            FinalImage.paste(og_img, (0, 0))

    ar_number = [[i * x + j for j in range(y)] for i in range(x)]
    print(ar_number)
    for i in range(y):
        ar_tmp = [0 for i in range(x)]
        st = x - i % x
        for j in range(x):
            if(st >= x):
                st = 0
            ar_tmp[j] = ar_number[i][st]
            st += 1
        for j in range(x):
            ar_number[i][j] = ar_tmp[j]

    for i in range(x):
        ar_tmp = [0 for i in range(y)]
        st = y - i % y
        for j in range(y):
            if(st >= y):
                st = 0
            ar_tmp[j] = ar_number[st][i]
            st += 1
        for j in range(y):
            ar_number[j][i] = ar_tmp[j]

    for i in range(x):
        num = i + 1
        seed = page + prd_ser
        if (seed % max_loop == 0):
            seed = math.fabs(page - prd_ser) + (max_loop + 1)
        k = int(((num * seed) + (page / max_loop)) % max_loop)
        for j in range(k - 1, -1, -1):
            ar_number = f_shuffle_r(ar_number, j, i, y)

    total = x * y
    ar_didx = [0 for i in range(total)]
    for i in range(y):
        for j in range(x):
            d_stx = diff_w + (j * after_width)
            d_sty = diff_h + (i * after_height)
            number = ar_number[i][j]
            ar_didx[number] = (d_stx, d_sty)
    print(ar_number)

    img_arr = []
    for i in s_data:
        location, length = i.split(',')
        img_arr.append(img_data[int(location):int(location) + int(length)])

    for i in range(total):
        x, y = ar_didx[i]
        file_data = BytesIO(img_arr[i])
        og_img = image.open(file_data)
        FinalImage.paste(og_img, (x, y))
    with open('./%d.jpg' % page, "wb") as f:
        FinalImage.save(f)
