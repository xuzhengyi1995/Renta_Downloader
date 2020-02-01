# use urllib to get resources

import socket
import urllib.request


class GetHtml:
    def __init__(self):
        self._url = 'http://www.google.com'

    def set(self, url, header=None, retryTimes=10):
        '''
        url: url to get
        header: as {'Accept':'application/json'}
        '''
        self._url = url
        self._header = header
        self._retryTimes = retryTimes

    def get(self):
        req = urllib.request.Request(self._url)
        if(self._header):
            for key in self._header:
                req.add_header(key, self._header[key])

        is_error = True
        s_retry = 0
        r_data = None
        while(is_error and s_retry < 10):
            try:
                r = urllib.request.urlopen(req, timeout=5)
                r_data = r.read()
                is_error = False
            except urllib.error.HTTPError:
                is_error = True
                s_retry += 1
                print('HTTPError Retry', s_retry, 'times')
            except urllib.error.URLError:
                is_error = True
                s_retry += 1
                print('URLError Retry', s_retry, 'times')
            except socket.timeout:
                is_error = True
                s_retry += 1
                print('SOCKETError Retry', s_retry, 'times')

        return r_data
