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
    def sortfun(self,e):
        return e[1]
    def beam5(self,states,i,n,start_state):
        self.best_state = states[0]
        if(i==n):
            return states[0]
        if(start_state[i] == ' '):
            return self.beam5(states,i+1,n,start_state)
        char = self.conf_matrix[start_state[i]]
        chars = [start_state[i]] + char
        newstates = []
        for state in states:
            for c in chars:
                state = state[:i]+c+state[i+1:]
                newstates.append([state,self.cost_fn(state)])
        newstates.sort(key=self.sortfun)
        nextstates =[]
        k = 50
        if(k>len(newstates)):
            k = len(newstates)
        for j in range(k):
            nextstates.append(newstates[j][0])
        return self.beam5(nextstates,i+1,n,start_state)
    def search(self, start_state):
        """
        :param start_state: str Input string with spelling errors
        """
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state
        print(start_state)
        states = []
        states.append(start_state)
        chars = self.conf_matrix[start_state[0]]
        for c in chars:
            start_state = c + start_state[1:]
            states.append(start_state)
        final_state = self.beam5(states,1,len(start_state),start_state)
        start_state = final_state
        for i in range(len(start_state)-1,-1,-1):
            if(start_state[i]==' '):
                continue
            start_state = start_state [:i]+self.giveChar(i,start_state)+start_state[i+1:]
            self.best_state = start_state
        return start_state
        raise Exception("Not Implemented.")
