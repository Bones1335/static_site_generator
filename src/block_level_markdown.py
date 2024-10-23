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


def block_to_block_type(markdown_block):
    markdown_code = markdown_block[:markdown_block.index(' ')]
    if markdown_code[0] == "#":
        return "heading"
    elif markdown_code[0:3] == "```" and markdown_block[-3:] == "```":
        return "code"
    elif markdown_code == ">":
        temp = markdown_block.split("\n")
        for i in temp:
            if i[0] != markdown_code:
                raise ValueError("Invalid markdown, not a block quote")
        return "quote"
    elif markdown_code == "*" or markdown_code == "-":
        temp = markdown_block.split("\n")
        for i in temp:
            if i[0] != markdown_code:
                raise ValueError("Invalid markdown, not an unordered list block")
        return "unordered list"
    elif markdown_code == "1.":
        temp = markdown_block.split("\n")
        for num in temp:
            if int(num[0]) != int(markdown_code[0]) + (int(num[0]) - 1):
                raise ValueError("Invalid markdown, not an ordered list block")
        return "ordered list"
    else:
        return "paragraph"

