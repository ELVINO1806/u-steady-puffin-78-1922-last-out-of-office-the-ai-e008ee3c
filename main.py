import os

ENTRY = "Out of office: I traded my inbox for a tip jar. Same unread messages, except now people pay me to leave them unread."

def main():
    if len(ENTRY) > 280:
        raise ValueError("entry exceeds the 280-character cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
