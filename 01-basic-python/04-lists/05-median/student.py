# Write your code here
def median(ns):
    ns.sort()
    if len(ns) % 2:
        return ns[len(ns) // 2]
    else:
        return (ns[len(ns) // 2] + ns[len(ns) // 2 - 1]) / 2
    