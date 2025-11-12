from crewai import Agent

from dotenv import load_dotenv

load_dotenv()
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

llm=None
data_intake_agent = Agent(
    role="Data Intake Agent",
    goal="Extract and structure applicant data for downstream processing",
    backstory="A meticulous data professional who prepares applicant profiles "
              "for KYC, credit scoring, and fraud analysis.",
    tools=[],
    verbose=True,
    memory=True,
    llm=llm
)
kyc_verification_agent = Agent(
    role="KYC Verification Officer",
    goal="Verify identity of applicants based on available data",
    backstory="A compliance officer ensuring all applicants pass KYC norms",
    tools=[],
    verbose=True,
    memory=True,
    llm=llm
)
credit_scoring_agent = Agent(
    role="Credit Analyst",
    goal="Evaluate applicant credit worthiness using profile data",
    backstory="A finance expert assessing applicant credit strength based on financial inputs",
    tools=[],
    verbose=True,
    memory=True,
    llm=llm
)
fraud_detection_agent = Agent(
    role="Fraud Detection Officer",
    goal="Identify potential fraud or anomalies in loan application",
    backstory="An experienced investigator skilled in pattern recognition and anomaly detection.",
    tools=[],
    verbose=True,
    memory=True,
    llm=llm
)
notification_reporting = Agent(
    role="Notification & Reporting Officer",
    goal="Generate final applicant evaluation report and store it in markdown format",
    backstory="A documentation expert who finalizes and stores the processed results.",
    tools=[],
    verbose=True,
    memory=True,
    llm=llm
)

