#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# dataset: https://ourworldindata.org/from-1-90-to-2-15-a-day-the-updated-international-poverty-line
dataset = pd.read_csv("poverty-explorer-2011-vs-2017-ppp.csv")

#%%
brazil_data = dataset[dataset['Entity'] == 'Brazil']
brazil_data = brazil_data[['Share of population below $1 a day (2017 prices)',
                           'Share of population below $2.15 a day (2017 prices)',
                           'Share of population below $3.65 a day (2017 prices)',
                           'Share of population below $6.85 a day (2017 prices)',
                           'Mean income or consumption per day (2017 prices)', 'Year']]

#%%
sns.set_palette("flare")

fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0.2, wspace=0)
axes = gs.subplots( sharex=True, sharey=True)

sns.lineplot(ax=axes[0, 0], data=dataset[dataset['Entity'] == 'Brazil'], x='Year', y='Share of population below $1 a day (2017 prices)')
sns.lineplot(ax=axes[0, 0], data=dataset[dataset['Entity'] == 'Brazil'], x='Year', y='Share of population below $2.15 a day (2017 prices)')
sns.lineplot(ax=axes[0, 0], data=dataset[dataset['Entity'] == 'Brazil'], x='Year', y='Share of population below $3.65 a day (2017 prices)')
sns.lineplot(ax=axes[0, 0], data=dataset[dataset['Entity'] == 'Brazil'], x='Year', y='Share of population below $6.85 a day (2017 prices)')
axes[0, 0].set(ylabel="% of pop.")
axes[0, 0].set_title("Brasil")

sns.lineplot(ax=axes[0, 1], data=dataset[dataset['Entity'] == 'Argentina - urban'], x='Year', y='Share of population below $1 a day (2017 prices)')
sns.lineplot(ax=axes[0, 1], data=dataset[dataset['Entity'] == 'Argentina - urban'], x='Year', y='Share of population below $2.15 a day (2017 prices)')
sns.lineplot(ax=axes[0, 1], data=dataset[dataset['Entity'] == 'Argentina - urban'], x='Year', y='Share of population below $3.65 a day (2017 prices)')
sns.lineplot(ax=axes[0, 1], data=dataset[dataset['Entity'] == 'Argentina - urban'], x='Year', y='Share of population below $6.85 a day (2017 prices)')
axes[0, 1].set(ylabel="% of pop.")
axes[0, 1].set_title("Argentina")


sns.lineplot(ax=axes[1, 0], data=dataset[dataset['Entity'] == 'Chile'], x='Year', y='Share of population below $1 a day (2017 prices)')
sns.lineplot(ax=axes[1, 0], data=dataset[dataset['Entity'] == 'Chile'], x='Year', y='Share of population below $2.15 a day (2017 prices)')
sns.lineplot(ax=axes[1, 0], data=dataset[dataset['Entity'] == 'Chile'], x='Year', y='Share of population below $3.65 a day (2017 prices)')
sns.lineplot(ax=axes[1, 0], data=dataset[dataset['Entity'] == 'Chile'], x='Year', y='Share of population below $6.85 a day (2017 prices)')
axes[1, 0].set(ylabel="% of pop.")
axes[1, 0].set_title("Chile")


sns.lineplot(ax=axes[1, 1], data=dataset[dataset['Entity'] == 'Bolivia'], x='Year', y='Share of population below $1 a day (2017 prices)', label='$1')
sns.lineplot(ax=axes[1, 1], data=dataset[dataset['Entity'] == 'Bolivia'], x='Year', y='Share of population below $2.15 a day (2017 prices)', label='$2.15')
sns.lineplot(ax=axes[1, 1], data=dataset[dataset['Entity'] == 'Bolivia'], x='Year', y='Share of population below $3.65 a day (2017 prices)', label='$3.65')
sns.lineplot(ax=axes[1, 1], data=dataset[dataset['Entity'] == 'Bolivia'], x='Year', y='Share of population below $6.85 a day (2017 prices)', label='$6.85')
axes[1, 1].set(ylabel="% of pop.")
axes[1, 1].set_title("Bolívia")

axes[1,1].legend(loc="upper left", bbox_to_anchor=(0, 1))

plt.show()
#%%
fig.savefig("perc of population below property line")
