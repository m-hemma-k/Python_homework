#!/usr/bin/env python3

# Day 4: Ceres Search

# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
# It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. 
# Here are a few ways XMAS might appear, where irrelevant characters have been replaced with.

# horizontal, 
# vertical, 
# diagonal, 
# written backwards, 
# or even overlapping other words

def read_input(filepath):
    with open(filepath, 'r') as infile:
        grid = infile.read().splitlines()
        width, height = len(grid[0]), len(grid)
    return grid, width, height

def part_one(grid, width, height):
    # Zähler für die gefundenen Muster
    part1 = 0
    
    # Durchlaufe alle möglichen Richtungen: rechts, unten, diagonal rechts unten, diagonal links unten
    for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
        for x in range(width):
            # Durchlaufe jede Zeile des Rasters
            for y in range(height):
                # Überprüfe, ob die nächsten 3 Schritte in der Richtung (dx, dy) innerhalb des Rasters bleiben
                if x + 3 * dx not in range(width) or y + 3 * dy not in range(height):
                    continue  # Wenn nicht, überspringe diese Iteration
                
                # # Überprüfe, ob das Muster "XMAS" in der aktuellen Richtung gefunden wird
                # if all(grid[y + i * dy][x + i * dx] == c for i, c in enumerate("XMAS")):
                #     part1 += 1  # Erhöhe den Zähler, wenn das Muster gefunden wird
                
                # # Überprüfe, ob das Muster "SAMX" in der aktuellen Richtung gefunden wird
                # if all(grid[y + i * dy][x + i * dx] == c for i, c in enumerate("SAMX")):
                #     part1 += 1  # Erhöhe den Zähler, wenn das Muster gefunden wird

                # # Überprüfe, ob das Muster "XMAS" in der aktuellen Richtung gefunden wird
                found_xmas = True
                for i, c in enumerate("XMAS"):
                    if grid[y + i * dy][x + i * dx] != c:
                        found_xmas = False
                        break
                if found_xmas:
                    part1 += 1  # Erhöhe den Zähler, wenn das Muster gefunden wird

                # Überprüfe, ob das Muster "SAMX" in der aktuellen Richtung gefunden wird
                found_samx = True
                for i, c in enumerate("SAMX"):
                    if grid[y + i * dy][x + i * dx] != c:
                        found_samx = False
                        break
                if found_samx:
                    part1 += 1  # Erhöhe den Zähler, wenn das Muster gefunden wird
    
    # Gib die Anzahl der gefundenen Muster aus
    return print("Part 1:", part1)

# the Elf looks quizzically at you. Did you misunderstand the assignment?
# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; 
# it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

def part_two(grid, width, height):
    # Zähler
    part2 = 0
    
    # Durchlaufe jede Spalte des Rasters, außer den Randspalten
    for x in range(1, width - 1):
        # Durchlaufe jede Zeile des Rasters, außer den Randzeilen
        for y in range(1, height - 1):
            # Überprüfe, ob das aktuelle Zeichen "A" ist und die umliegenden Bedingungen erfüllt sind
            if (
                grid[y][x] == "A"  # Das aktuelle Zeichen muss "A" sein
                and grid[y - 1][x - 1] in "MS"  # Das Zeichen oben links muss "M" oder "S" sein
                and grid[y + 1][x + 1] in "MS"  # Das Zeichen unten rechts muss "M" oder "S" sein
                and grid[y - 1][x - 1] != grid[y + 1][x + 1]  # Die Zeichen oben links und unten rechts dürfen nicht gleich sein
                and grid[y - 1][x + 1] in "MS"  # Das Zeichen oben rechts muss "M" oder "S" sein
                and grid[y + 1][x - 1] in "MS"  # Das Zeichen unten links muss "M" oder "S" sein
                and grid[y - 1][x + 1] != grid[y + 1][x - 1]  # Die Zeichen oben rechts und unten links dürfen nicht gleich sein
            ):
                part2 += 1  # Addiere zum Zähler
    
    # Gib die Anzahl der gefundenen Muster aus
    print("Part 2:", part2)

grid, width, height = read_input("./data/day4.txt")
# print(grid)
# print(width)
# print(height)
part_one(grid, width, height)
part_two(grid, width, height)