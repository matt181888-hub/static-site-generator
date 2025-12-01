def markdown_to_blocks(markdown):
    md_list = markdown.split("\n\n")
    new_list = []
    for md in md_list:
        new_md = md.strip()
        if new_md:
            new_list.append(new_md)
    return new_list

