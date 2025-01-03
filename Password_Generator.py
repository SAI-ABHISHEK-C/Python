import random 
import string

def generate_password():

    pass_list = []

    pass_len = int(input("length of your password ? :"))

    if pass_len < 4:
        print("Password should be more than 4 characters")
        return

    include_special = input("Do you want to include special characters ? (yes/no) : ").lower().strip()
    include_uppercase = input("Do you want to include uppercase characters ? (yes/no) : ").lower().strip()
    include_digits = input("Do you want to include digits ? (yes/no) : ").lower().strip()

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    all_characters = lower + uppercase + special + digits

    if include_uppercase == "yes":
        pass_list.append(random.choice(uppercase))
    if include_special == "yes":
        pass_list.append(random.choice(special))
    if include_digits == "yes":
        pass_list.append(random.choice(digits))

    req_len = pass_len - len(pass_list)
    for _ in range(req_len):
        pass_list.append(random.choice(all_characters))
    
    random.shuffle(pass_list)
    print("\n")
    return "".join(pass_list)


print("Your customised password has been generated : ",generate_password(),"\n")