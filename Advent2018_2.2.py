filename = input("Enter filename to load: ")

try:
    with open(filename, 'r') as f:

        ids = []

        for line in f:
            ids.append(line)
            
        for s1 in ids:
            for s2 in ids:
                diff = 0
                sim = ''
                
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        diff += 1
                    else:
                        sim += s1[i]
                        
                if diff == 1:
                    print (sim)
                
    f.close()

except IOError:
    print ("Could not read file: ", filename)