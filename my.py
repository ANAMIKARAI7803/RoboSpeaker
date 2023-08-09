import os

if __name__ == '__main__':
    print("welcome to Robospeaker 1.1. Created by anamikaa")
    while True:
        x = input("enter what you want me to speak:")
        if x == "q":
            os.system("say'bye bye friend'")
            break

    command = f"say{x}"
    os.system(command)