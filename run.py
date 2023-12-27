from src.agent import Agent

world_state = {}

if __name__ == "__main__":
    agent = Agent(world_state=world_state)
    print(agent.goals)
