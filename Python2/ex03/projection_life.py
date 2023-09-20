from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


def format_ticks(value, _):
    """
    Format the ticks of the x-axis
    """
    return {
        300: "300",
        1000: "1k",
        10000: "10k"
    }[value]


def main():
    """
    Load the life expectancy dataset and plot the life expectancy of Malaysia
    """
    try:
        income_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        income_data = income_data.loc[:, "1900"]
        life_data = load("life_expectancy_years.csv")
        life_data = life_data.loc[:, "1900"]

        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.scatter(income_data, life_data)
        plt.xscale("log")
        plt.xticks([300, 1000, 10000])

        formatter = ScalarFormatter()
        formatter.set_scientific(False)
        plt.gca().xaxis.set_major_formatter(
            plt.FuncFormatter(format_ticks))
        plt.savefig("1900.jpg")
    except Exception as err:
        print(err)
        return


if __name__ == "__main__":
    main()
