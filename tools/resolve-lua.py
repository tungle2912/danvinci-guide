#!/usr/bin/env python3
import json, subprocess, sys

NODE = "/Users/mac/.nvm/versions/node/v24.19.0/bin/node"
SERVER = "/Users/mac/Workspace/davinci-resolve-lua-mcp/server/index.js"


def call(tool, args):
    p = subprocess.Popen([NODE, SERVER], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL, text=True)

    def send(msg):
        p.stdin.write(json.dumps(msg) + "\n")
        p.stdin.flush()

    def recv(want_id):
        for line in p.stdout:
            msg = json.loads(line)
            if msg.get("id") == want_id:
                return msg

    send({"jsonrpc": "2.0", "id": 1, "method": "initialize",
          "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                     "clientInfo": {"name": "rl", "version": "1"}}})
    recv(1)
    send({"jsonrpc": "2.0", "method": "notifications/initialized"})
    send({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
          "params": {"name": tool, "arguments": args}})
    res = recv(2)
    p.stdin.close()
    p.terminate()
    r = res.get("result", res)
    out = r.get("structuredContent") or r
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tool":
        call(sys.argv[2], json.loads(sys.argv[3]) if len(sys.argv) > 3 else {})
    else:
        code = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
        call("run_lua", {"code": code, "timeout_s": 60})
