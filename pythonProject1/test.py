def check_password_base(password):
    with open(file='base.csv', mode='r', encoding='utf-8') as b_file:
        a = csv.reader(b_file, delimiter='|')
        for val in a:
            if a[1].lstrip() == password:
                print("Tayyor")