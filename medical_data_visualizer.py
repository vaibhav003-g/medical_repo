import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
    "Feature":["Age","Height","Weight","Gender","Systolic blood pressure","Diastolic blood pressure","Cholestrol",
               "Glucose","Smoking","Alcohol consumption","Physical activity","Presence or absence of cardiovascular disease"],

    "Variable Type":["Objective Feature","Objective Feature","Objective Feature","Objective Feature",
                     "Examination Feature","Examination Feature","Examination Feature","Examination Feature",
                     "Subjective Feature","Subjective Feature","Subjective Feature","Target Variable"],

    "Variable":["age","height","weight","gender","ap_hi","ap_lo","cholestrol","gluc","smoke","alco","active","cardio"],

    "Value Type":["int(days)","int(cm)","float(kg)","categorical code","int","int",
                  "1: normal, 2: above normal, 3: well above normal","1: normal, 2: above normal, 3: well above normal",
                  "binary","binary","binary","binary"]                 

}

df=pd.DataFrame(data)
print(df)

l=len(df)
df["height"]=int(input("enter your height in cm:"))
df["weight"]=float(input("enter your weight in kg:"))
df["bmi"]=(df["weight"]/(df["height"]*df["height"]))    
df["overweight"]=[0 if bmi < 25 else 1 for bmi in df["bmi"]]
print(df)


df["ap_hi"]=int(input("enter your systolic blood pressure:"))
df["ap_lo"]=int(input("enter your distolic blood pressure:"))
c=input("enter your cholestrol:")
g=input("enter your glucose:")
s=input("enter your smoking status(1 for yes,0 for no):")
a=input("enter your alcohol consumption status(1 for yes,0 for no):")
act=input("enter your physical activity status(1 for yes,0 for no):")
df["chol"]=c
df["glu"]=g
df["sm"]=s
df["al"]=a
df["ac"]=act
df["cholestrol"]=[0 if c=="1" else 1 for c in df["chol"]]
df["glucose"]=[0 if g=="1" else 1 for g in df["glu"]]
df["smoking"]=[0 if s=="1" else 1 for s in df["sm"]]
df["alcohol"]=[0 if a=="1" else 1 for a in df["al"]]
df["activity"]=[0 if act=="1" else 1 for act in df["ac"]]
print(df)


df_heat=df[df['ap_hi'] <= df['ap_lo']]
df_heat['height']=(df['height'] >= df['height'].quantile(0.025))
df_heat['height']=(df['height'] < df['height'].quantile(0.975))
df_heat["weight"]=(df["weight"]>=df["weight"].quantile(0.025))
df_heat["weight"]=(df["weight"]<df["weight"].quantile(0.975))
print(df_heat)

corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
