while True:
    try:
        list_num = int(input())
        list_ = input().split()
        sort_ = int(input())
        lise_new = list_[:list_num]
        if sort_:
            list_ = sorted(list_,reverse=True)
        else:
            list_ = sorted(list_)
        print(" ".join(list_))
    except:
        break


