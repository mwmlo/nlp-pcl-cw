import pandas as pd
from dont_patronize_me import DontPatronizeMe
dpm = DontPatronizeMe('.', 'dontpatronizeme_pcl.tsv')
# This method loads the subtask 1 data
dpm.load_task1()
# which we can then access as a dataframe
df = dpm.train_task1_df

# Load the dev and train set par_id lists
dev_par_ids = pd.read_csv("dev_semeval_parids-labels.csv")["par_id"]
train_par_ids = pd.read_csv("train_semeval_parids-labels.csv")["par_id"]

# Split into dev and train sets
df_par_ids = df["par_id"].astype("Int64")
df_dev = df[df_par_ids.isin(dev_par_ids)].dropna()
df_train = df[df_par_ids.isin(train_par_ids)].dropna()

# Display results
print("Dev Set:", df_dev.shape)
print("Train Set:", df_train.shape)

# Save if needed
df_dev.to_csv("dev_set.csv", index=False)
df_train.to_csv("train_set.csv", index=False)
