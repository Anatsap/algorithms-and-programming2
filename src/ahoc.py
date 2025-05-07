import os
class TrieNode:
    def __init__(self):
        self.children = {}
        self.output = []
        self.fail = None


def build_automaton(keywords):
    root = TrieNode()
    for keyword in keywords:
        node = root
        for char in keyword:
            node = node.children.setdefault(char, TrieNode())
        node.output.append(keyword)

    queue = []
    for node in root.children.values():
        queue.append(node)
        node.fail = root

    while queue:
        current_node = queue.pop(0)
        for key, next_node in current_node.children.items():
            queue.append(next_node)
            fail_node = current_node.fail
            while fail_node and key not in fail_node.children:
                fail_node = fail_node.fail
            next_node.fail = fail_node.children[key] if fail_node else root
            next_node.output += next_node.fail.output

    return root


def search_text(text, keywords):
    root = build_automaton(keywords)
    result = {keyword: [] for keyword in keywords}

    current_node = root
    for i, char in enumerate(text):
        while current_node and char not in current_node.children:
            current_node = current_node.fail

        if not current_node:
            current_node = root
            continue
        current_node = current_node.children[char]
        for keyword in current_node.output:
            result[keyword].append(i - len(keyword) + 1)

    return result


if __name__ == "__main__":
    file_path = "haystack.txt"
    if os.stat(file_path).st_size == 0:
        print("File is empty, you can not search ")
    else:
        with open("needle.txt") as textfile1, open("haystack.txt") as textfile2:
            for x, y in zip(textfile1, textfile2):
                needle = x.strip()
                haystack = y.strip()
                needles = needle.split()
                match = search_text(haystack, needles)
                #print(match)

                final_text = []
                text_to_delete = set()
                for word in match:
                    positions = match[word]
                    for pos in positions:
                        for j in range(pos, pos + len(word)):
                            text_to_delete.add(j)
                for h in range(len(haystack)):
                    if h not in text_to_delete:
                        final_text.append(haystack[h])
                    else:
                        continue

                new_file = "new_file.txt"
                with open(new_file, 'w') as file:
                    file.write("".join(final_text))
                print(f"File '{new_file}' created successfully.")