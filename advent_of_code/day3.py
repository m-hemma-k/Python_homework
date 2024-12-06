#!/usr/bin/env python3

# Funktion für das Produkt einer Liste von Zahlen
def prod(iterable):
    result = 1
    for n in iterable:
        result *= n
    return result

# Funktion für Übereinstimmung in einem Muster
def findall(pattern, string):
    import re # Reguläre Ausdrücke
    return re.findall(pattern, string)


with open("./data/day3.txt") as file:
    part1 = 0 # Zähler für Teil 1
    part2 = 0  # Zähler für Teil 2
    enabled = True  # Status true
    for line in file.read().splitlines():  # LZeile für Zeile
        for op in findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):  # Finde alle Operationen in der Zeile
            if op == "do()":
                enabled = True  # Status true
            elif op == "don't()":
                enabled = False  # Status false
            else:
                nums = findall(r"\d+", op)  # Finde alle Zahlen in der Operation
                result = prod(map(int, nums))  # Berechne das Produkt der Zahlen
                part1 += result  # Füge das Ergebnis zu Teil 1 hinzu
                if enabled:
                    part2 += result  # Füge das Ergebnis zu Teil 2 hinzu, wenn aktiviert

    # Gib die Ergebnisse für Teil 1 und Teil 2 aus
    print("Part 1:", part1)
    print("Part 2:", part2)