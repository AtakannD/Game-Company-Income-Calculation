*Calculation of Customer Income with Rule-Based Classification*

1. Business Problem

A game company wants to create new customer definitions based on level by using some features of its customers, 
create segments according to these new customer definitions and estimate how much the new customers can earn 
according to these segments.

For instance, it is desired to determine how much a 25-year-old male user from Turkey, who is an IOS user, can 
earn on average.

2. Story of Dataset

Persona.csv dataset contains the prices of the products sold by an international game company and some 
demographic information of the users who buy these products. The dataset consists of records created in each 
sales transaction. This means that the table is not deduplicated. In other words, a user with certain 
demographic characteristics may have made more than one purchase.

For instance:
User 1 is male from brazil and he is 17 years old. He bought this game for 39 units and he uses android.
User 2 is male from brazil and he is 17 years old. He bought this game for 39 units and he uses android too. 
But this users are totally different people.

3. Variables

PRICE – Customer's spending amount
SOURCE – The type of device the customer is connecting to
SEX – Gender of the client
COUNTRY – Country of the customer
AGE – Age of the customer


Task 1: Answer the Following Questions

Question 1: Read the persona.csv file and show the general information about the dataset.
Question 2: How many unique SOURCE are there? What are their frequencies?
Question 3: How many unique PRICEs are there?
Question 4: How many sales were made from which PRICE?
Question 5: How many sales were made from which country?
Question 6: How much was earned in total from sales by country?
Question 7: What are the sales numbers by SOURCE types?
Question 8: What are the PRICE averages by country?
Question 9: What are the PRICE averages according to SOURCEs?
Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?


Task 2: What is the average income broken down by COUNTRY, SOURCE, SEX, AGE?


Task 3: Sort the output by PRICE.


Task 4: Convert the names in the index to variable names.


Task 5: Convert AGE variable to categorical variable and add it to agg_df.


Task 6: Identify new level-based customers.


Task 7: Segment new customers.


Task 8: Classify new customers and estimate how much income they can provide.

For instance; 
• What segment does a 33-year-old Turkish woman using ANDROID belong to and how much income is expected to 
generate on average for the company?
• What segment does a 35-year-old French woman using IOS belong to and how much income is expected to 
generate on average for the company?
