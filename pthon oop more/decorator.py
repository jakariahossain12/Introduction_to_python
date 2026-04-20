def timer(func):
    def inner():
        print("time started")

        print(func)

        print("time ended")

    return inner

# timer()()

@timer # esy to decorate
def ger_factorial():
    print("factorial starting")

ger_factorial()

# vejailla way to decorate
# timer(ger_factorial)()