import socket

def get(path):
    s = socket.socket()
    s.connect(('localhost',8000))

    request = 'GET %s HTTP/1.1\r\n\r\n' % path

    s.send((request.encode()))

    chunks = []
    while True:
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            return

get('/foo')



