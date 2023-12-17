from multiprocessing import Pool
import sys

from requests import get

TITLE = """
 ____       _        _      _    _        ____                               _____         _  
|  _ \ __ _| |_ _ __(_) ___| | _( )___   / ___|___  _   _ _ __   ___  _ __  |_   _|__  ___| |_ ___ _ __ 
| |_) / _` | __| '__| |/ __| |/ /// __| | |   / _ \| | | | '_ \ / _ \| '_ \   | |/ _ \/ __| __/ _ \ '__|
|  __/ (_| | |_| |  | | (__|   <  \__ \ | |__| (_) | |_| | |_) | (_) | | | |  | |  __/\__ \ ||  __/ |   
|_|   \__,_|\__|_|  |_|\___|_|\_\ |___/  \____\___/ \__,_| .__/ \___/|_| |_|  |_|\___||___/\__\___|_|

"""

EC2_DATACENTER = "eu-north-1.compute.amazonaws.com"
EC2_INSTANCE = ""

COUPON_SERVICE_PORT = "9091"
COUPON_API = "/couponapi/coupons/"

coupon = "BLACK_FRIDAY"


print(TITLE)


def send_requests(coupon):
    request_url = "http://" + EC2_INSTANCE + "." + EC2_DATACENTER + ":" + COUPON_SERVICE_PORT + COUPON_API + coupon
    print(f"Coupon URL: {request_url}")
    print('')

    response = get(request_url)
    data = response.json()
    print(f"Data Received: {data}")
    print('')
    i=0
    while True:
        try:
            response = get(request_url)
            data = response.json()
            i = i+1
            b = "   Number of responses received: " + str(i)
            print (b, end="\r")
        except KeyboardInterrupt:
            print('')
            print('Interrupted!')
            sys.exit(0)


send_requests(coupon)
