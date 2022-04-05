def readFromFile(filename):
    '''
    Function that reads from a specific file a string of coordinates
    :param filename: - name of the file we want to read
    :return: the string of coordinates
    '''
    f = open(filename, "r")
    return f.read()


def parseToDict(points):
    '''
    Function that parse data from a string of coordinates to a dictionary where the keys are
    the values of y coordinate and the values of the keys are lists of x coordinates for the specific y
    ex : (1,2), (1,3), (2,2)-> {2=[1,2], 3=[1]}
    :param points: the string of coordinates
    :return: dictionary of coordinates
    '''
    points_Dict = {}
    points_List = points.split(", ") #we separate the coordinates by "," symbol

    for point in points_List:

        point = point.replace("(","").replace(")","") #we get rid of parenthesis
        coordinates = point.split(","); #we get the coordinates values

        x_value = coordinates[0];
        y_value = coordinates[1];

        if y_value in points_Dict:
            points_Dict[y_value].append(int(x_value)) #if this y-value already exists in the dictionary than we append to his list a new x value
        else :
            points_Dict[y_value]=[] #we create a new key with y-value and then append to his list
            points_Dict[y_value].append(int(x_value))

    #sorting every list from the values of the keys
    for i in points_Dict:
        points_Dict[i].sort()
    return points_Dict


def two_by_two_list(list):
    '''
    Function that transform a list of numbers into a list of pairs with every element, 2 by 2 from original list
    :param list: list of numbers
    :return: final_list : list of pairs with every element, 2 by 2
    '''
    final_list = []
    for i in range (len(list)):
        for j in range (i+1,len(list)):
            final_list.append((list[i],list[j]));
    return final_list;


def pairsList(points_Dict):
    '''
    Function that creates a list af every 2 elements, 2 by 2 from every list of the dictionary
    :param points_Dict: dictionary of coordinates
    :return: temp_list : list of lists
    '''
    temp_list = list(points_Dict.values()) #creating of a list with dict values
    for i in temp_list:
        temp_list[temp_list.index(i)] = two_by_two_list(i)
    return temp_list;

def dataProcessing(points):
    '''
    Function that parse the data from a string of coordinates to a dictionary then to a list of pairs
    :param points: the string of coordinates
    :return: list_of_pairs : list of lists
    '''
    points_Dict = parseToDict(points)
    list_of_pairs = pairsList(points_Dict)
    return list_of_pairs


def number_of_rectangles(list_of_pairs):
    '''
    Function that calculate the number of rectangles
    :param list_of_pairs: for every y this list contains a list with all the pairs formed with coresponding x values
    :return: no_of_rect : number of rectangles that can be created by those points
    '''
    no_of_rect = 0;
    for i in range (len(list_of_pairs)-1):  # we go through all list of pairs except the last one
        for j in list_of_pairs[i]:  # we go through every pair of the list
            for k in range (i+1,len(list_of_pairs)): #we go through every list of pairs from i+1 to the last one and verify if we have a matching pair
                if j in list_of_pairs[k]:
                    no_of_rect+=1;
    return no_of_rect


def testF():
    '''
    Testing function for different input sets
    '''
    points = readFromFile("input_test1.txt")
    assert (number_of_rectangles(dataProcessing(points)) == 3)
    points = readFromFile("input_test2.txt")
    assert (number_of_rectangles(dataProcessing(points)) == 1)
    points = readFromFile("input_test3.txt")
    assert (number_of_rectangles(dataProcessing(points)) == 3)
    points = readFromFile("input_test4.txt")
    assert (number_of_rectangles(dataProcessing(points)) == 5)
    points = readFromFile("input_test5.txt")
    assert (number_of_rectangles(dataProcessing(points)) == 7)

if __name__ == '__main__':
    testF()

    # points = readFromFile("input_test5.txt")
    # print(number_of_rectangles(dataProcessing(points)))



