class car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance=5555
    def company(self):
        while True:
            print("Toyota,Mercedes")
            self.n=input("enter the car company")
            if self.n=="Toyata":
                print("welcome to toyota")
                self.model()
                break
            elif self.n=="Mercedes":
                print("welcome to merc")
            if self.choice=="Fortuner":
                self.price(self.choice)
                break
            else:
                print("enter valid")
        elif self.n=="Mercedes":
            while True:
                print("Select from amg amd gw")
                self.choice=input("enter the car")
                                  if self.choice=="amg":
                                  self.price(self.choice)
                                  break
                                else:
                                    print("enter valid")
        def price(self,choice):
            if choice=="Fortuner":
                self.p=4500000
            elif choice=="LC":
                self.p=1000000
            elif choice=="amg":
                self.p=24432874
            elif choice=="gw":
                self.p=843726837
                tot_p=self.p+self.sgst+self.cgst+self.insurance
                print(tot_p)
