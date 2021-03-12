import os


# def load_csv_file(csv_file: Text) -> List[Dict]:
#     """ load csv file and check file content format
#
#     Args:
#         csv_file (str): csv file path, csv file content is like below:
#
#     Returns:
#         list: list of parameters, each parameter is in dict format
#
#     Examples:
#         >>> cat csv_file
#         username,password
#         test1,111111
#         test2,222222
#         test3,333333
#
#         >>> load_csv_file(csv_file)
#         [
#             {'username': 'test1', 'password': '111111'},
#             {'username': 'test2', 'password': '222222'},
#             {'username': 'test3', 'password': '333333'}
#         ]
#
#     """
#     if not os.path.isabs(csv_file):
#         global project_meta
#         if project_meta is None:
#             raise exceptions.MyBaseFailure("load_project_meta() has not been called!")
#
#         # make compatible with Windows/Linux
#         csv_file = os.path.join(project_meta.RootDir, *csv_file.split("/"))
#
#     if not os.path.isfile(csv_file):
#         # file path not exist
#         raise exceptions.CSVNotFound(csv_file)
#
#     csv_content_list = []
#
#     with open(csv_file, encoding="utf-8") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             csv_content_list.append(row)
#
#     return csv_content_list
from typing import Dict, List, Text

from httprunner import utils, exceptions, loader
from httprunner.parser import dolloar_regex_compile, variable_regex_compile, parse_data
import os

def regex_findall_variables(raw_string):
    """ extract all variable names from content, which is in format $variable

    Args:
        raw_string (str): string content

    Returns:
        list: variables list extracted from string content

    Examples:
        >>> regex_findall_variables("$variable")
        ["variable"]

        >>> regex_findall_variables("/blog/$postid")
        ["postid"]

        >>> regex_findall_variables("/$var1/$var2")
        ["var1", "var2"]

        >>> regex_findall_variables("abc")
        []

    """
    try:
        match_start_position = raw_string.index("$", 0)
    except ValueError:
        return []

    vars_list = []
    while match_start_position < len(raw_string):

        # Notice: notation priority
        # $$ > $var

        # search $$
        dollar_match = dolloar_regex_compile.match(raw_string, match_start_position)
        if dollar_match:
            match_start_position = dollar_match.end()
            continue

        # search variable like ${var} or $var
        var_match = variable_regex_compile.match(raw_string, match_start_position)
        if var_match:
            var_name = var_match.group(1) or var_match.group(2)
            vars_list.append(var_name)
            match_start_position = var_match.end()
            continue

        curr_position = match_start_position
        try:
            # find next $ location
            match_start_position = raw_string.index("$", curr_position + 1)
        except ValueError:
            # break while loop
            break

    return vars_list
str1 = """{
                        "isOverprint": "0",
                        "ticketNameId": "${gen_ticket_id($ticketNameCode)}",
                        "ticketNameCode": "01008",
                        "ticketName": "${gen_ticket_name($ticketNameCode)}",
                        "planNum": "1",
                        "unitMeasure": "${gen_ticket_unit_measure($ticketNameCode)}",
                        "copies": "${gen_ticket_copies($ticketNameCode)}",
                        "printName": "",
                        "printId": "",
                        "linker": "majun",
                        "linkerPhone": "13821503367",
                        "year": "$year",
                        "remark": "测试",
                        "quarter": "$quarter",
                        "agencyId": "${gen_ticket_agency_id($agency_code)}",
                        "agencyName": "${gen_ticket_agency_name($agency_code)}",
                        "agencyCode": "$bagency_code",
                        "planType": "0",
                        "dataSource": "0",
                        "auditTask": {"bizTypeCode": "auditTask"},
                    }"""
ls = regex_findall_variables(str1)
print(ls)


def parse_parameters(parameters: Dict,) -> List[Dict]:
    """ parse parameters and generate cartesian product.

    Args:
        parameters (Dict) parameters: parameter name and value mapping
            parameter value may be in three types:
                (1) data list, e.g. ["iOS/10.1", "iOS/10.2", "iOS/10.3"]
                (2) call built-in parameterize function, "${parameterize(account.csv)}"
                (3) call custom function in debugtalk.py, "${gen_app_version()}"

    Returns:
        list: cartesian product list

    Examples:
        >>> parameters = {
            "user_agent": ["iOS/10.1", "iOS/10.2", "iOS/10.3"],
            "username-password": "${parameterize(account.csv)}",
            "app_version": "${gen_app_version()}",
        }
        >>> parse_parameters(parameters)

    """
    parsed_parameters_list: List[List[Dict]] = []

    # load project_meta functions
    project_meta = loader.load_project_meta(os.getcwd())
    functions_mapping = project_meta.functions

    for parameter_name, parameter_content in parameters.items():
        parameter_name_list = parameter_name.split("-")

        if isinstance(parameter_content, List):
            # (1) data list
            # e.g. {"app_version": ["2.8.5", "2.8.6"]}
            #       => [{"app_version": "2.8.5", "app_version": "2.8.6"}]
            # e.g. {"username-password": [["user1", "111111"], ["test2", "222222"]}
            #       => [{"username": "user1", "password": "111111"}, {"username": "user2", "password": "222222"}]
            parameter_content_list: List[Dict] = []
            for parameter_item in parameter_content:
                if not isinstance(parameter_item, (list, tuple)):
                    # "2.8.5" => ["2.8.5"]
                    parameter_item = [parameter_item]

                # ["app_version"], ["2.8.5"] => {"app_version": "2.8.5"}
                # ["username", "password"], ["user1", "111111"] => {"username": "user1", "password": "111111"}
                parameter_content_dict = dict(zip(parameter_name_list, parameter_item))
                parameter_content_list.append(parameter_content_dict)

        elif isinstance(parameter_content, Text):
            # (2) & (3)
            parsed_parameter_content: List = parse_data(
                parameter_content, {}, functions_mapping
            )
            if not isinstance(parsed_parameter_content, List):
                raise exceptions.ParamsError(
                    f"parameters content should be in List type, got {parsed_parameter_content} for {parameter_content}"
                )
            parsed_parameter_content=parameter_content
            parameter_content_list: List[Dict] = []
            for parameter_item in parsed_parameter_content:
                if isinstance(parameter_item, Dict):
                    # get subset by parameter name
                    # {"app_version": "${gen_app_version()}"}
                    # gen_app_version() => [{'app_version': '2.8.5'}, {'app_version': '2.8.6'}]
                    # {"username-password": "${get_account()}"}
                    # get_account() => [
                    #       {"username": "user1", "password": "111111"},
                    #       {"username": "user2", "password": "222222"}
                    # ]
                    parameter_dict: Dict = {
                        key: parameter_item[key] for key in parameter_name_list
                    }
                elif isinstance(parameter_item, (List, tuple)):
                    if len(parameter_name_list) == len(parameter_item):
                        # {"username-password": "${get_account()}"}
                        # get_account() => [("user1", "111111"), ("user2", "222222")]
                        parameter_dict = dict(zip(parameter_name_list, parameter_item))
                    else:
                        raise exceptions.ParamsError(
                            f"parameter names length are not equal to value length.\n"
                            f"parameter names: {parameter_name_list}\n"
                            f"parameter values: {parameter_item}"
                        )
                elif len(parameter_name_list) == 1:
                    # {"user_agent": "${get_user_agent()}"}
                    # get_user_agent() => ["iOS/10.1", "iOS/10.2"]
                    # parameter_dict will get: {"user_agent": "iOS/10.1", "user_agent": "iOS/10.2"}
                    parameter_dict = {parameter_name_list[0]: parameter_item}
                else:
                    raise exceptions.ParamsError(
                        f"Invalid parameter names and values:\n"
                        f"parameter names: {parameter_name_list}\n"
                        f"parameter values: {parameter_item}"
                    )

                parameter_content_list.append(parameter_dict)

        else:
            raise exceptions.ParamsError(
                f"parameter content should be List or Text(variables or functions call), got {parameter_content}"
            )

        parsed_parameters_list.append(parameter_content_list)

    return utils.gen_cartesian_product(*parsed_parameters_list)



parameters = {

            "username-passwd": "${get_data()}",

        }
re = parse_parameters(parameters)
print(re)