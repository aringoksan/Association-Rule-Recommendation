import pandas as pd
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind



pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 500)

control_df = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
test_df = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")
control_df.head()
test_df.head()
control_df.describe().T
test_df.describe().T
control_df.isnull().sum()
test_df.isnull().sum()

merged_df = pd.concat([control_df, test_df], ignore_index=True)
# Formulation of the hypothesis
# There is no statistical difference between maximum bidding and average bidding
# H0: M1 = M2
# H1: M1 != M2
control_df["Purchase"].mean()
test_df["Purchase"].mean()


# Normality assumption control
# Assumption: H0 variable has normal distribution
# Assumption: H1 variable has normal distribution
print(shapiro(control_df["Purchase"]))
print(shapiro(test_df["Purchase"]))

# Homogeneity of variance control
# H0 has homogeneity of variance
# H1 has homogeneity of variance
print(levene(control_df["Purchase"], (test_df["Purchase"])))

# T testing
test_stat, p_value = ttest_ind(control_df["Purchase"], test_df["Purchase"], equal_var=True)
print(p_value)
# Hypothesis can not be denied, there is no statistical difference between two variables since p value is higher than 0.05
