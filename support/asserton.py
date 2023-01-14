from support.error_messages import ErrorMessages


class Assertion:
    def assertion_equal(expected, actual):
        assert expected == actual, ErrorMessages.ASSERTION_EQUIAL.format(expected, actual)


