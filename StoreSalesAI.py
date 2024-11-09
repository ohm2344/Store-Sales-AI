import pandas as pd
#TODO: Implement stringHash function
def stringHash(string):
    return 0

def getTrainData(filename):
    Train = {}
    with open(filename) as reader:
        for line in reader:
            if(line.split(",")[0] == "id"):
                continue
            else:
                dict_array = line.strip().split(",")
                date = dict_array[1]
                store_number = int(dict_array[2])
                #Family = stringHash(dict_array[3])
                Family = dict_array[3]
                promo_sales = (dict_array[4],dict_array[5])
                store_number_dict = {}
                Family_dict = {}
                Family_dict[Family] = promo_sales
                store_number_dict[store_number] = Family_dict
                Train[date] = store_number_dict # Date -> Store Number -> Family -> (sales,promotion)

    return Train

def Holiday(filename):

    Holiday = {}
    with open(filename) as reader:
        for line in reader:
            date = line.strip().split(",")[0]
            if(date == "date"):
                continue
            elif(line.strip().split(",")[5]=="True"):
                continue
            else:
                Holiday[date] = True
    return Holiday


def getOil(filename):
    Oil = {}
    checker = True
    with open(filename) as reader:
        for line in reader:
            line = line.strip().split(",")
            if checker is True:
                checker = False
                continue
            else:
                date = line[0]
                price = line[1]
                if price == "":
                    continue
                else:
                    price = float(price)
                    Oil[date] = price
    return Oil

def main():
    Train = getTrainData("train.csv")
    print(Train)
    holiday = Holiday("holiday.csv")
    print(holiday)
    oil = getOil("oil.csv")
    print(oil)