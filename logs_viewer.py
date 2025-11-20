import json

def view_logs():
    print("\n=== SmartAssist Logs ===\n")
    with open("logs.txt", "r") as f:
        for line in f.readlines():
            print("•", line.strip())

if __name__ == "__main__":
    view_logs()
