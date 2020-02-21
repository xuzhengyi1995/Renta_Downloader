# Renta_Downloader

Download manga you rent from <http://renta.papy.co.jp/>

[2020-02-01] Make it easier to use, add threadpool to make downloading faster

[2019-10-31] Changed to fit the new version of Renta.

# How to Use

**Now no need to find anything on the webpage, just put the cookie and url is ready for use.**

0.  Install python packages _pillow_ and _threadpool_.

    ```shell
    pip install Pillow
    pip install threadpool
    ```

1.  Change the `imgdir` in the main.py to indicate where to put the manga.

2.  Add your cookies in the program.

    **Remember to use F12 to see the cookies!**

    **Because some http only cookies can not be seen by javascript!**

    **~~Remember that now we should change the cookie each downloading! It means that one cookie for one manga for a period time. Change the manga, Change the cookie!~~**

    **Maybe no need to change, but if the program not work, you can try to refresh the cookies.**

    > 1.  Open the page.
    > 2.  Press F12.
    > 3.  Click on the _Network_.
    > 4.  Refresh the page.
    > 5.  Find the first _index.view_ request, click it.
    > 6.  On the right, there will be a _Request Headers_, go there.
    > 7.  Find the _cookie:...._, copy the string after the _cookie:_, paste to the _main.py_, _YOUR_COOKIES_HERE_

3.  Change the _url_ in the _main.py_.

    The URL is finished with **index.view**, here we use the manga [魔法使いの嫁](https://dre-viewer.papy.co.jp/sc/view_jsimg2/sample/9-265205-84/FIX001/index.view).

    This is the URL of the **魔法使いの嫁**: <https://dre-viewer.papy.co.jp/sc/view_jsimg2/sample/9-265205-84/FIX001/index.view>

    **If you want to download ebookrenta, just do the same thing but change the url to the ebookrenta:<http://us-dre4.ebookrenta.com/sc/view_jsimg2_en/3a2d4f07050062a785/9-671847-84/rbc1002/index.view>**

    Just copy this URL to the `url` in _main.py_.

4.  After edit the program, run `python main.py` to run it.

# Notice

1.  The `poolsize` by default is 5, it's already fast enough I think, you can change it but be careful that the server may **ban your ip or account** (I'm not sure, but be careful).
