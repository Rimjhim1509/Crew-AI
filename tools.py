from dotenv import load_dotenv
import os

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("OPENAI_API_KEY not found in environment.")

from crewai_tools import YoutubeChannelSearchTool
yt_tool =YoutubeChannelSearchTool(youtube_channel_url='CARachanaRanade')
