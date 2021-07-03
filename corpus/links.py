import re

import markdown


def extract_links(string):
    """Return a list with markdown links"""
    # Inspired by https://github.com/andrewp-as-is/markdown-link-extractor.py
    html = markdown.markdown(string, output_format='html')
    links = list(set(re.findall(r'href=[\'"]?([^\'" >]+)', html)))
    links = list(filter(lambda l: l[0] != "{", links))
    return links


def split_backlink_section_from_markdown(string):
    """Split the backlinks section from the markdown file, which should be the last, but doesn't have to be :)
    """
    # Find the section with Backlinks; if there are multiple for some reason, pick the last one
    markdown_parts = string.rsplit("# Backlinks")
    print(markdown_parts)
    backlinks_removed = markdown_parts[1].split('#')
    print(backlinks_removed)
    return markdown_parts


def find_backlinks_in_markdown(string):
    return string
