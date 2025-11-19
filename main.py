from src.assistant import SmartAssistAI

def main():
    ai = SmartAssistAI()

    print("1. Text")
    print("2. Image")
    print("3. Multimodal")

    ch = input("Choose: ")

    if ch == "1":
        t = input("Enter text: ")
        print(ai.text(t))

    elif ch == "2":
        img = input("Enter image path: ")
        print(ai.image(img))

    elif ch == "3":
        t = input("Enter text: ")
        img = input("Enter image path: ")
        print(ai.multimodal(t, img))

if __name__ == "__main__":
    main()
