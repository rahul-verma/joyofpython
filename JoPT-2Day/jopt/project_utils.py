import os


def get_root_dir():
    my_dir = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(my_dir, "..")


def get_output_file_path(file_name):
    return os.path.join(get_root_dir(), "output", file_name)


def get_input_file_path(file_name):
    return os.path.join(get_root_dir(), "input", file_name)


def get_full_driver_path(driver_name):
    return os.path.join(get_root_dir(), "drivers", driver_name)


def get_config_file_path():
    return os.path.join(get_root_dir(), "config", "config.json")
