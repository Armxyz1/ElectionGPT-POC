from agent import get_agent

def main():
    agent = get_agent()

    print("Election Agent Ready. Ask a question (type 'exit' to quit).")
    while True:
        question = input(">> ")
        if question.lower() in ["exit", "quit"]:
            break
        try:
            response = agent.run(question)
            print("\nAnswer:", response, "\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
