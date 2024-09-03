import json
import os
import sublime
import tarfile
import timeit

__dirname__ = os.path.dirname(os.path.realpath(__file__))


def load_completions_payload():
    with tarfile.open(os.path.join(__dirname__, 'files', 'completions-response.json.tar.gz'), fileobj=None) as tar:
        file = tar.getmember('completions-response.json')
        fileobj = tar.extractfile(file)
        if fileobj:
            return fileobj.read().decode('utf-8')


def test_json_parsing() -> str:
    completions_payload = load_completions_payload()
    assert completions_payload, 'Payload must not be empty'
    completions_payload_json = json.loads(completions_payload)

    def json_dumps() -> None:
        json.dumps(completions_payload_json['items'], ensure_ascii=True, check_circular=False, separators=(',', ':'))

    def json_loads() -> None:
        json.loads(completions_payload)

    def encode_value() -> None:
        sublime.encode_value(completions_payload_json['items'])

    def decode_value() -> None:
        sublime.decode_value(completions_payload)

    repeat = 3
    tests = [
        json_dumps,
        json_loads,
        encode_value,
        decode_value,
    ]
    lines = []
    for test in tests:
        times = timeit.repeat(test, repeat=repeat, number=1)
        lines.append('{}: {}s'.format(test.__name__, min(times)))
    return '\n\n'.join(lines)
