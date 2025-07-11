import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


file_path=Path("C:/Users/Sajjad_Lab/Downloads/Titanic-Dataset.csv")
df=pd.read_csv(file_path)
print(df.shape)          # (rows, columns)
print(df.columns)        # column names
print(df.dtypes)         # data types
print(df.head(10))       # first 10 rows
print(df.describe())     # stats summary

missing_values= df.isnull().sum()
print(f"Missing values per Column: \n{missing_values}")


df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.drop(columns=["Cabin"])
df["Embarked"]= df['Embarked'].fillna(df["Embarked"].mode()[0])
print(df.isnull().sum())

sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival Count by Gender")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

sns.countplot(x='Pclass', data=df)
plt.title("Passenger Count by Class")
plt.xlabel("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)")
plt.ylabel("Count")
plt.show()

sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.show()

sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")
plt.show()

sns.countplot(x='Pclass', hue='Sex', data=df[df['Survived']==1])
plt.title("Survivors by Class and Gender")
plt.xlabel("Class")
plt.ylabel("Number of Survivors")
plt.show()
