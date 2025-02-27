from openpyxl import Workbook
from openpyxl.styles import Alignment
import ccxt
import time
import datetime

unesminutesdebut =3
troisminutesdebut = 3  
unesminutesdebut = 3
cinqsminutesdebut = 3
quinsesminutesdebut = 3
trenteminutesdebut = 3
uneheuredebut = 3
deuxheuresdebut = 3
quatreheuresdebut = 3
sixheuresdebut = 3
huitheuresdebut = 3
douzeheuresdebut = 3
unedjoudebut = 3
troisjousdebut = 3
unesemaine = 3

lancements = {
    "lancement3minutes": 0,
    "lancement5minutes": 0,
    "lancement15minutes": 0,
    "lancement30minutes": 0,
    "lancement1h": 0,
    "lancement2h": 0,
    "lancement4h": 0,
    "lancement6h": 0,
    "lancement8h": 0,
    "lancement12h": 0,
    "lancement1jour": 0,
    "lancement3jour": 0,
    "lancement1semaine": 0,
    "total": 0
}

timeframes = {
    "1m": "1m",    
    "3m": "3m",     
    "5m": "5m",     
    "15m": "15m",   
    "30m": "30m",   
    "1h": "1h",     
    "2h": "2h",     
    "4h": "4h",     
    "6h": "6h",     
    "8h": "8h",     
    "12h": "12h",   
    "1d": "1d",     
    "3d": "3d",     
    "1w": "1w",     
}

wb = Workbook()
sheet = wb.active


alignment = Alignment(horizontal='center', vertical='center')


row = 1  
debutlongueur = 1  
longueur = 6  


for i, (timeframe, value) in enumerate(timeframes.items()):
    
    sheet.merge_cells(start_row=row, start_column=debutlongueur, end_row=row, end_column=longueur)
    
    
    cell = sheet.cell(row=row, column=debutlongueur, value=f"Time Frame : {timeframe}")
    cell.alignment = alignment 
    
   
    sheet.cell(row=row + 1, column=debutlongueur, value="timestamp").alignment = alignment
    sheet.cell(row=row + 1, column=debutlongueur + 1, value="Open").alignment = alignment
    sheet.cell(row=row + 1, column=debutlongueur + 2, value="High").alignment = alignment
    sheet.cell(row=row + 1, column=debutlongueur + 3, value="Low").alignment = alignment
    sheet.cell(row=row + 1, column=debutlongueur + 4, value="Close").alignment = alignment
    sheet.cell(row=row + 1, column=debutlongueur + 5, value="volume").alignment = alignment

    
    debutlongueur = longueur + 1
    longueur = longueur + 6
def times1minutes(timeframe):
    
    global unesminutesdebut
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'


    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)

    
    last_candle = ohlcv_data[-1]

    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]

    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


    
    sheet.cell(row=unesminutesdebut, column=1, value=timestamp).alignment = alignment
    sheet.cell(row=unesminutesdebut, column=2, value=open_price).alignment = alignment
    sheet.cell(row=unesminutesdebut, column=3, value=high_price).alignment = alignment
    sheet.cell(row=unesminutesdebut, column=4, value=low_price).alignment = alignment
    sheet.cell(row=unesminutesdebut, column=5, value=close_price).alignment = alignment
    sheet.cell(row=unesminutesdebut, column=6, value=volume).alignment = alignment

    
    unesminutesdebut += 1
    for key in lancements:
        lancements[key] += 1  

    return unesminutesdebut
    

def times3minutes(timeframe):
    
    global troisminutesdebut
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=troisminutesdebut, column=7, value=timestamp).alignment = alignment
    sheet.cell(row=troisminutesdebut, column=8, value=open_price).alignment = alignment
    sheet.cell(row=troisminutesdebut, column=9, value=high_price).alignment = alignment
    sheet.cell(row=troisminutesdebut, column=10, value=low_price).alignment = alignment
    sheet.cell(row=troisminutesdebut, column=11, value=close_price).alignment = alignment
    sheet.cell(row=troisminutesdebut, column=12, value=volume).alignment = alignment
    
    
    troisminutesdebut += 1


def times5minutes(timeframe):
    
    global cinqsminutesdebut
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=cinqsminutesdebut, column=13, value=timestamp).alignment = alignment
    sheet.cell(row=cinqsminutesdebut, column=14, value=open_price).alignment = alignment
    sheet.cell(row=cinqsminutesdebut, column=15, value=high_price).alignment = alignment
    sheet.cell(row=cinqsminutesdebut, column=16, value=low_price).alignment = alignment
    sheet.cell(row=cinqsminutesdebut, column=17, value=close_price).alignment = alignment
    sheet.cell(row=cinqsminutesdebut, column=18, value=volume).alignment = alignment
    
    
    cinqsminutesdebut += 1

def times15minutes(timeframe):
    global quinsesminutesdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=quinsesminutesdebut, column=19, value=timestamp).alignment = alignment
    sheet.cell(row=quinsesminutesdebut, column=20, value=open_price).alignment = alignment
    sheet.cell(row=quinsesminutesdebut, column=21, value=high_price).alignment = alignment
    sheet.cell(row=quinsesminutesdebut, column=22, value=low_price).alignment = alignment
    sheet.cell(row=quinsesminutesdebut, column=23, value=close_price).alignment = alignment
    sheet.cell(row=quinsesminutesdebut, column=24, value=volume).alignment = alignment
    
    
    quinsesminutesdebut += 1

def times30minutes(timeframe):
    global trenteminutesdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


    
    sheet.cell(row=trenteminutesdebut, column=25, value=timestamp).alignment = alignment
    sheet.cell(row=trenteminutesdebut, column=26, value=open_price).alignment = alignment
    sheet.cell(row=trenteminutesdebut, column=27, value=high_price).alignment = alignment
    sheet.cell(row=trenteminutesdebut, column=28, value=low_price).alignment = alignment
    sheet.cell(row=trenteminutesdebut, column=29, value=close_price).alignment = alignment
    sheet.cell(row=trenteminutesdebut, column=30, value=volume).alignment = alignment
    
    
    trenteminutesdebut += 1


def times1hour(timeframe):
    global uneheuredebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


    
    sheet.cell(row=uneheuredebut, column=31, value=timestamp).alignment = alignment
    sheet.cell(row=uneheuredebut, column=32, value=open_price).alignment = alignment
    sheet.cell(row=uneheuredebut, column=33, value=high_price).alignment = alignment
    sheet.cell(row=uneheuredebut, column=34, value=low_price).alignment = alignment
    sheet.cell(row=uneheuredebut, column=35, value=close_price).alignment = alignment
    sheet.cell(row=uneheuredebut, column=36, value=volume).alignment = alignment
    
    
    uneheuredebut += 1


def times2hours(timeframe):
    global deuxheuresdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=deuxheuresdebut, column=37, value=timestamp).alignment = alignment
    sheet.cell(row=deuxheuresdebut, column=38, value=open_price).alignment = alignment
    sheet.cell(row=deuxheuresdebut, column=39, value=high_price).alignment = alignment
    sheet.cell(row=deuxheuresdebut, column=40, value=low_price).alignment = alignment
    sheet.cell(row=deuxheuresdebut, column=41, value=close_price).alignment = alignment
    sheet.cell(row=deuxheuresdebut, column=42, value=volume).alignment = alignment
    
    
    deuxheuresdebut += 1


def times4hours(timeframe):
    global quatreheuresdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=quatreheuresdebut, column=43, value=timestamp).alignment = alignment
    sheet.cell(row=quatreheuresdebut, column=44, value=open_price).alignment = alignment
    sheet.cell(row=quatreheuresdebut, column=45, value=high_price).alignment = alignment
    sheet.cell(row=quatreheuresdebut, column=46, value=low_price).alignment = alignment
    sheet.cell(row=quatreheuresdebut, column=47, value=close_price).alignment = alignment
    sheet.cell(row=quatreheuresdebut, column=48, value=volume).alignment = alignment
    
    
    quatreheuresdebut += 1


def times6hours(timeframe):
    global sixheuresdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=sixheuresdebut, column=49, value=timestamp).alignment = alignment
    sheet.cell(row=sixheuresdebut, column=50, value=open_price).alignment = alignment
    sheet.cell(row=sixheuresdebut, column=51, value=high_price).alignment = alignment
    sheet.cell(row=sixheuresdebut, column=52, value=low_price).alignment = alignment
    sheet.cell(row=sixheuresdebut, column=53, value=close_price).alignment = alignment
    sheet.cell(row=sixheuresdebut, column=54, value=volume).alignment = alignment
    
    
    sixheuresdebut += 1


def times8hours(timeframe):
    global huitheuresdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=huitheuresdebut, column=55, value=timestamp).alignment = alignment
    sheet.cell(row=huitheuresdebut, column=56, value=open_price).alignment = alignment
    sheet.cell(row=huitheuresdebut, column=57, value=high_price).alignment = alignment
    sheet.cell(row=huitheuresdebut, column=58, value=low_price).alignment = alignment
    sheet.cell(row=huitheuresdebut, column=59, value=close_price).alignment = alignment
    sheet.cell(row=huitheuresdebut, column=60, value=volume).alignment = alignment
    
    
    huitheuresdebut += 1


def times12hours(timeframe):
    global douzeheuresdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    
    
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    
    last_candle = ohlcv_data[-1]
    
    
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    
    sheet.cell(row=douzeheuresdebut, column=61, value=timestamp).alignment = alignment
    sheet.cell(row=douzeheuresdebut, column=62, value=open_price).alignment = alignment
    sheet.cell(row=douzeheuresdebut, column=63, value=high_price).alignment = alignment
    sheet.cell(row=douzeheuresdebut, column=64, value=low_price).alignment = alignment
    sheet.cell(row=douzeheuresdebut, column=65, value=close_price).alignment = alignment
    sheet.cell(row=douzeheuresdebut, column=66, value=volume).alignment = alignment
    
    
    douzeheuresdebut += 1
    


def times1day(timeframe):
    global unjourdebut
    
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    

    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    

    last_candle = ohlcv_data[-1]
    

    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

    sheet.cell(row=unjourdebut, column=67, value=timestamp).alignment = alignment
    sheet.cell(row=unjourdebut, column=68, value=open_price).alignment = alignment
    sheet.cell(row=unjourdebut, column=69, value=high_price).alignment = alignment
    sheet.cell(row=unjourdebut, column=70, value=low_price).alignment = alignment
    sheet.cell(row=unjourdebut, column=71, value=close_price).alignment = alignment
    sheet.cell(row=unjourdebut, column=72, value=volume).alignment = alignment
    unjourdebut += 1


def times3days(timeframe):
    global times3days

    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    

    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    
    last_candle = ohlcv_data[-1]
    

    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


    sheet.cell(row=troistrainesdebut, column=73, value=timestamp).alignment = alignment
    sheet.cell(row=troistrainesdebut, column=74, value=open_price).alignment = alignment
    sheet.cell(row=troistrainesdebut, column=75, value=high_price).alignment = alignment
    sheet.cell(row=troistrainesdebut, column=76, value=low_price).alignment = alignment
    sheet.cell(row=troistrainesdebut, column=77, value=close_price).alignment = alignment
    sheet.cell(row=troistrainesdebut, column=78, value=volume).alignment = alignment
    
    troistrainesdebut += 1


def times1week(timeframe):
    global times1week
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    ohlcv_data = exchange.fetch_ohlcv(symbol, timeframe)
    last_candle = ohlcv_data[-1]
    timestamp= last_candle[0]
    open_price = last_candle[1]
    high_price = last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    volume = last_candle[5]
    timestamp = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
    sheet.cell(row=une_semaine_debut, column=79, value=timestamp).alignment = alignment
    sheet.cell(row=une_semaine_debut, column=80, value=open_price).alignment = alignment
    sheet.cell(row=une_semaine_debut, column=81, value=high_price).alignment = alignment
    sheet.cell(row=une_semaine_debut, column=82, value=low_price).alignment = alignment
    sheet.cell(row=une_semaine_debut, column=83, value=close_price).alignment = alignment
    sheet.cell(row=une_semaine_debut, column=84, value=volume).alignment = alignment
    une_semaine_debut += 1
    

def appel_fonction() :
    current_time = datetime.datetime.now()
    print(f"démarage du programme à, {current_time.hour}h, {current_time.minute}m, {current_time.second}s")
    while True:
        print(f"temps total ecouler {lancements["total"]}minute")
        times1minutes("1m")
        wb.save("DATA_crypto.xlsx")
        time.sleep(60)
        if lancements["lancement3minutes"] == 3:
            times3minutes("3m")
            lancements["lancement3minutes"] = 0
        if lancements["lancement5minutes"] == 5:
            times5minutes("5m")
            lancements["lancement5minutes"] = 0
        if lancements["lancement15minutes"] == 15:
            times15minutes("15m")
            lancements["lancement15minutes"] = 0
        if lancements["lancement30minutes"] == 30:
            times30minutes("30m")
            lancements["lancement30minutes"] = 0
        if lancements["lancement1h"] == 60:
            times1hour("1h")
            lancements["lancement1h"] = 0
        if lancements["lancement2h"] == 120:
            times2hours("2h")
            lancements["lancement2h"] = 0
        if lancements["lancement4h"] == 240:
            times4hours("4h")
            lancements["lancement4h"] = 0
        if lancements["lancement6h"] == 360:
            times6hours("6h")
            lancements["lancement6h"] = 0
        if lancements["lancement8h"] == 480:
            times8hours("8h")
            lancements["lancement8h"] = 0
        if lancements["lancement12h"] == 720:
            times12hours("12h")
            lancements["lancement12h"] = 0
        if lancements["lancement1jour"] == 1440:
            times1day("1d")
            lancements["lancement1jour"] = 0
        if lancements["lancement3jour"] == 4320 :
            times3days("3d")
            lancements["lancement3jour"] = 0
        if lancements["lancement1semaine"] == 10080:
            times1week("1w")
            lancements["lancement1semaine"] = 0

    
appel_fonction()
