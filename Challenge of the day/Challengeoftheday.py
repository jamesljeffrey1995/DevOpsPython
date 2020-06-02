def main():
    listofnumbers = []
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 == 0:
            listofnumbers.append(i)
    print(listofnumbers)



if __name__ == "__main__":
        main()