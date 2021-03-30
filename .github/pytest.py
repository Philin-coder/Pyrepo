gradys = int(input())  # ОШИБКА?1
vrema = input()
if gradys >= 10 and gradys <= 18:
    if vrema == "Morning":
        Outfit = Sweatshirt  # ПОСМОТРЕТЬ ВВОД SW  SN
        Shoes = Sneakers
        print(f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
    else:
        if gradys >= 10 and gradys <= 18:
            if vrema == "Afternoon":
                Outfit = Shirt
                Shoes = Moccasins
                print(f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
        else:
            if gradys>=10 and gradys<=18:
                if vrema=="Evening":
                    Outfit = Shirt
                    Shoes = Moccasins
                    print (f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
            else:
                if gradys<18 and gradys<=24:
                    if vrema=="Мorning":
                        Outfit = Shirt
                        Shoes = Moccasins
                        print (f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
                else:
                    if gradys<18 and gradys<=24:
                        if vrema=="Afternoon":
                            Outfit = T-Shirt
                            Shoes = Sandals
                            print (f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
                    else:
                        if gradys<18 and gradys<=24:
                            if vrema=="Evening":
                                Outfit = Shirt
                                Shoes = Moccasins
                                print (f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
                        else:
                            if gradys>=25:
                                if vrema=="Мorning":
                                    Outfit = T-Shirt
                                    Shoes = Sandals
                                    print (f"It's {gradys} degrees, get your {Outfit} and {Shoes}.")
