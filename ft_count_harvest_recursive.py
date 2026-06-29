def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(n):
        nbr_next = n - 1
        if nbr_next > 0:
            helper(nbr_next)
        print("Day:", n)
    helper(n)
    print("Harvest time !")
