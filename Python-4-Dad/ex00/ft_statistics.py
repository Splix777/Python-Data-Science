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
    vc = list(args)
    try:
        statistics_available = {
            "mean": sum(vc) / len(vc),
            "median": (
                vc[len(vc) // 2]
                if len(vc) % 2
                else (vc[len(vc) // 2] + vc[len(vc) // 2 - 1]) / 2
            ),
            "quartile": (vc[len(vc) // 4], vc[len(vc) // 4 * 3]),
            "var": sum((x - sum(vc) / len(vc)) ** 2 for x in vc) / len(vc),
            "std": (
                    (sum((x - sum(vc) / len(vc)) ** 2 for x in vc) / len(vc))
                    ** 0.5
            ),
        }
    except ZeroDivisionError:
        print("ERROR")
        return

    for value in kwargs.values():
        if value not in statistics_available:
            print("ERROR")
        else:
            print(f"{value}: {statistics_available[value]}")
    return


def main(*args: any, **kwargs):
    """
    Calculates statistics based on the given arguments.

    Args:
        *args: Numeric values to calculate statistics on.
        **kwargs: Additional keyword arguments for specifying
        the type of statistics to calculate.

    Returns:
        None
    """
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
