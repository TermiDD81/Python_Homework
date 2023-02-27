from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])
        return all_data


def show_all():
    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")


def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer


def add_new_contact():
    global last_id
    array = ["surname","name", "patronymic", "phone number"]
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("The entry has been successfully added to the phone book!\n")
    else:
        print("The data already exists!")


def search_contact():
    search_data = exist_contact(0, input("Enter the search data: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("The data is not correct!")


def del_contact():
    global all_data
    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")


def change_contact(data_tuple):
    global all_data
    symbol = "\n"
    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                        "1. Show all records\n"
                        "2. Add a record\n"
                        "3. Search a record\n"
                        "4. Delete a record\n"
                        "5. Change a record\n"
                        "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                del_contact()
            case "5":
                change_contact()
            case "6":
                play = False
            case _:
                print("Try again!\n")


main_menu()