# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 09:31:27 2023

@author: Miraj
"""

import datetime as dt_module
import time, sys

time_delta = ['days=0', 'seconds=0', 'microseconds=0', 'milliseconds=0', 'minutes=0', 'hours=0', 'weeks=0' ]

namaz = ['fajr', 'zuhar', 'asr', 'maghrib', 'ishha' ]

ptimes = ['6:00', '12:30', '3:45', '5:12', '8:00']

prayer_dic = { n:t for (n,t) in zip(namaz, ptimes)}

pr_dict = { 'fajr': '0517AM', 'zuhar': '1220PM', 'asr': '0345PM', 'mghrib': '0512PM', 'ishha': '0730PM' }

def get_time():
    
    return dt_module.datetime.today().strftime('%I%M%p')
    
def time_delta():
    return dt_module.timedelta(seconds=20)
    
try:
    while True:
        
        now_time = dt_module.datetime.today().strftime('%I%M%p')
        #print('Type of current time: {0}'.format(type(curr_time)))
        for nam, ntime in pr_dict.items():
                print('before check time: {0}'.format(now_time))
                if ntime == now_time:
                    print('Its {0} time. '.format(nam))
                    sys.exit(0)
                else:
                    print('Waiting for Prayer time. \n')
        time.sleep(30)
                    
except KeyboardInterrupt:
    print('User Interrupt Detected: Exiting \n')
    sys.exit(0)
                
            
