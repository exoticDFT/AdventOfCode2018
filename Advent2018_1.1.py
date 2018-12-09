freqFile = input("Enter file with frequencies: ")

try:
    with open(freqFile, 'r') as f:
        freq = f.read().splitlines()
    f.close()

    totalFreq = 0

    for x in freq:
        if '-' in x:
            totalFreq -= int(x.replace('-', ''))
        else:
            totalFreq += int(x.replace('+', ''))

    print ("\nTotal frequency change:", totalFreq)

except IOError:
    print ("Could not read file: ", freqFile)
