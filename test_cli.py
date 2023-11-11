import os
import subprocess

def test_cli():
    if os.path.exists("test_data/the_sorcerers_stone.txt"):
        os.remove("test_data/the_sorcerers_stone.txt")
    subprocess.run(["python3", "pdf_extractor.py", "test_data/the_sorcerers_stone.pdf", "test_data/the_sorcerers_stone.txt"], check=True)
    assert os.path.exists("test_data/the_sorcerers_stone.txt")
    os.remove("test_data/the_sorcerers_stone.txt")