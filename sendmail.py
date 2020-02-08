import smtplib, ssl
import csv
import yagmail
import codecs

def sendmail(filename):

    port = 465
    context = ssl.create_default_context()

    sender_em = input("Enter your email: \t")
    password = input("Enter your password: \t")
    reciever_em = input("Enter your friend's email: \t")

    print("ALERT: This is the last warning! Your email might even get banned.\nHopefully you've made an alternate email for this.")
    ans = input("Press Y to forward, anything else to exit:\t")

    if ans == 'y':
        print("Oh well, here we go.\n")
        print(f"Sending Emails to {reciever_em}Now.\n")
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                for word in line.split():
                    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                        server.login(sender_em, password)
                        server.sendmail(sender_em, reciever_em, word)
    else:
        print("Thank God!\n")
        print("That was too close!\n")
        exit(2)

def printscript(filename):

    counter = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                counter = counter + 1
                print(word)

    print(f"\nThis file has {counter} words. Either your friend will recieve {counter} emails if you go with option 1.\n")
    print("THINK BEFORE YOU HIT 1\n")
    print("Good Bye :)\n")

def main():

    filename = input("Enter file name: ")
    print("Select one option:\n")
    print("1. Send Script to friend, 1 WORD = 1 EMAIL\n")
    print("2. Print Script (Recommended to do before going with 1st option)\n")
    selection = input("Type 1 or 2 and press Enter\t")

    if selection == '1':
        sendmail(filename)
    elif selection == '2':
        printscript(filename)
    else:
        print("You okay? That didn't look like a 1. or 2.\n ")
        print("Bye Then\n")
        exit(1)

if __name__ == "__main__":
    main()
