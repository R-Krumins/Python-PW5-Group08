import socket

max_characters = 1800
char_count = 0

try:
    url = input("Enter URL: ")
    parts = url.split('/')
    host_name = parts[2]
    print("Host Name:", host_name)
    print('')
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'
    mysock.send(cmd.encode())
except Exception as e:
    print("Error occurred:", e)

while True:
    data = mysock.recv(512)
    if (len(data) < 1 or char_count >= max_characters):
        break
    print(data.decode(),end='')
    char_count += len(data)

print('')
print('Character count: ', char_count)
mysock.close()