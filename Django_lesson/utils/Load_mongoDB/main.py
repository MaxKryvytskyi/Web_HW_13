from parser_BS4 import main as start_parser
from load_json import main as load_in_mongoDB

def main():
    result = start_parser()
    if result:
        load_in_mongoDB()
        print("Successfully")
    else:
        print("Failure")

if __name__ == "__main__":
    main()