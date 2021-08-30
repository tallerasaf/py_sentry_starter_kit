import sentry_sdk

from sentry_starter_kit import SentryInit, SentryProjects
from sentry_starter_kit.consts import SentryConsts
from sentry_starter_kit.utils import set_tags


def main():
    SentryInit(project_type=SentryProjects.TEST_1)
    add_additional_info_to_sentry()


def add_additional_info_to_sentry() -> None:
    set_tags({
        SentryConsts.APPLICATION: 'my_application',
        SentryConsts.LOGGER: 'my_logger'
    })
    sentry_sdk.set_user({
        SentryConsts.USER_NAME: 'my_user_name',
    })
    sentry_sdk.set_context('MY Context', {
        SentryConsts.COMPUTER_NAME: 'my_computer_name',
        SentryConsts.HOST_IP: '192.168.1.1',
    })


if __name__ == "__main__":
    main()
