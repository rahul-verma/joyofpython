import platform


def is_windows_os():
    return platform.system() == 'Windows'