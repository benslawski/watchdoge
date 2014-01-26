from httplib import *
from datetime import *
from time import sleep


##WRITE_PATH = '/mnt/historic_prices/'
WRITE_PATH = 'test/'

def LogPrices():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')

    conn = None
    while True:
        print 'here'
        if conn:
            conn.close()
            sleep(1)

        try:
            conn = HTTPConnection("pubapi.cryptsy.com")
            conn.request("GET", "/api.php?method=marketdatav2")
        except Exception as e:
            print 'error connecting to API:', type(e), e
            continue

        try:
            results = conn.getresponse()
            if results.status != 200:
                print results
                continue
            price_data = results.read()
        except Exception as e:
            print 'error reading response:', type(e), e
            continue

        conn.close()
        break

    f = open(WRITE_PATH + timestamp + '_prices.json', 'w')
    f.write(price_data)
    f.close()


if __name__ == "__main__":
    LogPrices()
