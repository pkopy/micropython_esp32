import test
# import ubinascii

req = b'POST /test HTTP/1.1\r\nHost: 10.10.1.71\r\nConnection: keep-alive\r\nContent-Length: 45\r\nCache-Control: max-age=0\r\nOrigin: http://10.10.1.71\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nReferer: http://10.10.1.71/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\nlastname=Mouse&lastVname=CYC&firstname=OOOOO'


networks = [(b'swd', b'\xc0J\x00=\xd5\xc6', 6, -61, 2, False), (b'ScalesHotSpot WTC 135000', b'\xb4\xe6-\xb1J\x12', 1, -64, 0, False), (b'ScalesHotSpot C315 123000', b'\xb4\xe6-\xb1I\x16', 1, -64, 0, False), (b'RADWAG', b'z\x8a \x8d\xa0\xe7', 1, -67, 4, False), (b'INTERNET', b'x\x8a \x8d\xa0\xe7', 1, -70, 4, False), (b'RADWAG_PRODUKCJA', b'\x8a\x8a \x8d\xa0\xe7', 1, -73, 3, False), (b'RADWAG', b'z\x8a \x8d\x8d\xef', 11, -78, 4, False), (b'RADWAG_PRODUKCJA', b'\x8a\x8a \x8d\x8d\xef', 11, -78, 3, False), (b'INTERNET', b'x\x8a \x8d\x8d\xef', 11, -79, 4, False), (b'ScalesHotSpot WTC 100000', b'\xb4\xe6-\x97\xe4\xee', 5, -88, 0, False), (b'Radwaghot', b'df\xb3^\xb7\xb4', 6, -90, 3, False)]

# x = test.requestParse(req)
# a = x['body']

# for i in networks:
#     print(i[0].decode())
#     # print(ubinascii.hexlify(i[1]))
# if 'firstname' in x['body'].keys():
#     print(x['body'])
ddd = ''
url = '/favicon.dccc'
url = url[1:]
x = url[url.find('.'):]
# print(x)
# print(url.find('.'))
# print(url[url.find('.'):])

if '.' in url:
    ddd = url[url.find('.'):]

print(len(ddd))

if len(ddd) > 0:
    print('ok')
else
    print('do dupy')