from utility import *
import json

caurses = {}


def listCaurses():
    global caurses
    caurses = readJSON("caurses.json")
    print("**  Name of caurses and there codes  **")
    print("----------------------------------")
    for code in caurses.keys():
        caurse = caurses[code]
        print("{}: {} :{}".format(code,caurse["Name"],caurse["Maxdegree"]))

    return



def viewCaurse():
    global caurses
    code = getCode(caurses,"cources")
    caurse = caurses[code]

    print("Name: {}".format(caurse["Name"]))
    print("Maxdegree: {}".format(caurse["Maxdegree"]))
    return

def inputCaurse(caurse):
    global caurses
    if "code" not in caurse.keys():
        while True:
            code = input("Enter code:").replace(" ","")
            if not code.isdigit():
                print("Code must not contain letters, try another....")
            elif len(code)!=3:
                print("Code lenth must be 3 digit, try another....")
            elif code in caurses.keys():
                print("Code already used, try another....")
            else :
                caurse["code"] = code
                break

    caurse["Name"] = input("Enter Name:")
    caurse["Maxdegree"] = input("Enter MaxDegree:")
    return caurse


def addCaurse():
    global caurses
    caurse =inputCaurse({})
    code = caurse["code"]
    caurses[code] = caurse
    writeJSON(caurses,"caurses.json")


def editCaurse():
    global caurses
    code = getCode(caurses, "cources")
    caurse = inputCaurse(caurses[code])
    code = caurse["code"]
    caurses[code] = caurse
    writeJSON(caurses,"caurses.json")



def removeCaurse():
    global caurses
    code = getCode(caurses,"cources")
    del caurses[code]
    writeJSON(caurses,"caurses.json")

def back():
    return