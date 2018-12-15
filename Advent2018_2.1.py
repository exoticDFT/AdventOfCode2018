filename = input("Enter filename to load: ")

try:
    with open(filename, 'r') as f:

        count = [0, 0]
        dict = {}

        for line in f:
            dict.clear()

            for letter in line:
                if letter not in dict:
                    dict[letter] = 0
                
                dict[letter] += 1
                
            has2 = False
            has3 = False
            
            for k,v in dict.items():
                if v == 2:
                    has2 = True
                if v == 3:
                    has3 = True
            
            if has2:
                count[0] += 1
            if has3:
                count[1] += 1
            
        print (count[0] * count[1])

    f.close()

except IOError:
    print ("Could not read file: ", filename)