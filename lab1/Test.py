import pandas as pd
if __name__ == '__main__':
    list=[1,2,3,4,5,6,7,8,9]
    list2 = pd.Series(list)
    print(list2)
    print(list2.iloc[:3])

