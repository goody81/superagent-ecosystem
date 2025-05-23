class Agent:
    def __init__(self, role, mcps, parent=None):
        self.role = role
        self.mcps = mcps
        self.parent = parent
        self.memory = []

    def perform_task(self):
        result = f"{self.role} did its job"
        self.memory.append(result)
        self.mcps.log_experience(self.role, result)
        if self.parent:
            self.parent.receive_update(self, result)

    def receive_knowledge(self, knowledge):
        print(f"[{self.role}] Received new knowledge: {knowledge}")
