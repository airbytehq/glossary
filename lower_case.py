import os


content_path = "content"


def convert_glossary_terms_lower_case(file_path: str):
    # recursively convert all filenames to lower case
    for root, dirs, files in os.walk(file_path):
        for filename in files:
            os.rename(
                os.path.join(root, filename), os.path.join(root, filename.lower())
            )


if __name__ == "__main__":
    convert_glossary_terms_lower_case(content_path)
