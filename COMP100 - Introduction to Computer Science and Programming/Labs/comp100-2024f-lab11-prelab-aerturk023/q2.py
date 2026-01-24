def validate_tab_file(file_path, expected_fields, required_pattern):
    
    try:
        with open(file_path, "r") as file:
            is_in = False
            i=0
            for line in file:
                i+=1
                if line.count("\t") + 1 != expected_fields:
                    raise TabFileValidationError(f"File path: {file_path}, Line {i}: Expected {expected_fields} fields, found {line.count('\t')+1}.")
                else:
                    if required_pattern in line:
                        is_in = True
            if not is_in:
                raise TabFileValidationError(f"File path: {file_path}, No field contains required pattern '{required_pattern}'.")
            else:
                return "Tab-delimited file validation passed."
            
    except FileNotFoundError:
        return "File not found."


class TabFileValidationError(Exception):
    pass


                