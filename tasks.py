from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer

## researcher Task

researcher_task= Task(
    description=("Identify the video {topic}."
                "Get the detailed information about the video from the channel video."),
    expected_output = 'A comprehencsive 5 paragraph long report based on the {topic} of the video content and provide the bulletpoints of the important topic.',
    tools=[yt_tool],
    agent=blog_researcher,
    
   #             
)

## writer Task

writer_task= Task(
    description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='Stock_market.md'  # Example of output customization
)