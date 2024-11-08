inputfile = "client_import.csv"



with (open(inputfile, "r", encoding="utf-8") as file):
    for line in file:
        row = line.strip().split(";")
        data = {}

        if row[0].strip() != "":
            result = row[0].split()

            name = result[0]
            if len(result) > 1:
                surname = result[1]
                patronymic = result[2]

            data["last_name"] = name.lstrip()

        if row[1].strip() != "":
            data["first_name"] = row[1].lstrip()

        else:
            data["first_name"] = patronymic

        if row[2].strip() != "":
            data["sur_name"] = row[2].lstrip()
        else:
            data["sur_name"] = surname

        if row[3].strip() != "":
            if row[3].lstrip() == "м" or row[3].lstrip() == "мужской":
                data["gender"] = "1"
            if row[3].lstrip() == "ж" or row[3].lstrip() == "женский":
                data["gender"] ="2"

        if row[4].strip() != "":
            data["phone"] = row[4].lstrip().rstrip("\xa0")

        if row[5].strip() != "":
            data["avatar_file"] = row[5].lstrip().strip("Клиенты\\")

        if row[6].strip() != "":
            data["birthday"] = row[6].lstrip()

        if row[7].strip() != "":
            data["email"] = row[7].lstrip()

        if row[8].strip() != "":
            data["date_registration"] = row[8].lstrip()

        print(data)




