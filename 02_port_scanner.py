import socket

def scan(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f'[OPEN]\t\t {port}')
    except:
        print(f'[CLOSED]\t {port}')

target = input('Target IP/Domain: ')
ports = input('Target Port: ')

print('\nSTATUS\t\t PORT')

# 80,81,82
# 80-85
# 80 | 90

if ',' in ports:
    list_port = ports.split(',')
    for port in list_port:
        scan(target, int(port))
elif '-' in ports:
    port_range = ports.split('-')
    start = int(port_range[0])
    end = int(port_range[1]) + 1
    for port in range(start, end):
        scan(target, port)
else:
    scan(target, int(ports))
