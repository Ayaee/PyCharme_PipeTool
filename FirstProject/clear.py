import sys
import six


def do(name):
    """
    Unloads modules starting with "name" + "."

    :param name:
    :return:
    """

    tmp_modules = sys.modules.copy()
    for key, value in six.iteritems(tmp_modules):
        if key.startswith(name + '.'):
            sys.modules.pop(key, None)
            print('popped ' + key)