import sys
import traceback
from types import TracebackType
from typing import List, Optional, Tuple

import better_exceptions
from loguru import logger as Log


def print_and_log_better_trace_back(msg: str) -> None:
    trace = get_better_trace_back()
    print(msg)
    print(trace)
    Log.error(f'{msg} /n {trace}.')


def print_and_log_warning_better_trace_back(msg: str) -> None:
    trace = get_better_trace_back()
    print(msg)
    print(trace)
    Log.warning(f'{msg} /n {trace}.')


def print_better_trace_back(msg: Optional[str] = None) -> None:
    if msg:
        print(msg)
    print(get_better_trace_back())


def get_better_trace_back() -> str:
    normal_trace = traceback.format_exc()
    # noinspection PyBroadException
    try:
        return better_trace_back_format_exc()
    except Exception:
        return normal_trace


def better_trace_back_format_exc() -> str:
    return ''.join(better_exceptions.format_exception(*sys.exc_info()))


def get_better_trace_back_from_hint(exc_info: Tuple[type, Exception, TracebackType]) -> str:
    return ''.join(_get_better_trace_back_raw(exc_info))


def _get_better_trace_back_raw(exc_info: Tuple[type, Exception, TracebackType]) -> List[str]:
    normal_trace = traceback.format_exception(*exc_info)
    # noinspection PyBroadException
    try:
        return better_exceptions.format_exception(*exc_info)
    except Exception:
        return normal_trace
