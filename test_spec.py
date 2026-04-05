"""
mini-notes SPEC test senaryolari
Ogrenci: Pelin Kışlak (251478025)
Proje: mini-notes
"""
import subprocess
import os
import shutil

def run_cmd(args):
    """Komutu calistir, stdout dondur."""
    result = subprocess.run(
        ["python", "mininotes.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def setup_function():
    """Her testten once temiz baslangic."""
    if os.path.exists(".mininotes"):
        shutil.rmtree(".mininotes")

# --- init testleri ---
def test_init_creates_files():
    run_cmd(["init"])
    assert os.path.exists(".mininotes"), ".mininotes dizini olusturulmali"
    assert os.path.exists(".mininotes/notes.dat"), "notes.dat dosyasi olusturulmali"

def test_init_twice():
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output

# --- add testleri ---
def test_add_note():
    run_cmd(["init"])
    output = run_cmd(["add", "Hello World"])
    assert "Note saved" in output

def test_add_multiple_notes():
    run_cmd(["init"])
    run_cmd(["add", "First note"])
    output = run_cmd(["add", "Second note"])
    assert "ID: 2" in output

# --- list testleri ---
def test_list_not_implemented():
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "will be implemented" in output

# --- search testleri ---
def test_search_not_implemented():
    run_cmd(["init"])
    output = run_cmd(["search", "test"])
    assert "will be implemented" in output

# --- hata testleri ---
def test_error_before_init():
    output = run_cmd(["add", "Test"])
    assert "Not initialized" in output

def test_unknown_command():
    run_cmd(["init"])
    output = run_cmd(["fly"])
    assert "Unknown command" in output

def test_add_missing_args():
    run_cmd(["init"])
    output = run_cmd(["add"])
    assert "Usage:" in output

def test_no_args():
    output = run_cmd([])
    assert "Usage:" in output