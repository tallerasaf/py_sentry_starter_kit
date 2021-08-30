from typing import Any, Dict, Optional

import sentry_sdk

from .consts import SentryConsts, SentryLoggers, SentryProjects

EVENT_DISCARDING_CHECKS = [
    lambda event: event[SentryConsts.TAGS][SentryConsts.APPLICATION] == SentryProjects.TEST and event[
        SentryConsts.LOGGER] != SentryLoggers.TEST_LOGGER
]


def set_tags(tags: Dict[str, Any]) -> None:
    for key, value in tags.items():
        sentry_sdk.set_tag(key, value)


def discard_event_before_send(event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if should_discard_event(event):
        return None
    return event


def should_discard_event(event: Dict[str, Any]) -> bool:
    return any([
        check(event)
        for check in EVENT_DISCARDING_CHECKS
    ])
