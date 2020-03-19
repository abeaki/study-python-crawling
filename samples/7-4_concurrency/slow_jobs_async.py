import asyncio


async def slow_job(n):
    """
    引数で指定した秒数だけ時間のかかる処理を非同期で行うコルーチン。
    asyncio.sleep()を使って擬似的に時間がかかるようにしている。
    """

    print('Job {0} will take {0} seconds'.format(n))
    await asyncio.sleep(n)  # n秒sleepする処理が終わるまで待つ
    print('Job {0} finished'.format(n))


# イベントループを取得。
loop = asyncio.get_event_loop()
# 3つのコルーチンを作成する。コルーチンはこの時点では実行されない。
coroutines = [slow_job(1), slow_job(2), slow_job(3)]
# イベントループで3つのコルーチンを実行し、終了するまで待つ。
loop.run_until_complete(asyncio.wait(coroutines))
