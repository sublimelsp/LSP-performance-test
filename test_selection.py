import sublime
import timeit


def test_selection() -> str:

    sel = sublime.Selection(1)
    sel.add(sublime.Region(1, 2))

    def test_len():
        return sel[0] if len(sel) else None

    def test_trycatch():
        try:
            return sel[0]
        except Exception:
            return None

    repeat = 100000
    times = timeit.repeat(test_trycatch, repeat=3, number=repeat)
    return 'Best of {}: {} usec.'.format(repeat, min(times))

# 0.26699970833396947 usec.
# 0.4004749166670081 usec.
