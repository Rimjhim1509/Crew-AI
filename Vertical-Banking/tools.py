import os
import random
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from crewai.tools import BaseTool  # Correct import for BaseTool

# Load environment variables
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("OPENAI_API_KEY not found in environment.")


# ---------------------------
# Input schemas for tools
# ---------------------------

class DataCollectInput(BaseModel):
    applicant: dict = Field(..., description="Applicant record")

class VerifyKYCInput(BaseModel):
    profile: dict = Field(..., description="Applicant profile")

class CreditAssessorInput(BaseModel):
    profile: dict = Field(..., description="Applicant profile")

class FraudDetectorInput(BaseModel):
    profile: dict = Field(..., description="Applicant profile")

class ReportGeneratorInput(BaseModel):
    profile: dict = Field(..., description="Applicant profile")
    kyc: dict = Field(..., description="KYC result")
    credit: dict = Field(..., description="Credit result")
    fraud: dict = Field(..., description="Fraud result")


# ---------------------------
# Tool implementations
# ---------------------------

class DataCollectTool(BaseTool):
    name: str = "Data Collector"
    description: str = "Extract and structure applicant profile data from CSV row."
    args_schema = DataCollectInput

    def _run(self, applicant: dict) -> dict:
        return {
            "id": applicant["Loan_ID"],
            "gender": applicant["Gender"],
            "education": applicant["Education"],
            "income": applicant["ApplicantIncome"],
            "loan_amount": applicant["LoanAmount"],
            "credit_history": applicant["Credit_History"],
            "property_area": applicant["Property_Area"],
        }

class VerifyKYCTool(BaseTool):
    name: str = "KYC Verifier"
    description: str = "Simulate KYC verification for applicant profile."
    args_schema = VerifyKYCInput

    def _run(self, profile: dict) -> dict:
        verified = random.choice([True, True, True, False])
        return {"verified": verified, "remarks": "KYC Verified" if verified else "Verification Failed"}

class AssessCreditTool(BaseTool):
    name: str = "Credit Assessor"
    description: str = "Compute credit score and risk level based on applicant data."
    args_schema = CreditAssessorInput

    def _run(self, profile: dict) -> dict:
        score = 700
        if profile["income"] < 4000:
            score -= 100
        if profile["loan_amount"] > profile["income"] / 2:
            score -= 50
        if profile["credit_history"] == 0:
            score -= 150
        risk = "LOW" if score >= 650 else "MEDIUM" if score >= 550 else "HIGH"
        return {"credit_score": score, "risk_level": risk}

class FraudDetectorTool(BaseTool):
    name: str = "Fraud Detector"
    description: str = "Detect anomalies and potential fraud in applicant profile."
    args_schema = FraudDetectorInput

    def _run(self, profile: dict) -> dict:
        risk = "LOW"
        notes = []
        if profile["loan_amount"] > profile["income"]:
            risk = "HIGH"
            notes.append("Loan > Income")
        if profile["education"] == "Not Graduate" and profile["loan_amount"] > 200:
            notes.append("High loan for non-graduate")
        return {"fraud_risk": risk, "notes": notes}

class GenerateReportTool(BaseTool):
    name: str = "Report Generator"
    description: str = "Generate Markdown report summarizing applicant evaluation."
    args_schema = ReportGeneratorInput

    def _run(self, profile: dict, kyc: dict, credit: dict, fraud: dict) -> str:
        os.makedirs("outputs", exist_ok=True)
        filename = f"outputs/{profile['id']}_loan_report.md"
        with open(filename, "w") as f:
            f.write(f"# Loan Report - {profile['id']}\n\n")
            f.write(f"**Applicant:** {profile['gender']} ({profile['education']})\n")
            f.write(f"**Income:** ₹{profile['income']}\n")
            f.write(f"**Loan Amount:** ₹{profile['loan_amount']}\n\n")
            f.write(f"### KYC Status: {kyc['remarks']}\n")
            f.write(f"### Credit Score: {credit['credit_score']} ({credit['risk_level']})\n")
            f.write(f"### Fraud Risk: {fraud['fraud_risk']}\n")
            f.write(f"Notes: {', '.join(fraud['notes']) if fraud['notes'] else 'None'}\n")
        return filename


# ---------------------------
# Tool instances to use in tasks
# ---------------------------

data_collect_tool = DataCollectTool()
verify_kyc_tool = VerifyKYCTool()
assess_credit_tool = AssessCreditTool()
detect_fraud_tool = FraudDetectorTool()
generate_report_tool = GenerateReportTool()
