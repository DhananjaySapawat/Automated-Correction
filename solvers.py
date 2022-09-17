class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far .
        self.best_state = None

    def giveWord(self,w1,w2,w3):
        return "hello"
    def giveChar(self,i,start_state):
        c = start_state[i]
        cost = 5*[0]
        cost[0] = self.cost_fn(start_state)
        chars = self.conf_matrix[start_state[i]]
        for k in range(4):
            start_state = start_state [:i]+chars[k]+start_state[i+1:]
            cost[k+1] = self.cost_fn(start_state)
        m = cost[0]
        j = 0
        for k in range(1,5):
            if(cost[k] < m):
                if(i==0):
                    print(cost[k],m)
                m = cost[k]
                j = k
        if(i==8):
            print(c,": ",cost[0])
            for k in range(4):
                print(chars[k],": ",cost[k+1])
        if(j==0):
            return c
        else:
            return chars[j-1]
    def giveCharForWord(self,w,j):
        if(len(w)-j < 3):
            return w
        a = 3*[0]
        for i in range(3):
            a[i] = self.conf_matrix[w[j+i]]
            a[i].append(w[j+i])
        our = [10000000000000,w]
        for x1 in a[0]:
            for x2 in a[1]:
                for x3 in a[2]:
                    w = w[:j] + x1 + w[j+1:]
                    w = w[:j+1] + x2 + w[j+2:]
                    w = w[:j+2] + x3 + w[j+3:]
                    if(self.cost_fn(w)< our[0]):
                        our[0] = self.cost_fn(w)
                        our[1] = w
        return w[j]


    def giveWord(self,i,w):
        for j in range(len(w)):
            w = w[:j] + self.giveCharForWord(w,j) + w[j+1:]
        return w
    def search(self, start_state):
        """
        :param start_state: str Input string with spelling errors
        """
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state
        """
                s = 0
                r = 0
                for i in range(len(start_state)):
                    if(start_state[i]==" " or i == len(start_state)-1):
                        if(i == len(start_state)-1):
                            r = i+1
                        print(s,r)
                        start_state = start_state.replace(start_state[s:r],self.giveWord(s,r,start_state))
                        s = i+1

                    r = i + 1
        """
        words = start_state.split()
        str = " "
        for i in range(len(words)):
            words[i] = self.giveWord(i,words[i])
        sentence = str.join(words)
        print(sentence)
        print(start_state)
        for i in range(len(start_state)-1,-1,-1):
            if(start_state[i]==' '):
                continue
            start_state = start_state [:i]+self.giveChar(i,start_state)+start_state[i+1:]
        print(start_state)
        return start_state
        raise Exception("Not Implemented.")
