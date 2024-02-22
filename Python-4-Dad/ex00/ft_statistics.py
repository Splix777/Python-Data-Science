# statistics.py

def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Takes in *args a quantity of unknown numbers and makes
    the Mean, Median, Quartile (25% and 75%), Standard Deviation
    and Variance according to the **kwargs passed.
    """
    if args is None:
        print("ERROR")
        return
    vec = list(args)
    try:
        statistics_available = {
            "mean": sum(vec) / len(vec),
            "median": (
                vec[len(vec) // 2]
                if len(vec) % 2
                else (vec[len(vec) // 2] + vec[len(vec) // 2 - 1]) / 2
            ),
            "quartile": (vec[len(vec) // 4], vec[len(vec) // 4 * 3]),
            "var": sum((x - sum(vec) / len(vec)) ** 2 for x in vec) / len(vec),
            "std": (
                (sum((x - sum(vec) / len(vec)) ** 2 for x in vec) / len(vec))
                ** 0.5
            ),
        }
    except ZeroDivisionError:
        print("ERROR")
        return

    for value in kwargs.values():
        if value not in statistics_available:
            print("ERROR")
            return
        else:
            print(f"{value}: {statistics_available[value]}")
    return


def main():
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean",
                  tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std",
                  world="var")

    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
