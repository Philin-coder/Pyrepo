def isprime(n):
    m_list = []
    for i in range(n + 1):
        m_list.append(i)
    m_list[1] = 0
    i = 2
    while i <= n:
        if m_list[i] != 0:
            j = i + i
            while j <= n:
                m_list[j] = 0
                j = j + i
        i += 1
    m_list = set(m_list)
    m_list.remove(0)
    return m_list


if __name__ == '__main__':
    print(*isprime(n=int(input())))
