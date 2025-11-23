import datetime

# collect user info and costs
def get_stuff():
    nm = input("Enter your name: ")
    while True:
        bal = input("Enter bank account balance: ₹")
        try:
            startbal = float(bal)
            break
        except:
            print("Invalid input, please enter a number.")
    exps = {}
    eid = 1
    money = startbal
    while True:
        print(f"\nFunds left: ₹{money:.2f}")
        print("[1] Add item  [2] Done?")
        ch = input("Choice: ")
        if ch == "1":
            itm = input("Add Item/Liability Name: ")
            while True:
                cost = input(f"How much `{itm}`costs? ₹")
                try:
                    c = float(cost)
                    break
                except:
                    print("Invalid input, please enter a number.")
            if c > money:
                print("Warning: Not enough money in accoungt.")
                go = input("Add it anyway? (y/n): ")
                if go.lower() != "y":
                    continue
            t = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            exps[eid] = {"nm": itm, "c": c, "dt": t}
            eid += 1
            money -= c
        elif ch == "2":
            break
        else:
            print("Invalid input, please enter a number.")
    return nm, startbal, exps

def check_money(startbal, exps):
    spent = 0
    for x in exps.values():
        spent += x["c"]
    bal2 = startbal - spent
    vibe = ""
    if bal2 < 0:
        vibe = "Critical: Account Overdrawn (Debt)!"
    elif bal2 < (startbal * 0.2):
        vibe = "Warnning: Low Balance!!!"
    else:
        vibe = "Good Financial Management."
    return spent, bal2, vibe

def show(nm, exps, spent, bal2, vibe):
    print("\n" + "="*60)
    print(f"{'YOUR SPEND REPORT':^60}")
    print(f"{'Name: ' + nm:^60}")
    print("="*60)
    print(f"{'No.':<4}|{'Item':<20}|{'Date':^16}|{'Amt':>10}")
    print("-"*60)
    for i, x in exps.items():
        print(f"{i:<4}|{x['nm']:<20}|{x['dt']:^16}|{x['c']:>10.2f}")
    print("-"*60)
    print(f"{'SPENT':<40}|{spent:>10.2f}")
    print(f"{'LEFT':<40}|{bal2:>10.2f}")
    print(f"HEALTH: {vibe}")
    print("="*60)

def run():
    me, bal0, expd = get_stuff()
    s, b, v = check_money(bal0, expd)
    show(me, expd, s, b, v)

if __name__ == "__main__":
    run()

