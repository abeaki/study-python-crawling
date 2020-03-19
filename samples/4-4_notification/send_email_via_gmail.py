import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText('メールの本文です。')  # MIMETextオブジェクトでメッセージを組み立てる。
msg['Subject'] = Header('メールの件名', 'utf-8')  # 件名に日本語を含める場合はHeaderオブジェクトを使う。
msg['From'] = 'me@example.com'  # 差出人のメールアドレス
msg['To'] = 'you@example.com'  # 送信先のメールアドレス

with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    # Googleアカウントのユーザー名とパスワードを指定してログインする。
    # 2段階認証を設定している場合は、アプリパスワードを生成して使用する。
    smtp.login('ユーザー名', 'パスワード')
    smtp.send_message(msg)  # send_message()メソッドでメールを送信する。
