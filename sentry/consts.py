class SentryConsts:
    CONTEXT = 'contexts'
    USER_NAME = 'username'
    UNKNOWN = 'Unknown'
    HOST_IP = 'host_ip'
    INSTANCE_ID = 'instance_id'
    SYSTEM_DATA = 'System Data'
    HOST_DATA = 'Host Data'
    BETTER_EXCEPTIONS_TRACEBACK = 'Better Traceback'
    HINT_EXC_INFO = 'exc_info'
    TRANSACTIONS_CAPTURE_RATE = 1.0  # Capture 100% of transactions for performance monitoring.
    REQUEST_BODIES = 'always'  # SDK will always capture the request body for as long as Sentry can make sense of it.
    IS_IN_DEBUG_MODE = False  # If enabled SDK will print out useful debugging information.
    SHOULD_ATTACH_STACKTRACE = True  # stack traces are being automatically attached to all messages logged.
    SHOULD_ATTACH_LOCALS = True  # When enabled, local variables sent along with stack frames.
    SEND_DEFAULT_PII = True  # Personally identifiable information (PII) is added by active integrations.
    LOGGER = 'logger'
    TAGS = 'tags'
    APPLICATION = 'application'
    THREAD = 'thread'
    CPU = 'cpu'
    MEMORY = 'memory'
    DISK = 'disk'
    COMPUTER_NAME = 'computer_name'
    FILE_NAME = 'file_name'


class SentryLoggers:
    TEST_LOGGER = 'test_logger'


class SentryProjects:
    TEST = 'test_project'
    TEST_1 = 'test_project_1'
    TEST_2 = 'test_project_2'


PROJECT_TO_DSN_MAPPING = {
    SentryProjects.TEST: 'sentry_dsn_url',
    SentryProjects.TEST_1: 'sentry_dsn_url_1',
    SentryProjects.TEST_2: 'sentry_dsn_url_2'
}
