import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(data_path):
    my_data = pd.read_csv(data_path, sep=';')
    return my_data


def data_summary(data):
    main_sum = data.describe()
    return main_sum

def data_visual(data):
    mean = data['Weight'].mean()
    median = data['Weight'].median()
    quantile25 = data['Weight'].quantile(.25)
    quantile75 = data['Weight'].quantile(.75)

    plot = sns.histplot(data["Weight"], kde=True, color="blue", label="Weight")

    plot.axvline(mean, color="y", linestyle='-', label='Mean')
    plot.axvline(median, color="g", linestyle='-', label='Median')
    plot.axvline(quantile25, color="r", linestyle='-', label='25% quantile')
    plot.axvline(quantile75, color="b", linestyle='-', label='75% quantile')
    # Create legend
    plot.legend()

    plt.show()