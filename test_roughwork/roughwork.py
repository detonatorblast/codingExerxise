import numpy as np

def fizzbuzz(n):
    if str(n).isalpha():
        raise TypeError

    np_arr = np.arange(1, n+1)
    print np_arr
    print np_arr[(np_arr % 15) == 0]

fizzbuzz(15)



# import requests
#
#
# streetstr = "9324 WINDY MEADOW LN"
# street = '+'.join(streetstr.split(' '))
#
# statestr = "+CORDOVA," + "+TN," + "+38016"
#
# inputaddr = street + "," + statestr
#
# baseurl = "https://www.google.com/maps/place/"
# querystr = baseurl + inputaddr
# print requests.get(url=querystr)
# # print responsebuf

