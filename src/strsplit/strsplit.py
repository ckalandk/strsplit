from typing import Callable, Optional, Union
from .splitter import Splitter, SplitByStr
from .iterator import SplitIter


def split(text: str, splitter: Union[Splitter, str], predicate: Optional[Callable[[str], bool]] = None) -> SplitIter:
    if isinstance(splitter, str):
        s: Splitter = SplitByStr(splitter)
        return SplitIter(s, text, predicate)
    return SplitIter(splitter, text, predicate)
