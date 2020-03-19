import os
import signal

from rq import Queue


def requeue_job(job, *exc_info):
    print('Requeueing the job:', job)
    q = Queue(job.origin, connection=job.connection)  # ジョブの所属しているキューを取得
    q.enqueue_job(job, at_front=True)  # キューの先頭に再度ジョブを追加
    os.kill(os.getppid(), signal.SIGTERM)  # 親プロセスにSIGTERMを送信し、ワーカーをシャットダウンする。
    return False  # エラーハンドリングを終了する
