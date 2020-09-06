import idom


def increment(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


@idom.element
def Counter(initial_count):
    count, set_count = idom.hooks.use_state(initial_count)
    return idom.html.div(
        f"Count: {count}",
        idom.html.button({"onClick": lambda event: set_count(initial_count)}, "Reset"),
        idom.html.button({"onClick": lambda event: set_count(increment)}, "+"),
        idom.html.button({"onClick": lambda event: set_count(decrement)}, "-"),
    )


display(Counter, 0)