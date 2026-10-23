def alpha_beta(depth,index,alpha,beta):
    if depth==max_limit:
        return value[index]
    
    if depth%2==0:
        best = -math.inf
        for i in range(2):
            value = alpha_beta(depth+1,index*2+i,alpha,beta)
            best = max(best,value)
            alpha = max(alpha,best)
            if alpha>=beta:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            value = alpha_beta(depth+1,index*2+i,alpha,beta)
            best = min(best,value)
            beta = min(best,beta)
            if alpha>=beta:
                break
        return best
