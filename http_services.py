# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:07:55 2022

@author: -Imran Ahmed
Objective: Get bitcoin rate from website 
URL : https://rate.sx

"""

import sys, urllib3, requests, time

def requests_func():
        
    menu = "Requests is ready for today’s web.\n"
    menu += "Keep-Alive & Connection Pooling \n"
    menu += "International Domains and URLs \n"
    menu += "Sessions with Cookie Persistence \n"
    menu += "Browser-style SSL Verification \n"
    menu += "Automatic Content Decoding \n"
    menu += "Basic/Digest Authentication \n"
    menu += "Elegant Key/Value Cookies \n"
    menu += "Automatic Decompression \n"
    menu += "Unicode Response Bodies \n"
    menu += "HTTP(S) Proxy Support \n"
    menu += "Multipart File Uploads \n"
    menu += "Streaming Downloads \n"
    menu += "Connection Timeouts \n"
    menu += "Chunked Requests \n"
    menu += ".netrc Support \n"
    print(menu)

def basic_http(get_url):
   
    try: 
        
        #url_handle = requests.request('GET', get_url)
        url_handle = requests.get(get_url)
        #url_handle = requests.get(get_url, stream=True)
        print('request Status: {0}'.format(url_handle.status_code), end='\n')
        print('Headers included: {0}'.format(url_handle.headers['Content-encoding']), end='\n')
        print('Encoding set to: {0}'.format(url_handle.encoding), end='\n')
        #print('Content Length (Bytes): {0}'.format(url_handle.content))
        #print('Text: {0}'.format(url_handle.text))
        #print('Raw Output: {0}'.format(url_handle.raw.read(10)))
        print('\nLets examine what headers are defined in this address', end='\n\n')
        for item in url_handle.headers:
            print('{0}::\t is set to {1} '.format(item, url_handle.headers.get(item)), end='\n')
            
        print('\nLets examine response content', end='\n\n')
        print(url_handle.text)
        
        
        
        #print('type: {0} '.format(read))
    except requests.JSONDecodeError as err:
        print('Msg: {0}'.format(err.msg))
       
       

if __name__ == "__main__":
    
    url1 = "https://rate.sx"
    url2 = 'https://rates.sx/xrp@1h'
    
    #while True:
    #time.sleep(1)
    try:
        basic_http(url1)
        basic_http(url2)
            
            
    except KeyboardInterrupt:
        sys.exit(0)

