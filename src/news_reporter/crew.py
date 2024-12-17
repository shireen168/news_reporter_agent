from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class NewsReporter:
    """News Reporter Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def news_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['news_researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def report_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['report_compiler'],
            verbose=True
        )

    @task
    def fetch_news(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_news']
        )

    @task
    def compile_report(self) -> Task:
        return Task(
            config=self.tasks_config['compile_report'],
            context=[self.fetch_news()]  
        )

    @crew
    def NewsReporter(self) -> Crew:
        return Crew(
            agents=[
                self.news_researcher(),
                self.report_compiler()
            ],
            tasks=[
                self.fetch_news(),
                self.compile_report()
            ],
            process=Process.sequential,
            verbose=True
        )
    
    def run(self, inputs):
        crew_instance = self.NewsReporter()
        return crew_instance.kickoff(inputs=inputs)
