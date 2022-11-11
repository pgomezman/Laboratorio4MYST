import ccxt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from datetime import date
from datetime import datetime, timedelta
import MetaTrader5 as mt5
import calendar
import matplotlib.pyplot as plt


def diccionario(tiempo):
    y={}
    yy={}
    yyy={}
    z = {}

    # Repetitivo

    now0 = datetime.now()
    time_passed=datetime.now() - now0

    while time_passed.seconds <=tiempo:
        
    #BINANCE
        binance = ccxt.binance()
        time_passed=datetime.now() - now0
        time_samp = binance.iso8601(binance.milliseconds())

        # Bitcoin
        bi_btc_ob = binance.fetch_order_book('BTC/USDT', limit=30)

        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='BTC/USDT',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'BTC/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        y[str(time_samp)]=x



        # Etherum
        bi_btc_ob= binance.fetch_order_book('ETH/USDT', limit=30)
        time_samp = binance.iso8601(binance.milliseconds())
        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='ETH/USDT',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'ETH/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        y[str(time_samp)]=x



        # Doge
        bi_btc_ob= binance.fetch_order_book('DOGE/USDT', limit=30)
        time_samp = binance.iso8601(binance.milliseconds())
        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='DOGE/USDT',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'DOGE/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        y[str(time_samp)]=x
        
        
    # BITSO
        binance = ccxt.bitfinex()
        time_samp = binance.iso8601(binance.milliseconds())

        # Bitcoin
        bi_btc_ob = binance.fetch_order_book('BTC/USD', limit=30)

        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='BTC/USD',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'BTC/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        yy[str(time_samp)]=x



        # Etherum
        bi_btc_ob= binance.fetch_order_book('ETH/USD', limit=30)
        time_samp = binance.iso8601(binance.milliseconds())
        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='ETH/USD',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'ETH/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        yy[str(time_samp)]=x



        # Doge
        bi_btc_ob= binance.fetch_order_book('DOGE/USD', limit=30)
        time_samp = binance.iso8601(binance.milliseconds())
        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='DOGE/USD',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'DOGE/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        yy[str(time_samp)]=x
        
        
        
    #BITMART
        binance = ccxt.bitmart()
        time_passed=datetime.now() - now0
        time_samp = binance.iso8601(binance.milliseconds())

        # Bitcoin
        bi_btc_ob = binance.fetch_order_book('BTC/USDT', limit=30)

        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='BTC/USDT',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'BTC/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        yyy[str(time_samp)]=x



        # Etherum
        bi_btc_ob= binance.fetch_order_book('ETH/USDT', limit=30)
        time_samp = binance.iso8601(binance.milliseconds())
        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='ETH/USDT',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'ETH/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        yyy[str(time_samp)]=x



        # Doge
        bi_btc_ob= binance.fetch_order_book('DOGE/USDT', limit=30)
        time_samp = binance.iso8601(binance.milliseconds())
        # Ask and bid
        bi_btc_ob_ask = pd.DataFrame(bi_btc_ob['asks'], columns = ['price','quantity'])
        bi_btc_ob_bid = pd.DataFrame(bi_btc_ob['bids'], columns = ['price','quantity'])

        bid = bi_btc_ob['bids'][0][0] if len (bi_btc_ob['bids']) > 0 else None
        ask = bi_btc_ob['asks'][0][0] if len (bi_btc_ob['asks']) > 0 else None
        spread = (ask - bid) if (bid and ask) else None

        # OHLC
        OHLC=binance.fetch_ohlcv(symbol='DOGE/USDT',limit=1)

        #VWAP Calculation
        a=bi_btc_ob['bids']+bi_btc_ob['asks']
        aa=[row[0] for row in a]
        bb=[row[1] for row in a]
        VWAP=sum([a*b for a,b in zip(aa, bb)])/sum(bb)

        # dictionary entry
        x={'Coin': 'DOGE/USDT',
        'Ask': ask,
        'Bid':bid,
        'Ask_Volume':sum([row[1] for row in bi_btc_ob['bids']]),
        'Bid_Volume':sum([row[1] for row in bi_btc_ob['asks']]),
        'Level':len(bi_btc_ob['asks']),
        'Spread':spread,
        'Close_Price': OHLC[0][4],
        'Mid_Price': (OHLC[0][2]-OHLC[0][3])+OHLC[0][3],
        'VWAP': VWAP}

        yyy[str(time_samp)]=x
        
    z['Binance']=y
    z['Bitfinex']=yy
    z['Bitmart']=yyy

    return z


def dataframe(z):
    binance = (pd.DataFrame(z['Binance'])).transpose()
    binance.reset_index(inplace = True)
    binance.rename(columns={'index': 'TimeStamp'}, inplace=True)
    binance.insert(0, 'Exchange', 'Binance')

    bitfinex = (pd.DataFrame(z['Bitfinex'])).transpose()
    bitfinex.reset_index(inplace = True)
    bitfinex.rename(columns={'index': 'TimeStamp'}, inplace=True)
    bitfinex.insert(0, 'Exchange', 'Bitfinex')

    bitmart = (pd.DataFrame(z['Bitmart'])).transpose()
    bitmart.reset_index(inplace = True)
    bitmart.rename(columns={'index': 'TimeStamp'}, inplace=True)
    bitmart.insert(0, 'Exchange', 'Bitmart')

    df= pd.concat([binance, bitfinex, bitmart])

    df.insert(7, 'Total_volume', df['Ask_Volume']+df['Bid_Volume'])
    df.pop('Ask')
    df.pop('Bid')
    df.reset_index(inplace = True, drop = True)
    spread = df.pop('Spread')
    close_p = df.pop('Close_Price')

    return df

def dataframebin(z):
    binance = (pd.DataFrame(z['Binance'])).transpose()
    binance.reset_index(inplace = True)
    binance.rename(columns={'index': 'TimeStamp'}, inplace=True)
    binance.insert(0, 'Exchange', 'Binance')

    return binance
    

def dataframebit(z):

    bitmart = (pd.DataFrame(z['Bitmart'])).transpose()
    bitmart.reset_index(inplace = True)
    bitmart.rename(columns={'index': 'TimeStamp'}, inplace=True)
    bitmart.insert(0, 'Exchange', 'Bitmart')

    return bitmart

def dataframefinex(z):

    bitfinex = (pd.DataFrame(z['Bitfinex'])).transpose()
    bitfinex.reset_index(inplace = True)
    bitfinex.rename(columns={'index': 'TimeStamp'}, inplace=True)
    bitfinex.insert(0, 'Exchange', 'Bitfinex')

    return bitfinex


def binanceBTCcoin(binance):

    binance = binance.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    binance['diff'] = 0.0
    binance['Effective_Spread'] = 0.0

    binanceBTC = binance[binance['Coin'] == 'BTC/USDT']
    binanceBTC.reset_index(inplace = True, drop = True)


    return binanceBTC

def binanceETHcoin(binance):

    binance = binance.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    binance['diff'] = 0.0
    binance['Effective_Spread'] = 0.0

    binanceETH = binance[binance['Coin'] == 'ETH/USDT']
    binanceETH.reset_index(inplace = True, drop = True)

    return binanceETH

def binanceDOGEcoin(binance):

    binance = binance.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    binance['diff'] = 0.0
    binance['Effective_Spread'] = 0.0

    binanceDOGE = binance[binance['Coin'] == 'DOGE/USDT']
    binanceDOGE.reset_index(inplace = True, drop = True)

    return binanceDOGE

def bitfinexBTCcoin(bitfinex):
    bitfinex = bitfinex.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    bitfinex['diff'] = 0.0
    bitfinex['Effective_Spread'] = 0.0

    bitfinexBTC = bitfinex[bitfinex['Coin'] == 'BTC/USDT']
    bitfinexBTC.reset_index(inplace = True, drop = True)

    return bitfinexBTC

def bitfinexETHcoin(bitfinex):
    bitfinex = bitfinex.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    bitfinex['diff'] = 0.0
    bitfinex['Effective_Spread'] = 0.0

    bitfinexETH = bitfinex[bitfinex['Coin'] == 'ETH/USDT']
    bitfinexETH.reset_index(inplace = True, drop = True)

    return bitfinexETH

def bitfinexDOGEcoin(bitfinex):
    bitfinex = bitfinex.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    bitfinex['diff'] = 0.0
    bitfinex['Effective_Spread'] = 0.0

    bitfinexDOGE = bitfinex[bitfinex['Coin'] == 'DOGE/USDT']
    bitfinexDOGE.reset_index(inplace = True, drop = True)

    return bitfinexDOGE   


def bitmartBTCcoin(bitmart):

    bitmart = bitmart.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    bitmart['diff'] = 0.0
    bitmart['Effective_Spread'] = 0.0

    bitmartBTC = bitmart[bitmart['Coin'] == 'BTC/USDT']
    bitmartBTC.reset_index(inplace = True, drop = True)

    return bitmartBTC


def bitmartETHcoin(bitmart):

    bitmart = bitmart.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    bitmart['diff'] = 0.0
    bitmart['Effective_Spread'] = 0.0

    bitmartETH = bitmart[bitmart['Coin'] == 'ETH/USDT']
    bitmartETH.reset_index(inplace = True, drop = True)

    return bitmartETH

def bitmartDOGEcoin(bitmart):

    bitmart = bitmart.drop(['Ask','Bid','Ask_Volume','Bid_Volume','Level','VWAP'], axis = 1)
    bitmart['diff'] = 0.0
    bitmart['Effective_Spread'] = 0.0

    bitmartDOGE = bitmart[bitmart['Coin'] == 'DOGE/USDT']
    bitmartDOGE.reset_index(inplace = True, drop = True)

    return bitmartDOGE


def effective_spread(binanceBTC,binanceETH,binanceDOGE,bitfinexBTC,bitfinexETH,bitfinexDOGE,bitmartBTC,bitmartETH,bitmartDOGE):
    
    for i in range(len(binanceBTC)-1):
        binanceBTC['diff'][i+1] =  binanceBTC['Close_Price'][i+1] - binanceBTC['Close_Price'][i]
        binanceETH['diff'][i+1] =  binanceETH['Close_Price'][i+1] - binanceETH['Close_Price'][i]
        binanceDOGE['diff'][i+1] =  binanceDOGE['Close_Price'][i+1] - binanceDOGE['Close_Price'][i]
        
        bitfinexBTC['diff'][i+1] =  bitfinexBTC['Close_Price'][i+1] - bitfinexBTC['Close_Price'][i]
        bitfinexETH['diff'][i+1] =  bitfinexETH['Close_Price'][i+1] - bitfinexETH['Close_Price'][i]
        bitfinexDOGE['diff'][i+1] =  bitfinexDOGE['Close_Price'][i+1] - bitfinexDOGE['Close_Price'][i]
        
        bitmartBTC['diff'][i+1] =  bitmartBTC['Close_Price'][i+1] - bitmartBTC['Close_Price'][i]
        bitmartETH['diff'][i+1] =  bitmartETH['Close_Price'][i+1] - bitmartETH['Close_Price'][i]
        bitmartDOGE['diff'][i+1] =  bitmartDOGE['Close_Price'][i+1] - bitmartDOGE['Close_Price'][i]
        
        
    for i in range(len(binanceBTC)-5):
        binanceBTC['Effective_Spread'][i+1] = ((np.cov(binanceBTC['diff'][i:i+5]))**(1/2))*2
        
        bitfinexBTC['Effective_Spread'][i+1] = ((np.cov(bitfinexBTC['diff'][i:i+5]))**(1/2))*2
        
        bitmartBTC['Effective_Spread'][i+1] = ((np.cov(bitmartBTC['diff'][i:i+5]))**(1/2))*2
        
    df_complete = pd.concat([binanceBTC,binanceETH,binanceDOGE,bitfinexBTC,bitfinexETH,bitfinexDOGE,bitmartBTC,bitmartETH,bitmartDOGE])

    return df_complete