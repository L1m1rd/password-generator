import random



def head_text():
    print("====================================================")
    print("=============== ГЕНЕРАТОР ПАРОЛЕЙ ==================")
    print("====================================================")
    print(" ")


def length():
    while True:
        try:
            password_length = int(input("Введи длину пароля (от 8 до 128)"))
            if 8 <= password_length <= 128:
                return password_length
            else:
                print("Число должно быть от 8 до 128!")
        except:
            print("Введи число!")

def nums():
    password_nums = True
    while True:
        try:
            pas_nums = input("Нужны цифры в пароле? (Пиши 'да' или 'нет')")
            if pas_nums == 'да':
                password_nums = True
                return password_nums
            elif pas_nums == 'нет':
                password_nums = False
                return password_nums
            else:
                print("Пиши только 'да' или 'нет'")
        except:
            print("Пиши только 'да' или 'нет'")

def symbols():
    password_syms = True
    while True:
        try:
            pas_syms = input("Нужны специальные символы в пароле? (Пиши 'да' или 'нет')")
            if pas_syms == 'да':
                password_syms = True
                return password_syms
            elif pas_syms == 'нет':
                password_syms = False
                return password_syms
            else:
                print("Пиши только 'да' или 'нет'")
        except:
            print("Пиши только 'да' или 'нет'")


def generate(pass_len, pass_nums, pass_syms):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums  = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

    pool = letters
    if pass_nums:
        pool += nums
    if pass_syms:
        pool += symbols

    password = ''
    for _ in range(pass_len):
        password += random.choice(pool)

    return password

def rerol():
    resp_pass = True
    while resp_pass:
        like = input("Вам нравится пароль? (Пиши 'да' или 'нет')")
        if like == 'да':
            resp_pass = False
        elif like == 'нет':
            print("Тогда я сделаю новый пароль ")
            resp_pass = True
        else:
            print("Пиши только 'да' или 'нет'")



def main():
    head_text()

    pass_len = length()
    pass_nums = nums()
    pass_syms = symbols()

    password = generate(pass_len, pass_nums, pass_syms)

    print("пароль: ", password)



if __name__ == "__main__":
    main()