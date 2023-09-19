from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def extract(data, country):
    """
    Extract the population data of a country from the dataset
    """
    country_data = data[data["country"] == country]
    country_data = country_data.loc[:, "1800":"2050"]
    years = country_data.columns[1:].astype(int)
    population = country_data.values[0, 1:].astype(str)
    numeric_population = np.array([float(p[:-1]) if p[-1] == 'k'
                                   else float(p[:-1]) * 1000
                                   for p in population])
    numeric_population = np.round(numeric_population).astype(int)
    return years, numeric_population


def main():
    """
    Load the life expectancy dataset and plot the life expectancy of Malaysia
    and Singapore
    """
    try:
        data = load("population_total.csv")
        years_malaysia, pop_malaysia = extract(data, "Malaysia")
        years_singapore, pop_singapore = extract(data, "Singapore")

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.plot(years_malaysia, pop_malaysia, label="Malaysia")
        plt.plot(years_singapore, pop_singapore, label="Singapore")
        plt.yticks(range(0, max(pop_malaysia), 10000))
        plt.legend()
        plt.savefig("population_total.jpg")
    except Exception as err:
        print(err)
        return


if __name__ == "__main__":
    main()
