# Multi-Agent Loan Processing System 🤖💰

This system simulates an **automated loan processing pipeline** using multiple specialized agents, each responsible for a different stage of applicant evaluation. It is designed to be modular, extensible, and easy to understand.

---

## 🛠️ System Architecture

<img width="1000" alt="System Architecture Diagram" src="https://github.com/user-attachments/assets/179cc03f-431b-48be-962e-cc961f03c31e" />

> **Figure:** Flow of data through different agents and tools in the loan processing system.

---

## 🧩 Agents and Tools

| Agent | Role | Tool Used | Purpose |
|-------|------|-----------|---------|
| **Data Intake Agent** | Prepares applicant data | `DataCollectTool` | Extracts structured profiles from raw CSV input. |
| **KYC Verification Agent** | Identity verification | `VerifyKYCTool` | Checks applicant identity and compliance with KYC norms. |
| **Credit Scoring Agent** | Financial evaluation | `AssessCreditTool` | Computes credit score and risk level based on financial data. |
| **Fraud Detection Agent** | Risk analysis | `FraudDetectorTool` | Flags potential anomalies or fraudulent activity. |
| **Notification & Reporting Agent** | Reporting | `GenerateReportTool` | Generates Markdown reports summarizing applicant evaluation. |

---
## **📝 How It Works**

**1. Data Intake Agent**  
- Reads raw CSV data of applicants.  
- Converts it into structured profiles with all necessary fields (e.g., `id`, `income`, `loan_amount`, `credit_history`).  

**2. KYC Verification Agent**  
- Validates applicant identity against KYC norms.  
- Returns verification status and remarks.  

**3. Credit Scoring Agent**  
- Calculates credit score based on income, loan amount, and credit history.  
- Assigns a risk level: **LOW**, **MEDIUM**, or **HIGH**.  

**4. Fraud Detection Agent**  
- Detects anomalies such as unusually high loans or inconsistent data.  
- Flags fraud risk and provides detailed notes on suspicious patterns.  

**5. Notification & Reporting Agent**  
- Aggregates results from all agents.  
- Generates a comprehensive **Markdown report** for each applicant.  
- Saves the report for documentation, auditing, or downstream processes.  

## 🔄 Step-by-Step Workflow

```text
[Raw Applicant Data CSV]
           │
           ▼
  Data Intake Agent
  (DataCollectTool)
           │
           ▼
 KYC Verification Agent
  (VerifyKYCTool)
           │
           ▼
 Credit Scoring Agent
  (AssessCreditTool)
           │
           ▼
 Fraud Detection Agent
  (FraudDetectorTool)
           │
           ▼
Notification & Reporting Agent
 (GenerateReportTool)
           │
           ▼
      Markdown Report
