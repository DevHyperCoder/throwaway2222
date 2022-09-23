with open("final.md","w") as f:
    for i in range(10,22):
        file = f'{i}.py'

        content = open(file).read()

        f.write(f"\n\n# Program {i}\n\n")
        f.write('```python\n')
        f.write(content + "\n")
        f.write('```\n\n')

        if i == 16:
            f.write(f'![](./{i}-output-1.png)\n\n')
            f.write(f'![](./{i}-output-2.png)\n\n')
            f.write("\n")
            continue

        f.write(f'![](./{i}-output.png)\n\n')

        if i in [14,15]:
            f.write(f'![](./{i}-emp-csv.png)\n\n')
        f.write("\n")
