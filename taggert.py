import fileinput


def print_tags_line(file, line, wholeline):
    sep = "	"
    splits = line.split(maxsplit=2)
    probably_thing = splits[1] if 1 < len(splits) else splits[0]
    match splits[0]:
        case "foreign":  # foreign import
            print_tags_line(file, splits[2], wholeline)
        case "module":
            print(probably_thing, file, f'/^{wholeline}$/;"', "f", sep=sep)
        case "type":
            print(probably_thing, file, f'/^{wholeline}$/;"', "f", sep=sep)
        case "newtype":
            print(probably_thing, file, f'/^{wholeline}$/;"', "f", sep=sep)
        case "data":
            print(probably_thing, file, f'/^{wholeline}$/;"', "f", sep=sep)
        case "class":
            thing = line.split("<=")[1].split()[0] if "<=" in line else probably_thing
            print(thing, file, f'/^{wholeline}$/;"', "f", sep=sep)
        case thing:
            print(thing, file, f'/^{wholeline}$/;"', "f", sep=sep)


def main():
    for info in fileinput.input(encoding="utf-8"):
        [file, line] = info[:-1].split(":", maxsplit=1)
        print_tags_line(file, line, line)

if __name__ == "__MAIN__":
    main()
