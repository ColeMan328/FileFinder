def replace_first_occurrences(file_path, replacements):
    """
    Replace the first occurrence of each target string in the replacements dictionary
    with its corresponding replacement string.

    :param file_path: Path to the HTML file.
    :param replacements: A dictionary where keys are target strings and values are replacement strings.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    # Replace the first occurrence of each target string
    for target_string, replacement_string in replacements.items():
        contents = contents.replace(target_string, replacement_string, 1)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contents)

    print(f"Replaced the first occurrences of specified strings in {file_path}")

# Example usage
html_file_path = 'example.html'  # Path to your HTML file
replacements = {
    'old_string1': 'new_string1',
    'old_string2': 'new_string2',
    'old_string3': 'new_string3',
}

replace_first_occurrences(html_file_path, replacements)
