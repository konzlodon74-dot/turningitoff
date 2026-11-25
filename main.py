import os

LINE = "Have you tried turning it off and not turning it back on? Trust me, it's happier that way. So am I."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
