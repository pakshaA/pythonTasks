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


def read_and_check(welcome_text="", params_count=1, param_names=[], output_type="str"):
    input_list = input(welcome_text+" ").split()
    while len(input_list) < params_count:
        print("Вы ввели слишком малое кол-во параметров. Попробуйте снова.")
        input_list = input(welcome_text).split()

    output_arr = []

    for i in range(params_count):
        curr = input_list[i]
        while True:
            try:
                curr_float = float(curr)
                output_arr.append(curr_float)
                break
            except ValueError:
                curr_param_name = f"Параметр №{i+1}" if len(param_names) == 0 else param_names[i]
                input_curr = input(curr_param_name+f" не является типом {output_type}. Введите его заново: ").split()
                curr = input_curr[0] if len(input_curr) else ""
    return output_arr if params_count > 1 else output_arr[0]
