from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import researcher_task,writer_task

#Forming the tech-focused crew with some enhanced configurations

crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[researcher_task,writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)
## start the task execution 

result = crew.kickoff(inputs={'topic':'Basics of Stock Market For Beginners Lecture 1 By CA Rachana Phadke Ranade'})
print(result)