from camelcase import CamelCase

camelcase = CamelCase()

def toCamel(str):
    return camelcase.hump(str)

if __name__ == "__main__":
    print(toCamel("hello world"))


