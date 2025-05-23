from superagents.base_superagent import SuperAgent
from agents.base_agent import Agent
from mcps.mcps_core import MCPS

def run_workflow():
    mcps = MCPS()
    domains = ['Knowledge', 'Operations', 'Creativity']
    superagents = [SuperAgent(f"SuperAgent_{d}", d, mcps) for d in domains]
    roles = ['Researcher', 'Planner', 'Executor', 'QA', 'Communicator', 'Data', 'Innovator', 'Ops']
    for sa in superagents:
        for role in roles:
            sa.spawn_agent(Agent, role)
    for sa in superagents:
        for agent in sa.agents:
            agent.perform_task()
    for sa in superagents:
        sa.push_knowledge(f"Update from {sa.domain} domain")

if __name__ == "__main__":
    run_workflow()
