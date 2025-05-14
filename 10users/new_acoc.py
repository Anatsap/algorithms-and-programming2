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


def user_texts():
    files_directory = input('Enter the path of the files: ')
    result = []
    for user in range(10):
        file = os.path.join(files_directory, 'user_{}.txt'.format(user + 1))
        with open(file, 'r') as f:
            result.append(f.read())
    return result

def spammer_text():
    with open(file_path, "r") as file:
        phrases = []
        for line in file:
            phrases.append(line.strip())
        return phrases


if __name__ == "__main__":
    file_path = "spammer.txt"
    if os.stat(file_path).st_size == 0:
        print("File is empty, you can not search")
    else:
        texts = user_texts()
        phrases = spammer_text()
        for i, text in enumerate(texts):
            match = search_text(text, phrases)

            found = 0
            for word in match:
                if match[word]:
                    found += 1
            percentage = (found / len(phrases)) * 100
            print(f"User {i + 1}: {percentage:.2f}% spam similarity")
