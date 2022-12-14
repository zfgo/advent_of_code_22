
def main():
    file_name = "input.txt"
    lines = []
    total = 0
    crate_ct = 0
    indicator = True
    column_ct = 0

    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

        if lines[i].find('[') >= 0:
            for char in lines[i]:
                if char == '[':
                    crate_ct += 1
        elif indicator:
            indicator = False
            column_ct = len(lines[i].split())

    print(crate_ct, column_ct)
            

    
    print(total)


if __name__ == "__main__":
    main()
