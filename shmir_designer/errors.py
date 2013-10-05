#usr/bin/env python
import logging

error = 'insert only one siRNA sequence or both strands of one' \
'siRNA at a time; check if both stands are in 5-3 orientation'
len_error = "to long or to short"
patt_error = 'sequence can contain only {actgu} letters'


class InputException(Exception):
    """Exception error class for incorrect input"""

    def __init__(self, message=None):
        self.message = message
        logging.error('%s: %s', self.__class__.__name__, self.message)
        super(InputException, self).__init__(self.message)