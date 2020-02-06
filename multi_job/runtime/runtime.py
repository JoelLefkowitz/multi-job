from operator import itemgetter
from typing import List, Mapping

import sys; sys.path.append('..')
from models.processes import Process
from utils.colours import blue, green
from utils.emojis import MUSHROOM, TOPHAT, ZAP


def run(processes: List[Process], options: Mapping[str, bool]) -> None:
    quiet, silent, check, verbose = itemgetter("quiet", "silent", "check", "verbose")(
        options
    )

    if not (quiet or silent):
        print(ZAP + blue(" Multi Job ") + ZAP + "\nPlan:")

        for process in processes:
            print(green(process.show(verbose)))

    if check:
        return

    for process in processes:
        if not (quiet or silent):
            print(blue("Running: ") + process.show(verbose))

        output = process.trigger()
        if not silent:
            print(output)
