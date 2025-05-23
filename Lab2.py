

def get_user_inputs():
    user_temps = input("Enter temperatures separated by commas: ")
    print("Numbers entered:" + user_temps)
    temp_strings = user_temps.split(",")
    temperatures = [float(temp) for temp in temp_strings]
    return temperatures 

def calc_average(temperatures):
    avg = sum(temperatures)/len(temperatures)
    return avg

def sort_temperatures(temperatures):
    sort_temperature = sorted(temperatures)
    return sort_temperature 

def find_min_temp(temperatures):
    return min(temperatures)

def find_max_temp(temperatures):
    return max(temperatures)
    
def find_median(sort_temperature):
    n = len(sort_temperature)
    mid = n//2

    if(n%2==0):
        return (sort_temperature[mid-1] + sort_temperature[mid])/2
    else:
        return sort_temperature[mid]
    
def main():
    temperatures = get_user_inputs()
    print("\nYou entered:", temperatures)
    sorted_temps = sort_temperatures(temperatures)
    print("Sorted temperatures:", sort_temperatures(temperatures))
    print("Average temperature:", round(calc_average(temperatures), 2))
    print("Minimum temperature:", find_min_temp(temperatures))
    print("Maximum temperature:", find_max_temp(temperatures))
    print("Median temperature:", find_median(sorted_temps))

if __name__ == "__main__":
    main()
    

    



