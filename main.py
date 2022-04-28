from utils import *
import time
import requests
import urllib3

urllib3.disable_warnings()

def main():
    while True:
        duration = (config.CHECK_EVERY * 60)
        time.sleep(duration)
        request = requests.get(config.URL, verify=False)
        if (request.status_code != 200):
            send_down_email(request.status_code)
            check_status()                            

main()
        

