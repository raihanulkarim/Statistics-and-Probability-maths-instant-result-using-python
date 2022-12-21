import math


def boxplot():
    no_of_items = int( input( "Enter the number of inputs:" ) )
    print( "Enter the value:" )
    x = []
    value_no = 1
    for i in range( no_of_items ):
        value = float( input( "{}:".format( value_no ) ) )
        x.append( value )
        value_no += 1

    if no_of_items % 2 == 1:
        median_point = int(.5 *(no_of_items+1))
        mid_value = x[median_point -1]
    elif no_of_items % 2 == 0:
        median_point = int(.5 * (no_of_items+1))
        mid_value = (x[median_point-1] + x[median_point])/2

    # Interquartiles Range
    q1 = .25*(no_of_items+1)
    q3 = .75*(no_of_items+1)
    # print( "Q1:", q1 )
    # print( "Q1:", q3 )
    x.sort()
    if q1 %2 == 0:
        q1 = int(q1)
        q1_value = x[q1-1]
        # print("Q1:", q1_value)
    else:
        q1 = int(q1)
        q1_value = (x[q1-1]+x[q1])/2
        # print("Q1:", q1_value)

    if q3 % 2 == 0:
        q3 = int( q3 )
        q3_value = x[q3 - 1]
        # print("Q3:", q3_value)
    else:
        q3 = int( q3 )
        q3_value = (x[q3 - 1] + x[q3]) / 2
        # print("Q3:", q3_value)

    iqr = q3_value - q1_value
    lower = q1_value - 1.5*iqr
    uppper = q3_value + 1.5*iqr

    outliers = []
    for i in range(no_of_items):
        if x[i] > uppper:
            outliers.append(x[i])
    print("Min{}\nMax:{}".format(min(x), max(x)))
    print("Q1:",q1_value, "Q3:",q3_value)
    print( "Interquartile Range:", iqr)
    print("Median: {0:.2f} ".format(mid_value))
    print("Lower fence:", lower)
    print("Upper fence:", uppper)
    print("Outliers:", outliers)

def Chebysheff():
    level = int( input( "1. With K \n2. Without K\n>>" ) )
    if level == 1:
        k = float(input("Enter the K:"))
        value = (1/pow(k,2))
        value = (1 - value)
        print("Value:{0:.2f}".format( value))
    else:
        limit = float( input( "Enter the Limit:" ) )
        mean = float( input( "Enter Mean:" ) )
        sd = float( input( "Enter Standard Deviation:" ) )
        k = (limit - mean) / sd
        value = (1 / pow( k, 2 ))
        value = (1 - value)
        parcent = value * 100+1
        print("K:{0:.2f}".format(k))
        print( "Value:{0:.2f}".format( value ) )
        print( "Percentage:{0:.1f}%".format( parcent ) )

def z_score():
    value = float(input("Enter the value:"))
    mean = float(input("Enter Mean:"))
    sd = float(input("Enter Standard Deviation:"))
    score = (value - mean)/sd
    print("Z-score:{0:.2f}".format(score))

def deviation():
    level = int (input("1. Population \n2. Sample\n>>"))
    no_of_items = int( input( "Enter the number of inputs:" ) )
    print( "Enter the value:" )
    x = []
    value_no = 1
    for i in range( no_of_items ):
        value = float( input( "{}:".format( value_no ) ) )
        x.append( value )
        value_no += 1
    mean = sum( x ) / no_of_items
    x_avg = []
    for i in range(no_of_items):
        value = x[i] - mean
        x_avg.append(value)
    x_avg_sqr = []
    for i in range( no_of_items ):
        value = pow(x_avg[i], 2)
        x_avg_sqr.append( value )
    if level == 1:
        sd = math.sqrt(sum(x_avg_sqr)/no_of_items)
        variance = (sum(x_avg_sqr)/no_of_items)
    elif level == 2:
        sd = math.sqrt(sum(x_avg_sqr)/(no_of_items-1))
        variance = (sum(x_avg_sqr)/(no_of_items-1))

    print("average of X:", mean)
    print("(x - average X):", x_avg)
    print("(x - average X)sqr:", x_avg_sqr)
    print("Sum of (x-avgX)sqr:", sum(x_avg_sqr))
    print("Standard Variance:{0:.4f}".format(variance))
    print("Standard Deviation:{0:.4f}".format(sd))



def variabilty():
    no_of_items = int( input( "Enter the number of inputs:" ) )
    print( "Enter the value:" )
    x = []
    value_no = 1
    for i in range( no_of_items ):
        value = float( input( "{}:".format( value_no ) ) )
        x.append( value )
        value_no += 1

    # ranges
    ranges = max(x) - min(x)

    # Interquartiles Range
    q1 = .25*(no_of_items+1)
    q3 = .75*(no_of_items+1)
    # print( "Q1:", q1 )
    # print( "Q1:", q3 )
    x.sort()
    if q1 %2 == 0:
        q1 = int(q1)
        q1_value = x[q1-1]
        # print("Q1:", q1_value)
    else:
        q1 = int(q1)
        q1_value = (x[q1-1]+x[q1])/2
        # print("Q1:", q1_value)

    if q3 % 2 == 0:
        q3 = int( q3 )
        q3_value = x[q3 - 1]
        # print("Q3:", q3_value)
    else:
        q3 = int( q3 )
        q3_value = (x[q3 - 1] + x[q3]) / 2
        # print("Q3:", q3_value)

    iqr = q3_value - q1_value

    print( "Range:", ranges)
    print("Q1:",q1_value, "Q3:",q3_value)
    print( "Interquartile Range:", iqr)

def measures():
    no_of_items = int( input( "Enter the number of inputs:" ) )
    print( "Enter the value:" )
    x = []
    value_no = 1
    for i in range( no_of_items ):
        value = float( input( "{}:".format( value_no ) ) )
        x.append( value )
        value_no += 1
    mean = sum(x) / no_of_items
    x.sort()
    if no_of_items % 2 == 1:
        median_point = int(.5 *(no_of_items+1))
        mid_value = x[median_point -1]
    elif no_of_items % 2 == 0:
        median_point = int(.5 * (no_of_items+1))
        mid_value = (x[median_point-1] + x[median_point])/2
        # print(median_point)

    if mean == mid_value:
        skew = 'Symmetric'
    elif mean > median_point:
        skew = 'Skewed Right'
    else:
        skew = 'Skewed Left'
    print("Sorted:", x)
    print("Average or Mean:{}".format(mean))
    print("Median: {0:.2f} ".format(mid_value))
    print("Extreme Values:", skew)


def bivariete():
    no_of_items = int(input("Enter the number of inputs:"))
    print("Enter the value of x:")
    x = []
    value_no = 1
    for i in range(no_of_items):
        value = float(input("{}:".format(value_no)))
        x.append(value)
        value_no += 1
    # print(x)
    print( "Enter the value of Y:" )
    y = []
    value_no = 1
    for i in range( no_of_items ):
        value = float(input("{}:".format(value_no)))
        y.append( value )
        value_no += 1
    # print( y )
    xy =[]
    for i in range(no_of_items):
        value = x[i] * y[i]
        xy.append(value)
    # print(xy)
    pow_x = []
    pow_y = []

    for i in range(no_of_items):
        value1 = pow(x[i],2)
        value2 = pow(y[i],2)
        pow_x.append(value1)
        pow_y.append(value2)
    # print(pow_x)
    # print(pow_y)
    sum_pow_x = sum(pow_x)
    sum_pow_y = sum(pow_y)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xy)
    Sx = math.sqrt((sum_pow_x - pow(sum_x,2)/no_of_items)/(no_of_items-1))
    Sy = math.sqrt((sum_pow_y - pow(sum_y,2)/no_of_items)/(no_of_items-1))
    Sxy = (sum_xy - (sum_x * sum_y)/no_of_items)/(no_of_items-1)
    avg_x = sum_x/no_of_items
    avg_y = sum_y/no_of_items
    r = Sxy/(Sx * Sy)
    b = r*(Sy/Sx)
    a = avg_y - b * avg_x
    print("x: ", x)
    print("y: ", y)
    print("xy: ", xy)
    print("x2: ", pow_x)
    print("y2: ", pow_y)
    print("Sum of x: {0:.4f} ".format(sum_x))
    print("Sum of y: {0:.4f} ".format(sum_y))
    print("Average of x: {0:.4f} ".format(avg_x))
    print("Average of y: {0:.4f} ".format(avg_y))
    print("Sum of xy: {0:.4f} ".format(sum_xy))
    print("Sum of x2: {0:.4f} ".format(sum_pow_x))
    print("Sum of y2: {0:.4f} ".format(sum_pow_y))
    print("Sx: {0:.4f}".format(Sx))
    print("Sy: {0:.4f}".format(Sy))
    print("Sxy: {0:.4f}".format(Sxy))
    print( "Correlation coefficient, r: {0:.4f}".format(r))
    print( "The Best Fitting Line,y = a + bx = {0:.4f}".format(a), "+ {0:.4f}x".format(b))

    inp = input("\nPress enter to exit and y to calculate again:")
    if inp.upper() == "Y":
        bivariete()
    else:
        exit(1)

def main():
    print( """
        1. Mean , Mode, Median
        2. Range, Interquartile Range
        3. Standard Deviation / Variance
        4. Z - score
        5. Chebysheff's Theoram
        6. Box Plot
        7. Emphirical Rules
        8. Bivariate Data
        .Probability
    """ )
    inp = int( input( ">>" ) )
    if inp == 1:
        measures()
    elif inp == 2:
        variabilty()
    elif inp == 3:
        deviation()
    elif inp == 4:
        z_score()
    elif inp == 5:
        Chebysheff()
    elif inp == 6:
        boxplot()
    elif inp == 8:
        bivariete()

    inps = input( "\nPress enter to exit and y to calculate again:" )
    if inps.upper() == "Y":
        main()
    else:
        exit( 1 )



main()