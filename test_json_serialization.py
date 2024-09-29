import json
import orjson
import os
import tarfile
import timeit

__dirname__ = os.path.dirname(os.path.realpath(__file__))


def load_completions_payload():
    with tarfile.open(os.path.join(__dirname__, 'files', 'completions-response.json.tar.gz'), fileobj=None) as tar:
        file = tar.getmember('completions-response.json')
        fileobj = tar.extractfile(file)
        if fileobj:
            return fileobj.read().decode('utf-8')


def test_json_serialization_json() -> str:
    completions_payload = load_completions_payload()
    assert completions_payload, 'Payload must not be empty'

    def test() -> None:
        json.loads(completions_payload)

    repeat = 3
    times = timeit.repeat(test, repeat=repeat, number=1)
    return 'Best of {}: {} usec. All times: {}'.format(repeat, min(times), times)


def test_json_serialization_orjson() -> str:
    completions_payload = load_completions_payload()
    assert completions_payload, 'Payload must not be empty'

    def test() -> None:
        orjson.loads(completions_payload)

    repeat = 3
    times = timeit.repeat(test, repeat=repeat, number=1)
    return 'Best of {}: {} usec. All times: {}'.format(repeat, min(times), times)
