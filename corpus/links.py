import markdown
import re


def extract_links(string):
    """Return a list with markdown links"""
    # Inspired by https://github.com/andrewp-as-is/markdown-link-extractor.py
    html = markdown.markdown(string, output_format='html')
    links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', html)))
    links = list(filter(lambda l: l[0] != "{", links))
    return links
