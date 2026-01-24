from ps3a import decrypt_the_message

def aggregate_house_contributions(input_path, decrypted_houses_path, output_path):
    """Function to aggregate house contributions from the encrypted input file and write the aggregated contributions to the output file."""
    decrypt_the_message(input_path, 3, decrypted_houses_path)
    d = {}
    with open(decrypted_houses_path, "r") as read:
        for s in read:
            s = s.split(",")
            if d.get(s[0], -1)==-1:
                d[s[0]] = {'soldiers': 0, 'weapons': 0}
            d[s[0]]['soldiers'] += int(s[1])
            d[s[0]]['weapons'] += int(s[2])
    with open(output_path, "w") as out:
        for k,v in d.items():
            out.write(f"{k}: {v}\n")
            
aggregate_house_contributions(r"data/houses_encrypted.txt", r"solution_outputs/houses_decrypted.txt", r"solution_outputs/aggregated_houses.txt")