import links

with open('../README.md', 'r') as f:
    text = f.read()
    links = links.extract_links(text)
