'''
    @author: Yawar Azad
'''
def predata(filename,minSup):
    items = c.defaultdict(set)
    itemset = set()
    freitems = set()
    total_item = []
    
    num_basket = 0
    for i in filename:
        num_basket += 1
        i = i.split()
        i = set(i)
        total_item +=i
        items[num_basket]=i
        itemset = itemset.union(i)
    
    total = c.Counter(total_item)
    for item in itemset:
        num = total[item]
        if float(num)/num_basket > minSup:
            freitems.add(item)
 
    return items, freitems


def gencandidate(freitems,k):
    candidate = set()
    
    if k==2:
        for x in freitems:
            for y in freitems:
                if x!=y:
                    candidate.add((x,y))
    else:
        for x in freitems:
            for y in freitems:
                if len(set(x).union(y))==k:
                    candidate.add(tuple(set(x).union(y)))
        candidate=list(candidate)        
        for c in candidate:
            subsets = getsubsets(c)
            if any( [x not in freitems for x in subsets]):
                candidate.remove(c)     
    return set(candidate)


def getsubsets(candidate):
    import itertools
    subsets=[]
    subsets.extend(itertools.combinations(candidate,len(candidate)-1))
    
    return subsets


def genfreitems(candidate,items,minSup):
    freitems = set()
    
    count=0
    pref=open('pres.txt','a')    
    for c in candidate:
        for k in items:
            if set(c).issubset(items[k]):
                count+=1
        sup=float(count)/len(items)
        if sup > minSup:
            freitems.add(c)
            print(c)
        pref.write(str(c))
            
    pref.close()
    return freitems


def main():
    k=4
    minSup=0.08
    f=open("apriori.txt","r")
    
    candidate = set()
    freitems = set()
    
    items, freitems = predata(f,minSup)
    
    for i in range(2,k+1):
        candidate = gencandidate(freitems,i)
        freitems = genfreitems(candidate,items,minSup)
   
    return freitems


if __name__=='__main__':
    import collections as c 
    main()
    
