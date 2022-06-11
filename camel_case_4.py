# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
for line in sys.stdin:
    line = line.split(";")
    if line[0] == "C":
        name = line[2].split()
        if line[1] == "C":
            sys.stdout.write(name[0][0].upper() + name[0][1:])
        else:
            sys.stdout.write(name[0])
        for word in name[1:]:
            sys.stdout.write(word[0].swapcase() + word[1:])
        if line[1] == "M":
            sys.stdout.write("()")
    else:
        sys.stdout.write(line[2][0].lower())
        for letter in line[2][1:]:
            if letter.isupper():
                sys.stdout.write(" " + letter.lower())
            else:
                sys.stdout.write(letter)
    sys.stdout.write("\n")
