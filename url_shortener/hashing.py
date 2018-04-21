from hashlib import md5

def convertUrlToId(url):
    hashString = md5(url.encode("utf-8")).hexdigest()
    return hashString

def convertIdToShortUrl(id):
    shortUrl = ''
    keySet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    binaryId = convertIdtoBinary(id)
    binaryIdDec = int(binaryId.replace(' ', '')[0:43], 2)
    shortId = convertDecTo64(binaryIdDec)
    for id in shortId:
        shortUrl += keySet[id]
    return shortUrl

def convertIdtoBinary(id):
    return ' '.join(format(ord(x), 'b') for x in id)

def convertDecTo64(id):
    sortId = []
    while id > 0:
        sortId.append(id % 64)
        id = id // 64
    return sortId
