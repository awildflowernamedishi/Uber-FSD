import utils
from datetime import datetime

def main():
    pwd1 = "ateen123"
    print(utils.hash(pwd1))
    pwd2 = "aditi456"
    print(utils.hash(pwd2))
    print(datetime.utcnow())
    

if __name__ == "__main__":
    main()