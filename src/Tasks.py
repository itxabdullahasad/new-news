from crewai import Task
from textwrap import dedent

class NewsProcessingTasks():

    def news_research_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""\
                Conduct thorough research on news articles and sources.

                Participants: {participants}
                Context: {context}"""),
            expected_output=dedent("""\
                A detailed report summarizing key findings from the news research."""),
            async_execution=True,
            agent=agent
        )

    def news_analysis_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""\
                Analyze news content to extract key insights and trends.

                Participants: {participants}
                Context: {context}"""),
            expected_output=dedent("""\
                An insightful analysis report identifying key insights and trends extracted from the news."""),
            async_execution=True,
            agent=agent
        )

    def fact_checker_task(self, agent, participants, context):
        return Task(
            description=dedent(f"""\
                Verify the accuracy and credibility of news information.

                Participants: {participants}
                Context: {context}"""),
            expected_output=dedent("""\
                A fact-checked report ensuring the accuracy and credibility of news information."""),
            async_execution=True,
            agent=agent
        )

    def meeting_strategy_task(self, agent, context, objective):
        return Task(
            description=dedent(f"""\
                Develop strategies based on news insights for meetings and decision-making.

                Context: {context}
                Objective: {objective}"""),
            expected_output=dedent("""\
                A strategic report outlining meeting strategies based on news insights, including talking points, questions, and strategic angles."""),
            async_execution=True,
            agent=agent
        )

    def summary_and_briefing_task(self, agent, context, objective):
        return Task(
            description=dedent(f"""\
                Compile news analysis into concise and informative briefings.

                Context: {context}
                Objective: {objective}"""),
            expected_output=dedent("""\
                A comprehensive briefing document summarizing news analysis, including key insights, trends, and recommendations."""),
            async_execution=True,
            agent=agent
        )
