from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

# define llm before using it in Agent; replace None with a real LLM object if available
llm = None


##Create a Senior Blog Content Researcher

blog_researcher = Agent(
    role='Blog Researcher from Youtube videos',
    goal='get the relevant video content for the topic{topic}for the Youtube Videos',
    verboe=True,
    memory= True,
    backstory=(
        "Expert in understanding videos in AI Data Science , Machine Learning and GEN AI and providing suggestion"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
    )

##creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narrative that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
        
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)