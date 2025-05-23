class SuperAgent:
    def __init__(self, name, domain, mcps):
        self.name = name
        self.domain = domain
        self.mcps = mcps
        self.agents = []

    def spawn_agent(self, agent_class, role):
        agent = agent_class(role, self.mcps, parent=self)
        self.agents.append(agent)
        print(f"[{self.name}] Spawned agent: {agent.role}")
        return agent

    def receive_update(self, from_agent, update):
        print(f"[{self.name}] Received update from {from_agent.role}: {update}")
        self.mcps.log_experience(self.name, update)

    def push_knowledge(self, knowledge):
        for agent in self.agents:
            agent.receive_knowledge(knowledge)
