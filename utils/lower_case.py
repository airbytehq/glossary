from pandoc.types import *
import os

link_index_path = "assets/indices/linkIndex.json"
content_path = "content"


def convert_glossary_terms_lower_case(file_path: str):
    # recursively convert all filenames to lower case
    for root, dirs, files in os.walk(file_path):
        for filename in files:
            os.rename(
                os.path.join(root, filename), os.path.join(root, filename.lower())
            )


def convert_to_lower_case(file_path: str):
    """converting linkIndex.json file that is used for creating the paths. As we lowe lower case all glossary terms, we need to update these here as well"""
    with open(file_path, "r") as f:
        content = f.read()
        content = content.lower()
        with open(file_path, "w") as f:
            f.write(content)


if __name__ == "__main__":
    convert_glossary_terms_lower_case(content_path)
    convert_to_lower_case(link_index_path)
