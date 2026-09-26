import json
import subprocess
import sys
import tempfile
from pathlib import Path
import pytest

from webgen_engine import TEMPLATES, generate_site
from mcp_server import handle_request

def test_templates_catalog():
    assert "saas-dashboard" in TEMPLATES
    assert "cyberpunk-portfolio" in TEMPLATES
    for name, data in TEMPLATES.items():
        assert "html" in data
        assert "title" in data
        assert "<!DOCTYPE html>" in data["html"]
        # Sovereign theme token verification
        assert "#08080B" in data["html"] or "#050508" in data["html"]
        assert "#D4AF37" in data["html"] or "#00F0FF" in data["html"]

def test_generate_site():
    with tempfile.TemporaryDirectory() as tmpdir:
        out_file = Path(tmpdir) / "test_site" / "index.html"
        generate_site("saas-dashboard", str(out_file))
        assert out_file.exists()
        content = out_file.read_text(encoding="utf-8")
        assert "Sovereign SaaS Dashboard" in content
        assert "ZERO-EGRESS" in content

def test_cli_execution():
    with tempfile.TemporaryDirectory() as tmpdir:
        out_file = Path(tmpdir) / "cli_out.html"
        cmd = [sys.executable, "webgen_engine.py", "--template", "cyberpunk-portfolio", "--out", str(out_file)]
        res = subprocess.run(cmd, cwd=Path(__file__).parent.parent, capture_output=True, text=True)
        assert res.returncode == 0
        assert out_file.exists()
        content = out_file.read_text(encoding="utf-8")
        assert "Cyberpunk Portfolio" in content

def test_mcp_server_initialize():
    req = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
    res = handle_request(req)
    assert res["id"] == 1
    assert res["result"]["serverInfo"]["name"] == "zoth-webgen-mcp"

def test_mcp_server_tools_list():
    req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
    res = handle_request(req)
    assert res["id"] == 2
    tool_names = [t["name"] for t in res["result"]["tools"]]
    assert "webgen_list_templates" in tool_names
    assert "webgen_generate_site" in tool_names

def test_mcp_server_generate_site_call():
    with tempfile.TemporaryDirectory() as tmpdir:
        out_file = Path(tmpdir) / "mcp_site.html"
        req = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "webgen_generate_site",
                "arguments": {
                    "template": "saas-dashboard",
                    "output_path": str(out_file)
                }
            }
        }
        res = handle_request(req)
        assert res["id"] == 3
        assert "isError" not in res
        assert out_file.exists()
