from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load the life expectancy dataset and plot the life expectancy of Malaysia
    """
    try:
        data = load("life_expectancy_years.csv")
        malaysia = data[data["country"] == "Malaysia"]
        years = malaysia.columns[1:].astype(int)
        life_expectancy = malaysia.values[0, 1:].astype(float)

        plt.title("Malaysia Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.plot(years, life_expectancy)
        plt.savefig("life_expectancy_years.jpg")
    except Exception as err:
        print(err)
        return


if __name__ == "__main__":
    main()
