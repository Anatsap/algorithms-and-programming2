import random

file_size_mb = 50
target_bytes = file_size_mb * 1024 * 1024  # 50 МБ
chunk_size = 1024 * 1024  # 1 МБ за раз
written = 0

with open("haystack.txt", "w") as f:
    while written < target_bytes:
        chunk = []
        for _ in range(chunk_size):
            bit = "1" if random.random() < 0.3 else "0"
            chunk.append(bit)
        f.write("".join(chunk))
        written += chunk_size

print("Файл 'haystack.txt' створено успішно. Розмір ~50 МБ.")
