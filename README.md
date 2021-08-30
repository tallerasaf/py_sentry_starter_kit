# **_sentry_starter_kit_**! 🔥

## **sentry_starter_kit is a boilerplate for start using sentry.io fast.!**

### Features:

    1. Add better_exceptions traceback to every error sent to Sentry.
    2. Add real time CPU, MEMORY, DISK to every error sent to Sentry.
    3. Discard the event if he meet certain criteria before sending it to Sentry.
    4. Add additional info to every error sent to Sentry.
    5. Add the recommended settings Sentry. 
    6. Making sure Sentry Init will happen only once.

### Example Usage:

```
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
```

###### ![Sentry Image](https://www.sentry.dev/_assets2/static/default-1a447e1992a4243477b39d5fb03114fb.png)

###### ![Starter Kit Image](https://www.organicsnutrients.com/wp-content/uploads/Starter-Kit-ANG-1.-stran-3.jpg)

## Author:

- [Asaf Taller](https://github.com/tallerasaf)

##### Copyright (C) [2021] [tallerasaf].
