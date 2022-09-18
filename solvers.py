class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far .
        self.best_state = None
    def assignSubstring(self,s,i,j,v):
        return s[0:i]+v+s[j+1:]
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
        if(j==0):
            return c
        else:
            return chars[j-1]
    def giveTwoWord(self,s,i):
        m = self.cost_fn(s)
        min_string = s
        x1 = self.conf_matrix[s[i]]
        x1.append(s[i])
        x2 = self.conf_matrix[s[i+1]]
        x2.append(s[i+1])
        cost_array =[[]]
        for a in x1:
            for b in x2:
                    d = a + b
                    cost_stirng = self.assignSubstring(s,i,i+1,d)
                    cost = self.cost_fn(cost_stirng)
                    if(cost < m):
                        min_string = d
        return min_string
    def giveThreeWord(self,s,i):
        m = self.cost_fn(s)
        min_string = s[i:i+3]
        x1 = self.conf_matrix[s[i]]
        x1.append(s[i])
        x2 = self.conf_matrix[s[i+1]]
        x2.append(s[i+1])
        x3 = self.conf_matrix[s[i+2]]
        x3.append(s[i+2])
        cost_array =[[]]
        for a in x1:
            for b in x2:
                for c in x3:
                    d = a + b + c
                    cost_stirng = self.assignSubstring(s,i,i+2,d)
                    cost = self.cost_fn(cost_stirng)
                    if(cost < m):
                        min_string = d
        return min_string
    def giveWord(self,s,a,b):
        if(len(s)<2):
            return s[a:b]
        elif(len(s)==2):
            return self.giveTwoWord(s,a)
        for i in range(b-a-2):
            s = self.assignSubstring(s,a+i,a+i+2,self.giveThreeWord(s,a+i))
        return s[a:b]
    def search(self, start_state):
        """
        :param start_state: str Input string with spelling errors
        """
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state
        print(start_state)
        st = 0
        for j in range(len(start_state)):
            if(start_state[j]==' '):
                start_state = self.assignSubstring(start_state,st,j-1,self.giveWord(start_state,st,j))
                st = j+1
            elif(j==len(start_state)-1):
                j = j+1
                start_state = self.assignSubstring(start_state,st,j-1,self.giveWord(start_state,st,j))
        for i in range(len(start_state)-1,-1,-1):
            if(start_state[i]==' '):
                continue
            start_state = start_state [:i]+self.giveChar(i,start_state)+start_state[i+1:]
        print(start_state)
        return start_state
        raise Exception("Not Implemented.")
