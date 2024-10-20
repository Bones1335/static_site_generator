def markdown_to_blocks(markdown):
    blocks = markdown.split("\n")
    new_blocks = []
    list_block = []
    for block in blocks:
        if block == "":
            continue
        if block[0] == "*":
            list_block.append(block.strip())
        else:
            new_blocks.append(block.strip())
    new_blocks.append("\n".join(list_block))
    return new_blocks
