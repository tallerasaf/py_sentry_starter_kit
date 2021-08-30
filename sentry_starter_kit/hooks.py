import sys
from queue import Empty as QEmpty
from typing import Any, Dict, Optional

import system_data
from .better_trace_back import get_better_trace_back_from_hint
from .consts import SentryConsts
from .utils import discard_event_before_send


def _before_send(event: Dict[str, Any], hint: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    try:
        exc_info = hint[SentryConsts.HINT_EXC_INFO] if SentryConsts.HINT_EXC_INFO in hint else sys.exc_info()
        exc_type, exc_value, tb = exc_info
        if exc_type is not None and exc_type is not QEmpty:
            event.setdefault(SentryConsts.CONTEXT, {})[SentryConsts.BETTER_EXCEPTIONS_TRACEBACK] = {
                '': get_better_trace_back_from_hint(exc_info)
            }
        # Dynamic Contexts
        event.setdefault(SentryConsts.CONTEXT, {})[SentryConsts.SYSTEM_DATA] = {
            SentryConsts.DISK: system_data.get_disk_free_space(),
            SentryConsts.CPU: system_data.get_cpu(),
            SentryConsts.MEMORY: system_data.get_ram_none_k8s(),
        }
        event = discard_event_before_send(event)
    except Exception:  # noqa
        pass
    return event
