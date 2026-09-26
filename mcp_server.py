#!/usr/bin/env python3
"""
Zoth WebGen — Model Context Protocol (MCP) Server
Enables AI agents (Claude, Cursor, Hermes, Cline) to generate sovereign, zero-egress static web interfaces.
"""

import sys
import json
from pathlib import Path
from webgen_engine import TEMPLATES, generate_site, generate_master_artifacts

TOOLS = [
    {
        "name": "webgen_list_templates",
        "description": "List all available sovereign website templates and their architectural metadata.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "name": "webgen_generate_site",
        "description": "Generate a zero-egress, high-contrast dark/gold sovereign HTML website from a template.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "template": {
                    "type": "string",
                    "enum": list(TEMPLATES.keys()),
                    "description": "The template identifier to compile",
                },
                "output_path": {
                    "type": "string",
                    "description": "Destination file path (e.g., ./dist/index.html)",
                },
            },
            "required": ["template", "output_path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "webgen_generate_master_artifacts",
        "description": "Generate all 4 Master Artifacts (master-prompt.txt, master-instructions.sh, master-blueprint.json, llms.txt) for an archetype.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "template": {
                    "type": "string",
                    "enum": list(TEMPLATES.keys()),
                    "description": "The template identifier",
                },
                "framework": {
                    "type": "string",
                    "description": "Target framework (e.g. react-tailwind, astro, html, svelte)",
                },
                "theme": {
                    "type": "string",
                    "description": "Visual token theme (e.g. gold, cyberpunk, matrix)",
                },
                "output_dir": {
                    "type": "string",
                    "description": "Destination directory for master artifacts",
                },
            },
            "required": ["template", "output_dir"],
            "additionalProperties": False,
        },
    },
]

def handle_request(req: dict) -> dict:
    method = req.get("method")
    msg_id = req.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "zoth-webgen-mcp", "version": "1.1.0"},
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "ping":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {}}

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}

    if method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "webgen_list_templates":
            items = []
            for k, v in TEMPLATES.items():
                items.append({
                    "id": k,
                    "title": v.get("title"),
                    "description": v.get("description"),
                    "category": v.get("category", "SOVEREIGN")
                })
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {"content": [{"type": "text", "text": json.dumps(items, indent=2)}]},
            }

        if name == "webgen_generate_site":
            tpl = args.get("template", "saas-dashboard")
            out = args.get("output_path", "./dist/index.html")
            try:
                generate_site(tpl, out)
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(
                                    {"status": "success", "template": tpl, "output_path": out, "zero_egress": True}
                                ),
                            }
                        ]
                    },
                }
            except Exception as e:
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "isError": True,
                    "error": {"code": -32603, "message": str(e)},
                }

        if name == "webgen_generate_master_artifacts":
            tpl = args.get("template", "saas-dashboard")
            fw = args.get("framework", "react-tailwind")
            theme = args.get("theme", "gold")
            out_dir = args.get("output_dir", "./dist/artifacts")
            try:
                res = generate_master_artifacts(tpl, framework=fw, theme=theme, output_dir=out_dir)
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps(
                                    {"status": "success", "template": tpl, "artifacts": res, "zero_egress": True}
                                ),
                            }
                        ]
                    },
                }
            except Exception as e:
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "isError": True,
                    "error": {"code": -32603, "message": str(e)},
                }

        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "isError": True,
            "error": {"code": -32601, "message": f"Unknown tool: {name}"},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "isError": True,
        "error": {"code": -32601, "message": f"Unknown method: {method}"},
    }

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            if res:
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
