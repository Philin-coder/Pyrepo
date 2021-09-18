def stringer(m_str: str) -> str:
    res = ''.join(i for i in m_str if not i.isdigit())
    print(res)
    with open('проба' + '.' + 'txt', 'w', encoding='utf-8') as fp:
        print(res, file=fp, sep="\n")
    return res


if __name__ == '__main__':
    stringer(m_str=input())
