def message(msg: str | None):
    for i in msg:
        print(end=i)
        sleep(0.04)
    print()
    a: str = input("return key to continue…")
    if a == "exit" or a == "exit()": exit(0) # If u get bored ;)   


from time import sleep
print("HELLO\n")
for j in ("I won't show my name.
          "I learn programing.", 
          "I know python at most (second is html).", 
          "Now I (try to) learn Kotlin."):
message(j) # Created on phone
