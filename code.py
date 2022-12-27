import random

def main():
    list = []
    for i in range(3,33,3):
        list.append(i)

    incorrect = 0
    score = 1
    level = get_level()
    x, y = generate_integer(level)

    i = 1

    while i <= 10:
        try:
            guess = int(input(f"{x} + {y} = "))
            if guess == (x + y):
                score += 1
                x, y = generate_integer(level)
                i += 1
            else:
                print("EEE")
                incorrect += 1
                if incorrect in list:
                    print(f"{x} + {y} = ", x + y)
                    score -= 1
                    x, y = generate_integer(level)
                    i+=1

        except ValueError:
            print("EEE")
            incorrect += 1
            if incorrect in list:
                print(f"{x} + {y} = ", x + y)
                score -= 1
                x, y = generate_integer(level)
                i+=1


    print("Score: ", score)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                raise ValueError
            else:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return [random.randint(0, 9), random.randint(0, 9)]

    if level == 2:
        return [random.randint(10, 99), random.randint(10, 99)]

    if level == 3:
        return [random.randint(100, 999), random.randint(100, 999)]





if __name__ == "__main__":
    main()
