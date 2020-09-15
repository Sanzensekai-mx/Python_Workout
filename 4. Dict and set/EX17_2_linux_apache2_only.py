#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
HTTP_STATUS_CODE = {'100': 'Continue', '101': 'Switching Protocols', '102': 'Processing', '103': 'Early Hints',
                    '200': 'OK', '201': 'Created',
                    '202': 'Accepted', '203': 'Non-authoritative Information', '204': 'No Content',
                    '205': 'Reset Content', '206': 'Partial Content', '207': 'Multi-Status',
                    '208': 'Already Reported', '226': 'IM Used', '300': 'Multiple Choices', '301': 'Moved Permanently',
                    '302': 'Moved Temporarily / Found', '303': 'See Other',
                    '304': 'Not Modified', '305': 'Use Proxy', '306': 'none', '307': 'Temporary Redirect',
                    '308': 'Permanent Redirect', '400': 'Bad Requests', '401': 'Unauthorized',
                    '402': 'Payment Required', '403': 'Forbidden', '404': 'Not Found', '405': 'Method Not Allowed',
                    '406': 'Not Acceptable', '407': 'Proxy Authentication Required',
                    '408': 'Request Timeout', '409': 'Conflict', '410': 'Gone', '411': 'Length Required',
                    '412': 'Precondition Failed', '413': 'Payload Too Large', '414': 'URI Too Long',
                    '415': 'Unsupported Media Type',
                    '416': 'Range Not Satisfiable', '417': 'Expectation Failed', '418': "I'm a teapot",
                    '419': 'Authentication Timeout (not in RFC 2616)', '421': 'Misdirected Request',
                    '422': 'Unprocessable Entity', '423': 'Locked', '424': 'Failed Dependency', '425': 'Too Early',
                    '426': 'Upgrade Required', '428': 'Precondition Required',
                    '429': 'Too Many Requests', '431': 'Request Header Fields Too Large', '449': 'Retry With',
                    '451': 'Unavailable For Legal Reasons', '499': 'Client Closed Request',
                    '500': 'Internal Server Error', '501': 'Not Implemented', '502': 'Bad Gateway',
                    '503': 'Service Unavailable', '504': 'Gateway Timeout', '505': 'HTTP Version Not Supported',
                    '506': 'Variant Also Negotiates',
                    '507': 'Insufficient Storage', '508': 'Loop Detected', '509': 'Bandwidth Limit Exceeded',
                    '510': 'Not Extended', '511': 'Network Authentication Required',
                    '520': 'Unknown Error', '521': 'Web Server Is Down', '522': 'Connection Timed Out',
                    '523': 'Origin Is Unreachable', '524': 'A Timeout Occurred', '525': 'SSL Handshake Failed',
                    '526': 'Invalid SSL Certificate'}


pattern_ip = re.compile(r'[\d]{2,3}\.[\d]{1,3}\.[\d]{1,4}\.[\d]{1,3}')
pattern_mes = re.compile(r'\s[1-5]{1}\d{2}\s')

all_ip = []
all_mes = []
with open('/var/log/apache2/access.log', 'r') as log:
    for line in log:
        ip = re.match(pattern_ip, line)
        message = re.search(pattern_mes, line)
        all_ip.append(ip.group())
        all_mes.append(message.group().strip())

for ip_i, mes_i in zip(all_ip, all_mes):
    print(f'{ip_i} --> {mes_i} - {HTTP_STATUS_CODE[mes_i]}')
