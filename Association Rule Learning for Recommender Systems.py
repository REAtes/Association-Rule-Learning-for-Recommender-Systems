# ### Data Preparation
# 1. Load the dataset from the "armut_data.csv" file.

import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


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


# ### Generating Association Rules
# 1. Create a pivot table representing the purchased services as columns and baskets (CartID) as rows. The entries in
# this table should indicate whether a service was purchased in a particular basket.

cart_df = df.pivot_table(index="CardID", columns="Services", values="UserId")
cart_df = cart_df.applymap(lambda x: 1 if x != 0 else 0)


# ### Generate Association Rules
# 1. Use Apriori algorithm to discover association rules among the purchased services.
# 2. Filter the rules based on desired support and confidence levels.

associations = apriori(cart_df, min_support=0.01, use_colnames=True)

associations.sort_values("support", ascending=False)

rules = association_rules(urun_birliktelikleri_df,
                          metric="support",
                          min_threshold=0.01)

rules.sort_values("lift", ascending=False)



# ### Generate Recommendations
# 1. Implement the `arl_recommender` function to recommend services to customers based on their previous purchases.
# 2. Provide recommendations to customers who recently purchased a specific service (e.g., "2_0").