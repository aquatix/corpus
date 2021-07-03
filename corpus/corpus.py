from pathlib import Path

# from . import links
import links


def parse_files(all_files):

    links_from = {}
    links_to = {}
    for textfile in all_files:
        with open(textfile, 'r') as f:
            text = f.read()
            print(links.split_backlink_section_from_markdown(text))
            links_in_file = links.extract_links(text)
            print(links_in_file)


# all_files = list(Path.home().joinpath("phren").rglob("*.[mM][dD]"))
# print(all_files)
# parse_files(all_files)
parse_files(['/home/mbscholt/phren/homeautomation/lights.md'])
