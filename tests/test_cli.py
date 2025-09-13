import subprocess, sys

def _run(args=None):
    args = args or []
    # python -m hello_cli を実行して標準出力を返す
    res = subprocess.run([sys.executable, "-m", "hello_cli", *args],
                         capture_output=True, text=True, check=True)
    return res.stdout

def test_cli_default():
    out = _run([])
    assert "Hello, world!" in out

def test_cli_with_name():
    out = _run(["--name", "kazuma"])
    assert "Hello, kazuma!" in out
