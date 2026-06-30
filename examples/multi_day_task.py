"""Example: a long-horizon task spanning multiple agent sessions, using memory."""
from agent.core import ClaudeFable5Agent
from agent.memory import ConversationMemory

if __name__ == "__main__":
    memory = ConversationMemory(".migration_session.json")
    agent = ClaudeFable5Agent()
    agent.conversation_history = memory.load()

    try:
        response = agent.chat("Продолжи работу над миграцией базы данных, начатую в прошлой сессии.")
        print(response)
    finally:
        memory.save(agent.conversation_history)
