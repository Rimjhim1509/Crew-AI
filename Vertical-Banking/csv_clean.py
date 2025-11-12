import pandas as pd

df = pd.read_csv("train_u6lujuX_CVtuZ9i (1).csv")

print(df.columns)

# Fill missing values
df['Gender'].fillna('Male', inplace=True)
df['Married'].fillna('No', inplace=True)
df['Dependents'].fillna(0, inplace=True)
df['Self_Employed'].fillna('No', inplace=True)
df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
df['Loan_Amount_Term'].fillna(360, inplace=True)
df['Credit_History'].fillna(1.0, inplace=True)

# Convert to proper types
df['Dependents'] = df['Dependents'].astype(str)

applicant = df.iloc[0].to_dict()
print(applicant)