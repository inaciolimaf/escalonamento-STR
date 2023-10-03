def cargaCumulativa(i, P, C, ts):
    uList = []
    wList = []
    for t in range(1, ts):
        u = 0
        w = 0
        for j in range(0, i):
            w += (t/P[j])*C[j]
        u = w/t
        uList.append(u)
        wList.append(w)
        
    return {"w": wList, "u": uList}
        
if __name__ == "__main__":
    # print(cargaCumulativa(1,[60,1],[6, 0.015], 60))
    for i in cargaCumulativa(2,[60,1],[6, 0.015], 60)['u']:
        print(i)
        if i>1:
            print("ERRO")
    
        