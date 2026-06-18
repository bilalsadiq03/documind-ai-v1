# test_analyzer.py

from repo_analyzer import collect_files
from repo_analyzer import build_prompt

repo_path = "./repos/test"

files = collect_files(repo_path)

print("Files:", len(files))

prompt = build_prompt(files)

print(prompt[:3000])