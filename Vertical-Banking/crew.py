from crewai import Crew, Agent, Task


from agents import data_intake_agent, kyc_verification_agent, credit_scoring_agent, fraud_detection_agent, notification_reporting


from tasks import (
    data_intake_task,
    kyc_task,
    credit_task,
    fraud_task,
    report_task
)

loan_approval_crew = Crew(
    agents=[
        data_intake_agent,
        kyc_verification_agent,
        credit_scoring_agent,
        fraud_detection_agent,
        notification_reporting
    ],
    
    tasks=[
        data_intake_task,
        kyc_task,
        credit_task,
        fraud_task,
        report_task
    ],
    process="sequential"   
)

if __name__ == "__main__":
    result = loan_approval_crew.run({"dataset_path": "train_u6lujuX_CVtuZ9i (1).csv"})
    print(result)
