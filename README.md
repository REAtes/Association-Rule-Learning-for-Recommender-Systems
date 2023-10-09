# Association Rule Learning for Recommender Systems

## Business Problem

Armut, Turkey's largest online service platform, connects service providers with customers looking for services such as cleaning, renovation, and transportation. Armut aims to create a product recommendation system using Association Rule Learning based on customer service usage and categories.

## Dataset

The dataset consists of customer service usage records, including information about the services purchased, their respective categories, and the date and time of the service.

- `UserId`: Customer ID
- `ServiceId`: Anonymized IDs representing different services. (e.g., Service ID 9_4 may refer to upholstery cleaning in one category, and Service ID 2_4 may refer to furniture assembly in another category.)
- `CategoryId`: Anonymized category IDs (e.g., Cleaning, Transportation, Renovation)
- `CreateDate`: Date of service purchase

## Task

### Data Preparation
1. Load the dataset from the "armut_data.csv" file.

### Create a New Service Identifier
1. Combine the `ServiceId` and `CategoryId` columns using "_" to create a new variable called `Services`.

### Define Shopping Baskets
1. To apply Association Rule Learning, we need to define shopping baskets. In this case, each basket corresponds to the services purchased by a customer within a specific month.
2. Create a new date variable containing only the year and month information.
3. Combine the `UserId` and the new date variable with "_" to create a unique basket identifier called `CartID`.

### Generating Association Rules
1. Create a pivot table representing the purchased services as rows and baskets (CartID) as columns. The entries in this table should indicate whether a service was purchased in a particular basket.

### Generate Association Rules
1. Use Apriori algorithm to discover association rules among the purchased services.
2. Filter the rules based on desired support and confidence levels.

### Generate Recommendations
1. Implement the `arl_recommender` function to recommend services to customers based on their previous purchases.
2. Provide recommendations to customers who recently purchased a specific service (e.g., "2_0").

The recommendations are based on association rules, and the most relevant services are suggested to the customer.

---

**Note:** The code provided is for demonstration purposes. In practice, the dataset and parameters may vary, and additional preprocessing steps and evaluations may be necessary.