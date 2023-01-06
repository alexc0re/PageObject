from support.error_messages import ErrorMessages


class Assertion:

    @staticmethod
    def assertion_equal(expected, actual):
        assert expected == actual, ErrorMessages.ASSERTION_EQUIAL.format(expected, actual)


