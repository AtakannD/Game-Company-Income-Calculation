import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Task 1.1
df = pd.read_csv(r"C:\Users\atakan.dalkiran\PycharmProjects\Game Company Income Calculation\persona.csv")


def check_df(dataframe, head=5):
    """
    This function gives us a first look when we import our dataset.

    Parameters
    ----------
    dataframe: pandas.dataframe
    It is the dataframe from which variable names are to be drawn.
    head: int
    The variable that determines how many values we want to look at first when browsing the data set we have.

    Returns
    -------
    shape: tuple
    it gives us how many rows and how many columns our dataset consists of.
    type: pandas.series
    gives us the datatypes of our variables in our dataset.
    head: pandas.Dataframe
    It gives us the variables and values of our dataset, starting from the 0th index to the number we entered,
    as a dataframe.
    tail: pandas.Dataframe
    Contrary to head, this method counts us down starting from the index at the end.
    isnull().sum(): pandas.series
    It visits the variables in our data set and checks if there are any null values and, gives us the statistics
    of how many of them are in each variable.
    quantile: pandas.dataframe
    It gives the range values of the variables in our data set as a percentage according to the values we entered.

    Examples
    --------
    The output of shape return is given to us as a tuple (5000, 5).
    """
    print("######################### Shape #########################")
    print(dataframe.shape)
    print("\n######################### Type #########################")
    print(dataframe.dtypes)
    print("\n######################## Columns ########################")
    print(dataframe.columns)
    print("\n######################### Head #########################")
    print(dataframe.head(head))
    print("\n######################### Tail #########################")
    print(dataframe.tail(head))
    print("\n######################### NA #########################")
    print(dataframe.isnull().sum())
    print("\n######################### Quantiles #########################")
    print(dataframe.quantile([0, 0.25, 0.5, 0.75, 0.95, 1]).T)


check_df(df)

# Task 1.2
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Task 1.3
df["PRICE"].nunique()

# Task 1.4
df["PRICE"].value_counts()

# Task 1.5
df["COUNTRY"].value_counts()

# Task 1.6
df.groupby("COUNTRY").agg({"PRICE": "count"})

# Task 1.7
df["SOURCE"].value_counts()

# Task 1.8
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# Task 1.9
df.groupby("SOURCE").agg({"PRICE": "mean"})

# Task 1.10
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

# Task 2
df1 = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# Task 3
agg_df = df1.sort_values(by=["PRICE"], ascending=False)

# Task 4
agg_df = agg_df.reset_index()

# Task 5
agg_df["AGE_TH"] = pd.cut(agg_df["AGE"], [14, 18, 23, 29, 36, 48, 70],
                          labels=['14_18', '19_23', '24_29', '30_36', '37_48', '49_70'])

# Task 6
[row for row in agg_df.values]
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" +
                                   row[2].upper() + "_" + row[5] for row in agg_df.values]
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}).sort_values(by=["PRICE"], ascending=False)

# Task 7
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

# Task 8
agg_df = agg_df.reset_index()
new_user = "TUR_ANDROID_FEMALE_30_36"
agg_df[agg_df["customers_level_based"] == new_user]
new_user1 = "FRA_IOS_FEMALE_30_36"
agg_df[agg_df["customers_level_based"] == new_user1]