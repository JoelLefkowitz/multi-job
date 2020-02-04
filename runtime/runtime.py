from operator import itemgetter
from typing import List, Mapping
from models.models import Process
from utils.colours import green, blue
from utils.emojis import ZAP, MUSHROOM, TOPHAT


def run(processes: List[Process], options: Mapping[str, bool]) -> None:
    quiet, silent, check, verbose = itemgetter("quiet", "silent", "check", "verbose")(
        options
    )

    if not (quiet or silent):
        print(ZAP + blue(" Multi Job ") + ZAP + "\nPlan:")

        for process in processes:
            print(green(process.call_repr(verbose)))

    if check:
        return

    for process in processes:
        if not (quiet or silent):
            print(blue("Running: ") + (process.call_repr(verbose)))

        output = process.trigger()
        if not silent:
            print(output)
