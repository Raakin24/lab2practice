def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**height)
    print("bmi: " + str(bmi))
    if (bmi<18.5):
        print("underweight")
        return -1
    elif(18.5<bmi<25.0):
        print("normalweight")
        return 0
    else:
        print("overweight")
        return 1

def main():
    output = calculate_bmi(weight=57, height=1.73)
    print("Return value based on weight classification: ", output)

if __name__ == "__main__":
    main()


