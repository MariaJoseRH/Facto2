def factorizar (number : int) -> int:
    counter=1
    facto2=1
    while counter <= number:
        facto2*=counter
        counter+=1
    return facto2
