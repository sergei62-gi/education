from string import ascii_uppercase

def main():
    uppercase_litter = [i for i in ascii_uppercase]
    return uppercase_litter

def repetition_of_letters(a:list):
    x = [a[i-1]*i for i in range(1, len(a)+1)]
    return x

def a_task():
    phrase = 'Take only the words that start with t in this sentence'
    list = [i for i in phrase.split() if i[0] == "t" or i[0] == "T"]
    print(list)

if __name__ == "__main__":
    namber = int(input())
    x = main()
    print(x[:namber])

    y = repetition_of_letters(x)
    print(y[:namber])

    a_task()
