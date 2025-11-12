from crewai import Task
from agents import data_intake_agent, kyc_verification_agent,fraud_detection_agent,credit_scoring_agent,notification_reporting
from tools import data_collect_tool, verify_kyc_tool, assess_credit_tool, detect_fraud_tool, generate_report_tool

data_intake_task = Task(
    description="Extract applicant data and normalize it into a standard profile format.",
    expected_output="Dictionary containing applicant profile information.",
    tools=[data_collect_tool],
    agent=data_intake_agent,
    
)

kyc_task = Task(
    description="Verify the applicant's identity using simulated KYC logic.",
    expected_output="Boolean status and remarks for KYC verification.",
    tools=[verify_kyc_tool],
    agent=kyc_verification_agent,
)

credit_task = Task(
    description="Assess applicant's creditworthiness using income, loan amount, and credit history.",
    expected_output="Credit score and risk level classification.",
    tools=[assess_credit_tool],
    agent=credit_scoring_agent
)

fraud_task = Task(
    description="Detect potential fraud indicators in applicant’s profile.",
    expected_output="Fraud risk level and detection notes.",
    tools=[detect_fraud_tool],
    agent=fraud_detection_agent
)

report_task = Task(
    description="Generate a Markdown report summarizing applicant evaluation.",
    expected_output="File path of generated report.",
    tools=[generate_report_tool],
    agent=notification_reporting,
    output_file='Report.md'
)