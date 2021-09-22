M, N, T = map(int, input().split())

if M == N:
    result = T // M  # суммарное количество съеденных гамбургеров и чизбургеров
    ostatok = T % M  # оставшееся время
    if ostatok != 0:
        print(result, ostatok)
    else:
        print(result)
else:
    step_min = min(M, N)
    step_max = max(M, N)

    result = T // step_min
    ostatok = T % step_min

    result_test = result
    ostatok_test = ostatok

    while True:
        result_test -= 1
        ostatok_test += step_min

        if result_test == -1: break

        if ostatok_test % step_max < ostatok:
            result = result_test + ostatok_test // step_max
            ostatok = ostatok_test % step_max
        elif ostatok_test % step_max == ostatok:  # при равенстве потраченного времени
            if result < result_test + ostatok_test // step_max:
                result = result_test + ostatok_test // step_max
                ostatok = ostatok_test % step_max

    if ostatok != 0:
        print(result, ostatok)
    else:
        print(result)
