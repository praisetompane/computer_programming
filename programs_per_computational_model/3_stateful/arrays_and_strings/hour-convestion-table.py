def generatePMConversionTable(n, index, hour, hour24):
    print(f'"0{hour}PM" -> "{hour24}",')
    if index == n:
        print("")
    else:
        generatePMConversionTable(n, index + 1, hour - 1, hour24 - 1)


def generateAMConversionTable(n, index, hour, hour24):
    print(f'"0{hour}AM" -> "{hour24}",')
    if index == n:
        print("")
    else:
        generateAMConversionTable(n, index + 1, hour - 1, hour24 - 1)


generatePMConversionTable(11, 0, 11, 23)
generateAMConversionTable(11, 0, 11, 11)
