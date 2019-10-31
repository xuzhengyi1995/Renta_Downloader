# Renta_Downloader

Download manga you rent from <http://renta.papy.co.jp/>

[2019-10-31] Changed to fit the new version of Renta.

# How to Use

0.  Change the `imgdir` in the main.py to indicate where to put the manga.

1.  Add your cookies in the program.

2.  Add your manga's url in base url and replace the page number as %d, now it's a little bit complicate.

Also on the page **index.view**, here we use the manga [魔法使いの嫁](https://dre-viewer.papy.co.jp/sc/view_jsimg2/sample/9-265205-84/FIX001/index.view).

On this link: <https://dre-viewer.papy.co.jp/sc/view_jsimg2/sample/9-265205-84/FIX001/index.view> We should find the variables below:

**max_page**: `sum_page` in main.py, how many page this manga have.

**url_base2**: `base_url` in main.py, remember to add a %d in the end of this string.

**cache_update**: `cache_update` in main.py, used to build the base_url, if don't have this, give it `None`.

**auth_key**: `auth_key` in the main.py, used to build the base_url.

```javascript
var OpenLR = 1;    		//右開きフラグ(1:右開き)
var page=1;				//現在のページ
var page_back = -1;
var set_page=1;			//栞更新用


//******sum_page in main.py******
var max_page = 50;		//総ページ数
//******sum_page in main.py******


var user_id = "sample";      //ユーザID
var m_line="";			//目次情報
var en_flag = 0;		//海外版と日本語版の判別(1:英語版 0:日本語版)
var cnts_type = "6";	// コンテンツtype
var url_bookmark = "https://dre-viewer2.papy.co.jp/sc/bookmark/sample/9-265205-84/FIX001/";
var url_base = "/sc/view_jsimg2/sample/9-265205-84/FIX001/";


//******base_url in main.py******
// This is the base_url on main.py, but add a %d to the end:
// https://dre-aka-f.papy.co.jp/filesv/sc/contents/265205/6s/1/%d
var url_base2 = "https://dre-aka-f.papy.co.jp/filesv/sc/contents/265205/6s/1/";
//******base_url in main.py******


var url_base2_papy = "https://dre-papy-f.papy.co.jp/filesv/sc/contents_papy/265205/6s/1/FIX001/";
var ar_edge = url_base2.split("/");
var edge = ar_edge[2];
var rt_id = "FIX001";


//******cache_update in main.py******
var cache_update = "201903230013";
//******cache_update in main.py******


//******prd_ser in main.py******
var prd_ser = "265205";
//******prd_ser in main.py******


var disp_single = "0";
var print_flag = "0";
var viewer_mode = "akamai";


//******auth_key_papy in main.py******
var auth_key = "auth-key=exp=1572532993~acl=%2Ffilesv%2Fsc%2Fcontents%2F265205%2F6s%2F1%2F%2A~hmac=012471b45afef8db1093314b63bf7f62659f01f875a895c4e5bbfe16930f4023";
//******auth_key_papy in main.py******
```

3.  Find out you **prd_ser** in your manga page's **index.view**, like this:

```javascript
var rt_id = "FIX001";
//******prd_ser******
var prd_ser = "480796";
//******prd_ser******
var disp_single = "0";
var print_flag = "0";
var animation = 'all 0.4s ease-out';
```

4.  After edit the program, run `python main.py` to run it.

# TODO

1.  Using threadpool to make it faster.
