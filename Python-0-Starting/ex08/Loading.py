# Loading.py


def ft_tqdm(
        lst: range,
        bar_width: int = 40,
        bar_char: str = '█',
        bar_end: str = '█'
) -> None:
    """
    This function is a clone of the tqdm library.
    It takes a range and prints a progress bar.

    Args:
        lst (range): A range of numbers.
        bar_width (int): The width of the progress bar.
        bar_char (str): The character used to fill the progress bar.
        bar_end (str): The character used to end the progress bar.

    Returns:
        None
    """
    total = len(lst)

    for i, _ in enumerate(lst):
        progress = (i + 1) / total
        progress_width = int(progress * bar_width)
        bar = bar_char * progress_width + bar_end + ' ' * (bar_width - progress_width)

        print(f'\r{progress:.0%}|{bar}| {i + 1}/{total}', end='', flush=True)

        yield i

    print()
