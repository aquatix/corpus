from pathlib import Path

import links

all_files = list(Path.home().joinpath("phren").rglob("*.[mM][dD]"))
print(all_files)

with open('../README.md', 'r') as f:
    text = f.read()
    links = links.extract_links(text)
