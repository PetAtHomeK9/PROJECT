class Computer:
    def configuration(self):
        print("i5, 16gb, 1TB")

Com1 = Computer()
Com2 = Computer()
Computer.configuration(Com1)
Computer.configuration(Com2)

Com1.configuration()
Com2.configuration()