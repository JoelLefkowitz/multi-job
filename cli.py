def main(scripts, jobs):
    interface = "Usage:"
    for name, params in [(i.name, i.params) for i in scripts + jobs]:
        interface += (
            f"\n  naval_fate.py {name} {' '.join(sorted([f'[<{i}>]' if params[i] else f'<{i}>' for i in params.keys()]))}"
            + " [--quiet --check]"
        )
    return interface
