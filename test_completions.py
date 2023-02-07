from LSP.plugin.core.views import format_completion
import json
import os
import tarfile
import timeit

__dirname__ = os.path.dirname(os.path.realpath(__file__))


def load_completions_payload():
    with tarfile.open(os.path.join(__dirname__, 'files', 'completions-response.json.tar.gz'), fileobj=None) as tar:
        file = tar.getmember('completions-response.json')
        fileobj = tar.extractfile(file)
        if fileobj:
            return json.loads(fileobj.read().decode('utf-8'))


def test_format_completions() -> str:
    completions_payload = load_completions_payload()
    assert completions_payload, 'Payload must not be empty'

    def test() -> None:
        items = completions_payload['items']
        for i, c in enumerate(items):
            format_completion(c, i, can_resolve_completion_items=True, session_name='LSP-foo', view_id=1)

    repeat = 3
    times = timeit.repeat(test, repeat=3, number=1)
    return 'Best of {}: {} usec. All times: {}'.format(repeat, min(times), times)
