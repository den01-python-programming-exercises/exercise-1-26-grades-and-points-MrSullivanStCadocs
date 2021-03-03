def main():
    #write your code below this line
    points = int(input("Give points [0-100]:"))

    if(points<0):
      print("Grade: impossible!")
    elif(points<=49):
      print("Grade: failed")
    elif(points<=59):
      print("Grade: 1")
    elif(points<=69):
      print("Grade: 2")
    elif(points<=79):
      print("Grade: 3")
    elif(points<=89):
      print("Grade: 4")
    elif(points<=100):
      print("Grade: 5")
    elif(points>100):
      print("Grade: incredible")

if __name__ == '__main__':
    main()
