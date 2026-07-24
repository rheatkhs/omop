import urllib.request, urllib.parse
import base64

# Decode those session vars
sessions = {
    "3dvkqqdh100dbm9js2qgh2alg5": "bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGVtcHxiOjE7cmVxdWVzdF90b2tlbnxzOjMyOiJNSFVPcW4yQXBMT1NyVDBxNzRzMGluQWY0REVMcjluTiI7",
    "6r7sfqaukq6hl0dl78oeh4l7cs": "bGFuZ3VhZ2V8czo1OiJlbl9VUyI7dGVtcHxiOjE7cmVxdWVzdF90b2tlbnxzOjMyOiJIZkNZVVhYNWlUYWl5a0t0cUgxYlJzRFF6RG1OYXBHeCI7",
}

for sid, data in sessions.items():
    try:
        decoded = base64.b64decode(data).decode("utf-8", errors="replace")
        print(f"Session {sid}: {decoded}")
    except Exception as e:
        print(f"Error: {e}")

# Also try to get the session vars base64 decoded via the webshell
