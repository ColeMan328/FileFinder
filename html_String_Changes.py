def replace_first_occurrences_with_links(file_path, replacements):
    """
    Replace the first occurrence of each target string in the replacements dictionary
    with its corresponding hyperlink.

    :param file_path: Path to the HTML file.
    :param replacements: A dictionary where keys are target strings and values are tuples of (replacement text, URL).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    # Replace the first occurrence of each target string with a hyperlink
    for target_string, (replacement_text, url) in replacements.items():
        hyperlink = f'<a href="{url}">{replacement_text}</a>'
        contents = contents.replace(target_string, hyperlink, 1)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contents)

    print(f"Replaced the first occurrences of specified strings with hyperlinks in {file_path}")

# Example usage
html_file_path = 'example.html'  # Path to your HTML file
replacements = {
    'old_string1': ('new_text1', 'http://example.com/link1'),
    'old_string2': ('new_text2', 'http://example.com/link2'),
    'old_string3': ('new_text3', 'http://example.com/link3'),
}

replace_first_occurrences_with_links(html_file_path, replacements)
