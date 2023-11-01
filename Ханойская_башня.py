def hanoi_tower(n, source, aux, target):
    if n == 1:
        print(f"Переместите диск 1 с {source} на {target}")
        return
    hanoi_tower(n-1, source, target, aux)
    print(f"Переместите диск {n} с {source} на {target}")
    hanoi_tower(n-1, aux, source, target)


def main():
    n = int(input("Введите количество дисков: "))
    hanoi_tower(n, 'A', 'B', 'C')

if __name__ == "__main__":
   main()