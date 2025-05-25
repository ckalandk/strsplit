from .splitter import Splitter
from typing import Callable, Optional, Iterator


class SplitIter:

    def __init__(self, splitter: Splitter, text: str, Predicate: Optional[Callable[[str], bool]] = None):
        self._splitter = splitter
        self._text = text
        self._predicate: Callable[[str], bool] = \
            Predicate if Predicate is not None else lambda x: False
        if Predicate is not None and not callable(Predicate):
            raise TypeError("Predicate must be a callable function")
        self._start: int = 0
        self._end: int = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self._start >= len(self._text):
            raise StopIteration
        _substr: str = self.__next_substr()
        if self._predicate(_substr):
            return self.__next__()
        return _substr

    def __next_substr(self) -> str:
        if self._splitter.maxsplit == 0:
            _substr = self._text[self._start:]
            self._start = len(self._text)
            return _substr
        self._end, _cap = self._splitter.find(self._text, self._start)
        _substr = self._text[self._start:self._end]
        self._start = _cap
        self._splitter.maxsplit -= 1
        return _substr
