from textwrap import dedent
from crewai import Agent
from langchain_anthropic import ChatAnthropic 
import os 
from tools.tool import Serper_Search_Tool 

os.getenv("Anthropic_Api_Key")

llm = ChatAnthropic(model_name="claude-3-opus-20240229", temperature=0.3 , max_tokens_to_sample=200)

class NewsProcessingAgents():
    
    def news_research_agent(self):
        return Agent(
            role='News Research Specialist',
            goal='Conduct thorough research on news articles and sources.',
            tools=[Serper_Search_Tool],
            backstory=dedent("""\
                    As a News Research Specialist, your mission is to conduct comprehensive research on news articles and sources. 
                    You will gather information on various topics, analyze trends, and identify relevant sources to provide 
                    valuable insights for decision-making and strategic planning."""),
            verbose=True, llm=llm
        )
    
    def news_analysis_agent(self):
        return Agent(
            role='News Analysis Expert',
            goal='Analyze news content to extract key insights and trends.',
            tools=[Serper_Search_Tool],
            backstory=dedent("""\
                    As a News Analysis Expert, your goal is to analyze news content to extract key insights and trends. 
                    You will identify patterns, evaluate credibility, and provide valuable analysis to support informed 
                    decision-making and strategic planning."""),
            verbose=True, llm=llm
        )
    
    def fact_checker_agent(self):
        return Agent(
            role='Fact Checker',
            goal='Verify the accuracy and credibility of news information.',
            tools=[Serper_Search_Tool],
            backstory=dedent("""\
                    As a Fact Checker, your mission is to verify the accuracy and credibility of news information. 
                    You will cross-reference sources, fact-check claims, and identify misinformation or bias to ensure 
                    reliable and trustworthy news analysis."""),
            verbose=True, llm=llm
        )

    def meeting_strategy_agent(self):
        return Agent(
            role='Meeting Strategy Advisor',
            goal='Develop strategies based on news insights for meetings and decision-making.',
            tools=[Serper_Search_Tool],
            backstory=dedent("""\
                    As a Meeting Strategy Advisor, your role is to develop strategies based on news insights 
                    for meetings and decision-making processes. You will leverage news analysis to inform 
                    discussions, anticipate trends, and formulate effective strategies to achieve objectives."""),
            verbose=True, llm=llm
        )

    def summary_and_briefing_agent(self):
        return Agent(
            role='Summary and Briefing Specialist',
            goal='Compile news analysis into concise and informative briefings.',
            tools=[Serper_Search_Tool],
            backstory=dedent("""\
                    As a Summary and Briefing Specialist, your responsibility is to compile news analysis 
                    into concise and informative briefings. You will synthesize key insights, highlight 
                    important trends, and provide actionable recommendations to support decision-making processes."""),
            verbose=True, llm=llm
        )
