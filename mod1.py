def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("Both type different so I can't add those.")
        return
    else:
        result = sum(a, b)
    return result

if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10, 10.4))