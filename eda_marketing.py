import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Dataset Shape:", df.shape)
print("\nMissing Values:\n")
print(df.isnull().sum())

# ==========================
# DATA CLEANING
# ==========================

# Remove missing income rows
df = df.dropna(subset=["Income"])

# Convert date column
df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    format="%d-%m-%Y"
)

# Age
df["Age"] = 2025 - df["Year_Birth"]

# Total Children
df["Children"] = df["Kidhome"] + df["Teenhome"]

# Total Spending
df["Total_Spending"] = (
    df["MntWines"]
    + df["MntFruits"]
    + df["MntMeatProducts"]
    + df["MntFishProducts"]
    + df["MntSweetProducts"]
    + df["MntGoldProds"]
)

# Total Purchases
df["Total_Purchases"] = (
    df["NumWebPurchases"]
    + df["NumCatalogPurchases"]
    + df["NumStorePurchases"]
)

# Campaign Acceptance
df["Accepted_Any_Campaign"] = (
    df["AcceptedCmp1"]
    + df["AcceptedCmp2"]
    + df["AcceptedCmp3"]
    + df["AcceptedCmp4"]
    + df["AcceptedCmp5"]
)

print("\nData cleaned successfully")

# ==========================
# BASIC INSIGHTS
# ==========================

print("\nAverage Income:")
print(df["Income"].mean())

print("\nAverage Spending:")
print(df["Total_Spending"].mean())

print("\nCampaign Response Rate:")
print(df["Response"].mean() * 100)

# ==========================
# VISUALIZATION 1
# Customer Age Distribution
# ==========================

plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=20)
plt.title("Customer Age Distribution")
plt.savefig("age_distribution.png")
plt.show()

# ==========================
# VISUALIZATION 2
# Income vs Spending
# ==========================

plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Income",
    y="Total_Spending"
)
plt.title("Income vs Spending")
plt.savefig("income_vs_spending.png")
plt.show()

# ==========================
# VISUALIZATION 3
# Purchases by Channel
# ==========================

channels = {
    "Web": df["NumWebPurchases"].sum(),
    "Catalog": df["NumCatalogPurchases"].sum(),
    "Store": df["NumStorePurchases"].sum()
}

plt.figure(figsize=(6,4))
plt.bar(channels.keys(), channels.values())
plt.title("Purchases by Channel")
plt.savefig("purchase_channel.png")
plt.show()

# ==========================
# VISUALIZATION 4
# Campaign Acceptance
# ==========================

campaigns = [
    "AcceptedCmp1",
    "AcceptedCmp2",
    "AcceptedCmp3",
    "AcceptedCmp4",
    "AcceptedCmp5"
]

campaign_data = df[campaigns].sum()

plt.figure(figsize=(8,5))
campaign_data.plot(kind="bar")
plt.title("Campaign Acceptance Count")
plt.ylabel("Accepted Customers")
plt.savefig("campaign_acceptance.png")
plt.show()

# ==========================
# VISUALIZATION 5
# Product Spending
# ==========================

products = {
    "Wine": df["MntWines"].sum(),
    "Fruits": df["MntFruits"].sum(),
    "Meat": df["MntMeatProducts"].sum(),
    "Fish": df["MntFishProducts"].sum(),
    "Sweets": df["MntSweetProducts"].sum(),
    "Gold": df["MntGoldProds"].sum()
}

plt.figure(figsize=(8,5))
plt.bar(products.keys(), products.values())
plt.title("Spending by Product Category")
plt.savefig("product_spending.png")
plt.show()

print("\nEDA Completed Successfully")