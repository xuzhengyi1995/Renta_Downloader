# Renta_Downloader
Download manga you rent from http://renta.papy.co.jp/
# How to Use
1. Add your cookies in the program
2. Add your manga's url in base url and replace the page number as %d
3. Find out you **prd_ser** in your manga page's **index.view**, like this:
```javascript
var rt_id = "FIX001";
//******prd_ser******
var prd_ser = "480796";
//******prd_ser******
var disp_single = "0";
var print_flag = "0";
var animation = 'all 0.4s ease-out';
```
# TODO
1. Using threadpool to make it faster.
# Just for fun
