class Torch:
    def __init__(self, name):
        self.name = 'choi su gil'
    
    def print(self):
        print('this is torch class' +self.name)

def main():
    print('this is my first python programming')
    torch1 = Torch('최수길')
    # torch2 = Torch()
    # torch3 = Torch()
    torch1.print()
    print(torch1.name)

if __name__ == '__main__':
    main()
