def main():
    name = input("Filename: ")
    k, L, t = int(input("k: ")), int(input("L: ")), int(input("t: "))
    print(clump_find(name, k, L, t))

def clump_find(name, k, L, t):
    with open(name, 'r') as file:
        txt = file.read()


if __name__ == "__main__":
    main()