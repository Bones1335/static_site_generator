from textnode import TextNode


def main():
    text = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(text.__repr__())


if __name__ == "__main__":
    main()
