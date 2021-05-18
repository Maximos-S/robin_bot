import config

import robin_stocks as rh
import datetime as dt
import time

def login(days):
    time_logged_in = 60*60*24*days
    rh.authentication.login(username=config.USERNAME,
                            password=config.PASSWORD,
                            expiresIn=time_logged_in,
                            scope='internal',
                            by_sms=True,
                            store_session=True)

def logout():
    rh.authentication.logout()

def get_stocks():
    stocks = list()
    stocks.append('INPX')
    stocks.append('HHT')
    stocks.append('CNET')
    return(stocks)

def open_market():
    market = True
    time_now = dt.datetime.now().time()
    
    market_open = dt.time(9,30,0) # 9:30AM
    market_close = dt.time(15,59,0) # 3:59PM

    if time_now > market_open and time_now < market_close:
        market = True
    else:
        print('### market is closed')

    return(market)

if __name__ == "__main__":
    print('im right here')
    # login(days=1)

    stocks = get_stocks()
    print('stocks', stocks)

    while open_market():
        print('lets make some money')
        prices = rh.stocks.get_latest_price(stocks)