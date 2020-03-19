from urllib.robotparser import RobotFileParser

rp = RobotFileParser('http://gihyo.jp/robots.txt')
rp.read()
print(rp.can_fetch('mybot', 'http://gihyo.jp/'))
