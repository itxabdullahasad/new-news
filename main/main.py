from src.Agents import NewsProcessingAgents
from src.Tasks import NewsProcessingTasks
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from crewai import Crew, Process
from langchain.agents import AgentExecutor
from apps import new_inputs

load_dotenv()
os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.getenv("Anthropic_Api_Key")

llm = ChatAnthropic(model_name="claude-3-opus-20240229", temperature=0.3, max_tokens_to_sample=200)

tasks = NewsProcessingTasks()
agents = NewsProcessingAgents()

participants, context, objective = new_inputs()
print(participants)
print(context)
print(objective)

# Create Agents
news_research_agent = agents.news_research_agent()
news_analysis_agent = agents.news_analysis_agent()
fact_checker_agent = agents.fact_checker_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

# Create Tasks
news_research_task = tasks.news_research_task(news_research_agent, participants, context)
news_analysis_task = tasks.news_analysis_task(news_analysis_agent, participants, context)
fact_checker_task = tasks.fact_checker_task(fact_checker_agent, participants, [news_research_task, news_analysis_task])
meeting_strategy_task = tasks.meeting_strategy_task(meeting_strategy_agent, [fact_checker_task], objective)
summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent, [fact_checker_task, meeting_strategy_task], objective)

crew = Crew(
    agents=[
        news_research_agent,
        news_analysis_agent,
        fact_checker_agent,
        meeting_strategy_agent,
        summary_and_briefing_agent
    ],
    tasks=[
        news_research_task,
        news_analysis_task,
        fact_checker_task,
        meeting_strategy_task,
        summary_and_briefing_task
    ],
    process=Process.hierarchical,
    manager_llm=llm
)

result = crew.kickoff()

# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")
print(result)

# from IPython.display import display, Markdown
# display(Markdown(result))
