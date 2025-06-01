"""
Content Marketing Crew Implementation
"""
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from datetime import datetime
import dotenv
# dotenv.load_dotenv()
# import agentops
# agentops.init()
@CrewBase
class ContentMarketingCrew:
    """Content Marketing Crew for automated content generation across multiple platforms"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        # Initialize tools
        self.serper_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        
        # Get current date for research tasks
        self.current_date = datetime.now().strftime("%B %d, %Y")
    
    @agent
    def research_strategist(self) -> Agent:
        """Research Strategist Agent for market research and trend analysis"""
        return Agent(
            config=self.agents_config['research_strategist'],
            tools=[self.serper_tool, self.scrape_tool],
            verbose=True,
            max_iter=5
        )
    
    @agent
    def content_strategist(self) -> Agent:
        """Content Strategist Agent for strategic planning"""
        return Agent(
            config=self.agents_config['content_strategist'],
            verbose=True,
            max_iter=3
        )
    
    @agent
    def content_writer(self) -> Agent:
        """Content Writer Agent for creating initial content drafts"""
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True,
            max_iter=3
        )
    
    @agent
    def content_editor(self) -> Agent:
        """Content Editor Agent for content refinement and quality improvement"""
        return Agent(
            config=self.agents_config['content_editor'],
            verbose=True,
            max_iter=3
        )
    
    @agent
    def platform_adapter(self) -> Agent:
        """Platform Adapter Agent for platform-specific content optimization"""
        return Agent(
            config=self.agents_config['platform_adapter'],
            verbose=True,
            max_iter=3
        )
    
    @agent
    def seo_optimizer(self) -> Agent:
        """SEO Optimizer Agent for search engine optimization"""
        return Agent(
            config=self.agents_config['seo_optimizer'],
            verbose=True,
            max_iter=3
        )
    
    # Phase 1: Research & Strategy Tasks
    @task
    def market_research_task(self) -> Task:
        """Research latest market trends and competitor insights"""
        return Task(
            config=self.tasks_config['market_research_task']
        )
    
    @task
    def audience_analysis_task(self) -> Task:
        """Analyze target audience behavior and preferences"""
        return Task(
            config=self.tasks_config['audience_analysis_task']
        )
    
    @task
    def content_strategy_task(self) -> Task:
        """Develop comprehensive content strategy"""
        return Task(
            config=self.tasks_config['content_strategy_task']
        )
    
    # Phase 2: Content Creation Tasks
    @task
    def draft_content_task(self) -> Task:
        """Create initial content draft"""
        return Task(
            config=self.tasks_config['draft_content_task']
        )
    
    @task
    def edit_content_task(self) -> Task:
        """Edit and refine content quality"""
        return Task(
            config=self.tasks_config['edit_content_task']
        )
    
    @task
    def optimize_blog_seo_task(self) -> Task:
        """Optimize blog content for SEO"""
        return Task(
            config=self.tasks_config['optimize_blog_seo_task']
        )
    
    # Phase 3: Platform Adaptation Tasks
    @task
    def adapt_instagram_task(self) -> Task:
        """Adapt content for Instagram platform"""
        return Task(
            config=self.tasks_config['adapt_instagram_task']
        )
    
    @task
    def adapt_linkedin_task(self) -> Task:
        """Adapt content for LinkedIn platform"""
        return Task(
            config=self.tasks_config['adapt_linkedin_task']
        )
    
    @task
    def adapt_twitter_task(self) -> Task:
        """Adapt content for Twitter platform"""
        return Task(
            config=self.tasks_config['adapt_twitter_task']
        )
    
    @task
    def adapt_facebook_task(self) -> Task:
        """Adapt content for Facebook platform"""
        return Task(
            config=self.tasks_config['adapt_facebook_task']
        )
    
    @task
    def finalize_blog_task(self) -> Task:
        """Finalize blog post with complete formatting"""
        return Task(
            config=self.tasks_config['finalize_blog_task']
        )
    
    @crew
    def crew(self) -> Crew:
        """Content Marketing Crew with sequential process"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            
        )
    
