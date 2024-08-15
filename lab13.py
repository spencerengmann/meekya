sum = data[0]
FOR i <- 1 ...n
    sum += data[i]
sum_largest <- sum

FOR i_remove <- 0 ... length data - n
    i_add = i_remove + n 
    sum <- sum - data[i_remove] + data[i_add] 
    IF sum > sum_largest
        sum_largest <- sum

RETURN sum_largest/n 