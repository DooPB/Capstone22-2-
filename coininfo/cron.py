from apscheduler.schedulers.background import BackgroundScheduler
import websockets
import asyncio
import json
import pandas as pd

def job():
    async def upbit_websocket_ETH():
        upbit_url = 'wss://api.upbit.com/websocket/v1'

        async with websockets.connect(upbit_url, ping_interval=60) as ws:
            upbit_sub_ETH = [

                {'ticket': 'test'},
                {
                    'type': 'ticker',
                    'codes': ['KRW-ETH'],
                    'isOnlyRealtime': True,
                },
                {'format': 'SIMPLE'}
            ]
            subscribe_date = json.dumps(upbit_sub_ETH)
            await ws.send(subscribe_date)

            while True:
                data = await ws.recv()
                data_ETH = json.loads(data)
                print(data_ETH)
                df = pd.DataFrame.from_dict([data_ETH])
                print(df)
                df.to_csv("c:/projects/mysite/static/ETH.csv", index=False, columns=['cd', 'tp', 'scr', 'tv'])

    async def upbit_websocket_BTC():
        upbit_url = 'wss://api.upbit.com/websocket/v1'

        async with websockets.connect(upbit_url, ping_interval=60) as ws:
            upbit_sub_BTC = [

                {'ticket': 'test'},
                {
                    'type': 'ticker',
                    'codes': ['KRW-BTC'],
                    'isOnlyRealtime': True,
                },
                {'format': 'SIMPLE'}
            ]
            subscribe_date = json.dumps(upbit_sub_BTC)
            await ws.send(subscribe_date)

            while True:
                data = await ws.recv()
                data_BTC = json.loads(data)
                print(data_BTC)
                df = pd.DataFrame.from_dict([data_BTC])
                print(df)
                df.to_csv("c:/projects/mysite/static/BTC.csv", index=False, columns=['cd', 'tp', 'scr', 'tv'])

    async def upbit_websocket_XRP():
        upbit_url = 'wss://api.upbit.com/websocket/v1'

        async with websockets.connect(upbit_url, ping_interval=60) as ws:
            upbit_sub_XRP = [

                {'ticket': 'test'},
                {
                    'type': 'ticker',
                    'codes': ['KRW-ETH'],
                    'isOnlyRealtime': True,
                },
                {'format': 'SIMPLE'}
            ]
            subscribe_date = json.dumps(upbit_sub_XRP)
            await ws.send(subscribe_date)

            while True:
                data = await ws.recv()
                data_XRP = json.loads(data)
                print(data_XRP)
                df = pd.DataFrame.from_dict([data_XRP])
                print(df)
                df.to_csv("c:/projects/mysite/static/XRP.csv", index=False, columns=['cd', 'tp', 'scr', 'tv'])

    async def main():
        coin1 = upbit_websocket_ETH()
        coin2 = upbit_websocket_BTC()
        coin3 = upbit_websocket_XRP()
        await asyncio.gather(
            coin1,
            coin2,
            coin3
        )

    asyncio.run(main())

def main():
    sched = BackgroundScheduler()
    sched.add_job(job,'interval', seconds=3, id='test')
    sched.start()
