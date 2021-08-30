import os

import better_exceptions
import sentry_sdk
from loguru import logger as Log
from sentry_sdk.integrations.logging import ignore_logger

from .consts import PROJECT_TO_DSN_MAPPING, SentryConsts
from .hooks import _before_send
from .singleton import MetaSingleton
from .utils import set_tags


class SentryInit(metaclass=MetaSingleton):
    def __init__(self, project_type: str) -> None:
        try:
            Log.info(f'Starting to initialize Sentry for "{project_type}".')
            better_exceptions.hook()
            super().__init__()
            self.project_type = project_type
            self._sdk_init()
            self._add_additional_info()
            Log.info(f'Sentry has been initialized successfully for "{project_type}".')
        except Exception:  # noqa
            Log.error(f'Failed to initialize Sentry for "{project_type}".')

    @property
    def sentry_dsn(self) -> str:
        return PROJECT_TO_DSN_MAPPING.get(self.project_type)

    def _sdk_init(self) -> None:
        ignore_logger('fake_logger.connection.Connection')
        sentry_sdk.init(
            dsn=self.sentry_dsn,
            release='release-1.2.3',
            environment='PROD',
            traces_sample_rate=SentryConsts.TRANSACTIONS_CAPTURE_RATE,
            debug=SentryConsts.IS_IN_DEBUG_MODE,
            attach_stacktrace=SentryConsts.SHOULD_ATTACH_STACKTRACE,
            with_locals=SentryConsts.SHOULD_ATTACH_LOCALS,
            send_default_pii=SentryConsts.SEND_DEFAULT_PII,
            request_bodies=SentryConsts.REQUEST_BODIES,
            before_send=_before_send,
        )

    @staticmethod
    def _add_additional_info() -> None:
        if SentryConsts.USER_NAME in os.environ:
            sentry_sdk.set_user(
                {SentryConsts.USER_NAME: os.getenv(SentryConsts.USER_NAME, SentryConsts.UNKNOWN)})
        # None Dynamic Contexts
        host_data_context = {
            SentryConsts.HOST_IP: os.getenv(SentryConsts.HOST_IP, SentryConsts.UNKNOWN),
        }
        if SentryConsts.INSTANCE_ID in os.environ:
            host_data_context[SentryConsts.INSTANCE_ID] = os.getenv(SentryConsts.INSTANCE_ID,
                                                                    SentryConsts.UNKNOWN)
        sentry_sdk.set_context(SentryConsts.HOST_DATA, host_data_context)
        # Searchable Tags
        set_tags({
            SentryConsts.APPLICATION: None or SentryConsts.UNKNOWN,
            SentryConsts.COMPUTER_NAME: None or SentryConsts.UNKNOWN,
        })
