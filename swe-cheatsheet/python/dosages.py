
def main():
    d1 = 500
    d2 = 650
    dosages = [(1, 0, 500), (0, 1, 650)]
    max_dose = 650
    dose_limit = 5000
    i = 0
    seen = {(1, 0), (0, 1)}
    while max_dose < dose_limit:
        a, b, amount = dosages[i]
        if (a + 1, b) not in seen:
            seen.add((a + 1, b))
            dosages.append((a + 1, b, amount + d1))
            max_dose = max(max_dose, amount + d1)
        if (a, b + 1) not in seen:
            seen.add((a, b + 1))
            dosages.append((a, b + 1, amount + d2))
            max_dose = max(max_dose, amount + d2)

        i += 1

    prev = 0
    for a, b, amount in sorted(dosages, key=lambda x: x[2]):
        print(f'{a}\t{b}\t{amount}\t{amount - prev}')
        prev = amount


main()
