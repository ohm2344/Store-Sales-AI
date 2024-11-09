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
            if(line.split(",")[0] == "date"):
                continue
            else:








def main():
    Train = getTrainData("C:\\Users\\Eillo\\PycharmProjects\\Store-Sales-AI\\data\\train.csv")
    print(Train)