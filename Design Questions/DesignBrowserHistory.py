class BrowserHistory:
    def __init__(self, homepage: str):
        self.for_ward = [homepage]
        self.backward = []

    def visit(self, url: str) -> None:
        self.backward.clear() 
        self.for_ward.append(url)

    def back(self, steps: int) -> str:
        while len(self.for_ward)>1 and steps>0:
            curr = self.for_ward.pop()
            self.backward.append(curr)
            steps-=1
        return self.for_ward[-1]

    def forward(self, steps: int) -> str:
        while len(self.backward)>0 and steps>0:
            curr = self.backward.pop()
            self.for_ward.append(curr)
            steps-=1
        return self.for_ward[-1]
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)