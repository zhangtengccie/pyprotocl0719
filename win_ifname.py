import netifaces as ni


def get_connection_name_from_guid(iface_guids):
    wr = __import__('winreg', globals(), locals(), ['wr'])
    iface_dict = {}
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    print(reg)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{07374750-E68B-490E-9330-9FD785CD71B6}')
    print(reg_key)
    for i in iface_guids:
        try:
            reg_subkey = wr.OpenKey(reg_key, i + r'\Connection')
            iface_dict[wr.QueryValueEx(reg_subkey, 'Name')[0]] = i
        except FileNotFoundError:
            pass

    return iface_dict


def win_from_name_id(ifname):
    x = ni.interfaces()
    return get_connection_name_from_guid(x).get(ifname)


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        print(win_from_name_id('Net1'))
