
class Organization:
    def __init__(self):
        self.formatnames('names.txt')
        self.formatlinks('links.txt')
        self.makedict()

    def formatnames(self, filename):
        with open(filename) as f:
            a = f.readlines()
            self.namelist = []
            for eachline in a:
                eachline = eachline.strip()
                self.namelist.append(eachline)
        return self.namelist

    def formatlinks(self, filename):
        with open(filename) as f:
            a = f.readlines()
            self.linklist = []
            for eachline in a:
                eachline = eachline.strip()
                eachline = 'https://www.' + eachline
                self.linklist.append(eachline)
        return self.linklist

    def makedict(self):
        assert len(self.namelist) == len(self.linklist)
        self.dic = {}
        for index in range(len(self.namelist)):
            self.dic[self.namelist[index]] = self.linklist[index]
        return self.dic
