from crewai import Agent, Task, Crew, Process

# Define the Market Research Agent
researcher = Agent(
  role='Market Analyst',
  goal='Analyze the UAE AI market trends for 2026',
  backstory='Expert in GCC tech landscapes and digital transformation.',
  verbose=True,
  allow_delegation=False
)

# Define the Task
task1 = Task(
  description='Summarize the top 3 AI sectors growing in Dubai and Abu Dhabi.',
  agent=researcher,
  expected_output='A bullet-point report on 3 key AI growth sectors.'
)

# Instantiate the Crew
crew = Crew(
  agents=[researcher],
  tasks=[task1],
  verbose=True,
  process=Process.sequential
)

# Execute
print("### Starting the AI Agent Workflow ###")
result = crew.start()
print("\n### Final Report ###\n")
print(result)
