from crewai import Agent, Task, Crew, Process

# 1. تعريف الوكيل (الخبير)
researcher = Agent(
  role='AI Solutions Specialist',
  goal='Identify the best AI Agent use cases for enterprise automation in 2026',
  backstory='Expert in bridging legacy infrastructure with cutting-edge AI orchestration.',
  verbose=True,
  allow_delegation=False
)

# 2. تعريف المهمة
task1 = Task(
  description='Analyze how AI Agents can reduce operational costs in IT infrastructure by 70%.',
  agent=researcher,
  expected_output='A strategic report outlining 3 specific use cases for AI Agents in IT Ops.'
)

# 3. تشكيل الفريق (The Crew)
crew = Crew(
  agents=[researcher],
  tasks=[task1],
  verbose=True,
  process=Process.sequential
)

# 4. التنفيذ
print("### Starting the AI Orchestration Workflow ###")
result = crew.start()
print("\n### Strategic AI Report ###\n")
print(result)
