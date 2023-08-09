
class SegmentTree:
    def __init__(self,data):
        self.tree = [0]*4*len(data)
        self.original_data = data
        self.build()
    def build(self):
        def buildHelper(idx,l,r):

            if l==r:
                self.tree[idx] = self.original_data[l]
                return
            mid = (l+r)//2
            buildHelper(2*idx+1,l,mid)
            buildHelper(2*idx+2,mid+1,r)
            self.tree[idx] = self.tree[2*idx+1]+self.tree[2*idx+2]
        buildHelper(0,0,len(self.original_data)-1)
    def update(self,idx,value):
        def update(nodeIdx,idx,value,l,r):
            if l == r:
                self.original_data[idx] +=value
                self.tree[nodeIdx] += value
                return
            mid = (l+r)//2
            if idx<=mid:
                update(2*nodeIdx+1,idx,value,l,mid)
            else:
                update(2*nodeIdx+2,idx ,value,mid+1,r)
            self.tree[nodeIdx] = self.tree[2*nodeIdx+1]+self.tree[2*nodeIdx+2]
        update(0,idx,value,0,len(self.original_data)-1)

    def query(self,l,r):
        def query(node,tl,tr,l,r):
            if l>tr or r<tl:
                return 0
            if l<=tl and tr<=r:
                return self.tree[node]
            tm = (tl+tr)//2
            return query(2*node+1,tl,tm,l,r)+query(2*node+2,tm+1,tr,l,r)
        return query(0,0,len(self.original_data)-1,l,r)
if __name__ == '__main__':
    st = SegmentTree([1,2,3,4,5])
    st.update(1,1)
    print(st.query(0,3))



