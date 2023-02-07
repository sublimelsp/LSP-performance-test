from .test_completions import test_format_completions
import sublime
import sublime_plugin


TESTS = [
    test_format_completions,
]


class LspSelectPerformanceTestCommand(sublime_plugin.WindowCommand):
    def run(self) -> None:
        self.window.show_quick_panel([test.__name__ for test in TESTS], on_select=self._on_select)

    def _on_select(self, index: int) -> None:
        if index == -1:
            return
        result = TESTS[index]()
        sublime.message_dialog(result)
