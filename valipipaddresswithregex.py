from re import compile, match

ipv4num = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))'
ipv4exp = compile(r'^'+r'\.'.join([ipv4num]*4)+r'$')

ipv6num = r'[0-9A-Fa-f]{1,4}'
ipv6exp = compile(r'^'+r':'.join([ipv6num]*8)+r'$')

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ipv4exp.match(IP):
            return 'IPv4'
        if ipv6exp.match(IP):
            return 'IPv6'
        return 'Neither'
