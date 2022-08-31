def get_last_digit(seed):
    out = (seed*661231616) % 10

    return out

seed_num = input("Enter 2-digit number: ")
return_num = get_last_digit(int(seed_num))

print(return_num)