from netifaces import  interfaces,ifaddresses,AF_INET,AF_INET6

import platform


def get_ip_address(ifname):
    if platform.system() == 'Linux':
        try:
            return ifaddresses(ifname)[AF_INET][0]['addr']
        except ValueError:
            return None
    elif platform.system() == 'Windows':
        from win_ifname import get_connection_name_from_guid
        if_id = get_connection_name_from_guid(ifname)
        if not if_id:
            return
        else:
            return ifaddresses(if_id)[AF_INET][0]['addr']
    else:
        print('操作系统不支持，本脚本只能工作在Windows或者Linux环境')
def get_ipv6_address(ifname):
    if platform.system() == 'Linux':
        try:
            return ifaddresses(ifname)[AF_INET6][0]['addr']
        except ValueError:
            return None
    elif platform.system() == 'Windows':
        from win_ifname import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        if not if_id:
            return
        else:
            return ifaddresses(if_id)[AF_INET6][0]['addr']

    else:
        print('操作系统不支持，本脚本只能工作在Windows或者Linux环境')

if __name__ == '__main__':
    if platform.system() == 'Linux':
        print(get_ip_address('ens33'))
        print(get_ipv6_address('ens33'))
    elif platform.system() == 'Windows':
        print(get_ip_address('Net1'))
        print(get_ipv6_address('Net1'))