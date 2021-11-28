import sys


def merge_dicts(first, second, third):
    version = sys.version_info
    if version.major >= 3 and version.minor >= 5:
        merged_dict = {
            **first,
            **second,
            **third
        }
    else:
        merged_dict = merge_dicts(first, second)
        merged_dict = merge_dicts(merged_dict, third)
    return merged_dict
