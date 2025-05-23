from collections import defaultdict

class MCPS:
    def __init__(self):
        self.memory = defaultdict(list)

    def log_experience(self, agent_name, experience):
        self.memory[agent_name].append(experience)
        print(f"[MCPS] Logged for {agent_name}: {experience}")

    def get_memory(self, agent_name):
        return self.memory.get(agent_name, [])

    def broadcast(self, knowledge):
        print(f"[MCPS] Broadcasting knowledge: {knowledge}")
