#!/usr/bin/python3

# program that prints all the names defined by the compiled module

if __name__ == "__main__":
    import hidden_4
    titles = dir(hidden_4)
    for title in titles:
        if title[:2] != "__":
            print(title)
