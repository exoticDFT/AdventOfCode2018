freqFile = input("Enter file with frequencies: ")

try:
    with open(freqFile, 'r') as f:
        freq = f.read().splitlines()

    freqs = set()
    totalFreq = 0
    freqs.add(totalFreq)
    found = False
    count = 0

    while not found:
        for x in freq:
            if '-' in x:
                totalFreq -= int(x.replace('-', ''))
            else:
                totalFreq += int(x.replace('+', ''))

            if totalFreq in freqs:
                found = True
                break

            freqs.add(totalFreq)
        count += 1

    print ("\nTotal frequency change:", totalFreq)
    print ("Total iterations: ", count)

except IOError:
    print ("Could not read file: ", freqFile)
