from rag.rag_pipeline import RAGPipeline
from agent.agent import SmartAssistAgent

def main():
    rag = RAGPipeline()
    agent = SmartAssistAgent(rag)

    while True:
        query = input("\nAsk SmartAssist: ")
        response = agent.run(query)
        
        print("\nPLAN:", response["plan"])
        print("\nANSWER:", response["answer"])

if __name__ == "__main__":
    main()
