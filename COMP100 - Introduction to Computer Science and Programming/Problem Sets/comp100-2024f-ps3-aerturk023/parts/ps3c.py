from ps3a import decrypt_the_message

def handling_assignments(assignments_path, houses_path, decrypted_assignment_path, updated_assignments_path, updated_houses_path):
    """Function to handle assignments and update house contributions."""
    decrypt_the_message(assignments_path, 3, decrypted_assignment_path)
    house_dict = txt_to_dict(houses_path)
    up_as_dict = {}
    with open(decrypted_assignment_path, "r") as de_assign:
        for de_as in de_assign:
            de_as = de_as.split(",")
            house = de_as[1]
            if house_dict.get(house, -1) != -1:
                up_as_dict[de_as[0]] = {"house": house, "soldiers":int(de_as[2])+int(house_dict[house]["soldiers"]), "weapons":int(de_as[3])+int(house_dict[house]["weapons"])}
                house_dict[house]["soldiers"] = 0
                house_dict[house]["weapons"] = 0
    with open(updated_assignments_path, "w") as up_as_path, open(updated_houses_path, "w") as up_h_path:
        for k,v in up_as_dict.items():
            up_as_path.write(f"{k}: {v}\n")
        for k,v in house_dict.items():
            up_h_path.write(f"{k}: {v}\n")
         


def txt_to_dict(path):
    d = {}
    with open(path, "r") as file:
        for l in file:
            l = l.strip()
            if l:
                k, v = l.split(": ", 1)
                v = v.strip('{}')
                items = v.split(", ")
                inner_dict = {}
                for item in items:
                    key, value = item.split(": ")
                    if value.isnumeric():
                        inner_dict[key.strip("'")] = int(value)
                    else:
                        inner_dict[key.strip("'")] = value.strip("'")
                d[k] = inner_dict
    return d