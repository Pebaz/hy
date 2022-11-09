import io
from typing import Optional, Tuple
import codecs


def hy_encode(input, errors='strict') -> Tuple[object, int]:
    return print(hy_encode), 0


def hy_decode(input: object, errors: str = 'strict') -> Tuple[object, int]:
    return print(hy_decode), 0


class HyIncrementalEncoder(codecs.IncrementalEncoder):
    def __init__(self, errors='strict'):
        super().__init__(errors)

    def encode(self, object, final=False) -> object:
        if final:
            "Last time encode() will be called"

    def reset(self) -> None:
        "Suggested to call self.encode(None, final=True) to reset"

    def getstate(self) -> int:
        return 0

    def setstate(self, state: int) -> None:
        ...


class HyIncrementalDecoder(codecs.IncrementalDecoder):
    def __init__(self, errors='strict'):
        super().__init__(errors)

    def decode(self, object, final=False) -> object:
        if final:
            "Last time decode() will be called"

    def reset(self) -> None:
        ...

    def getstate(self) -> Tuple[object, int]:
        return None, 0

    def setstate(self, state: int) -> None:
        ...


class HyStreamWriter(codecs.StreamWriter):
    def __init__(self, stream, errors='strict'):
        super().__init__(stream, errors)

    def write(self, object) -> None:
        "Write to self.stream"

    def writelines(self, list) -> None:
        for line in list:
            self.write(line)

    def reset(self) -> None:
        ...

    # ? https://docs.python.org/3/library/codecs.html#codecs.StreamWriter
    # ? In addition to the above methods, the StreamWriter must also inherit all
    # ? other methods and attributes from the underlying stream.


class HyStreamReader(codecs.StreamReader):
    def __init__(self, stream, errors='strict'):
        super().__init__(stream, errors)

    def read(self, size=-1, chars=-1, firstline=False) -> object:
        ...

    def readline(self, size=None, keepends=True) -> object:
        ...

    def readlines(self, sizehint=None, keepends=True) -> list[object]:
        ...

    def reset(self):
        ...


HY_CODEC_INFO = codecs.CodecInfo(
    name='hy',
    encode=hy_encode,
    decode=hy_decode,
    incrementalencoder=HyIncrementalEncoder,
    incrementaldecoder=HyIncrementalDecoder,
    streamwriter=HyStreamWriter,
    streamreader=HyStreamReader
)


def search_function(codec_name: str) -> Optional[codecs.CodecInfo]:
    if codec_name == 'hy':
        return HY_CODEC_INFO


codecs.register(search_function)

print(codecs.lookup('hy'))
# codecs.decode(io.BytesIO(b'Hello World!'), 'hy')
