# ### Data Preparation
# 1. Load the dataset from the "armut_data.csv" file.

import pandas as pd
from efficient_apriori import apriori, generate_rules_apriori


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 1500)

df = pd.read_csv("data.csv")


# ### Create a New Service Identifier
# 1. Combine the `ServiceId` and `CategoryId` columns using "_" to create a new variable called `Services`.

df["Services"] = df["ServiceId"].astype(str) + "_" + df["CategoryId"].astype(str)


# ### Define Shopping Baskets
# 1. To apply Association Rule Learning, we need to define shopping baskets. In this case, each basket corresponds to
# the services purchased by a customer within a specific month.
# 2. Create a new date variable containing only the year and month information.
# 3. Combine the `UserId` and the new date variables with "_" to create a unique basket identifier called `CartID`.

df["Year"] = df["CreateDate"].str[:4]
df["Month"] = df["CreateDate"].str[5:7]
df["CardID"] = df["UserId"].astype(str) + "_" + df["Year"] + "_" + df["Month"]


# ### Generate Association Rules
# 1. Use Apriori algorithm to discover association rules among the purchased services.
# 2. Filter the rules based on desired support and confidence levels.

user_groups = df.groupby("UserId")['Services'].apply(list).reset_index(name='ServicesList')

itemsets, rules = apriori(user_groups['ServicesList'], min_support=0.01, min_confidence=0.10)

rule_list = []
for rule in rules:
    antecedents = list(rule.lhs)
    consequents = list(rule.rhs)
    support = rule.support
    confidence = rule.confidence
    lift = rule.lift
    rule_list.append([antecedents, consequents, support, confidence, lift])

rules_df = pd.DataFrame(rule_list, columns=["Antecedents", "Consequents", "Support", "Confidence", "Lift"])
print(rules_df)

rules_df.sort_values("Lift", ascending=False)


# ### Generate Recommendations
# 1. Implement the `arl_recommender` function to recommend services to customers based on their previous purchases.
# 2. Provide recommendations to customers who recently purchased a specific service (e.g., "2_0").

def arl_recommender(rules_df, product_id, rec_count=3):
    sorted_rules = rules_df.sort_values("Lift", ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["Antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["Consequents"]))

    return recommendation_list[0:rec_count]


product_id = "25_0"
recommendations = arl_recommender(rules_df, product_id, rec_count=3)
print(recommendations)


# Check:
filtered_rules = rules_df[rules_df["Antecedents"].apply(lambda x: "25_0" in x)].sort_values("Lift", ascending=False)
print(filtered_rules)