import sys 


def main(scripts, jobs):
    interface = "Usage:"
    exec_path = " ".join(sys.argv[:2])
    for name, params in [(i.name, i.params) for i in scripts + jobs]:
        interface += f"\n {exec_path} {name} {fmt(params)} [--quiet --check]"
    return interface


def fmt(params):
    return " ".join(
        sorted([f"[<{i}>]" if params[i] else f"<{i}>" for i in params.keys()])
    )
