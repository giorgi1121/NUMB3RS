import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        chars = ip.split(".")
        for x in chars:
            if int(x) < 0 or int(x) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()