import socket

HOST = "127.0.0.1"
PORT = 25

# Establish a TCP connection with the mail server.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    response = s.recv(1024).decode('utf-8')

    # read greeting from the server
    if not response.startswith('220'):
        raise Exception('220 reply not received from server.')

    # send HELO command and get server response
    cmd_HELO = 'HELO alice\r\n'
    s.sendall(cmd_HELO.encode())
    response = s.recv(1024).decode('utf-8')
    if not response.startswith('250'):
        raise Exception('250 reply not received from server.')

    # send MAIL FROM command
    cmd_MAIL_FROM = 'MAIL FROM: <alice@crepes.fr>\r\n'
    s.sendall(cmd_MAIL_FROM.encode())
    response = s.recv(1024).decode('utf-8')
    if not response.startswith('250'):
        raise Exception('250 reply not received from server.')

    # send RCPT TO command; send to <sys> which account on the VM
    cmd_RCPT_TO = 'RCPT TO: <sys>\r\n'
    s.sendall(cmd_RCPT_TO.encode())
    response = s.recv(1024).decode('utf-8')
    if not response.startswith('250'):
        raise Exception('250 reply not received from server.')

    # send DATA command
    cmd_DATA = 'DATA\r\n'
    s.sendall(cmd_DATA.encode())
    response = s.recv(1024).decode('utf-8')
    if not response.startswith('354'):
        raise Exception('354 reply not received from server.')

    # send message data, ending with line with a single period
    cmd_MSG = 'SUBJECT: hello\r\n'
    cmd_MSG += 'Hi Marques, How\'s the weather? Charlotte.\r\n'
    cmd_MSG += '.\r\n'
    s.sendall(cmd_MSG.encode())
    response = s.recv(1024).decode('utf-8')
    if not response.startswith('250'):
        raise Exception('250 reply not received from server.')

    # send QUIT command
    cmd_QUIT = 'QUIT\r\n'
    s.sendall(cmd_QUIT.encode())





