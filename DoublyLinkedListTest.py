from testing import *
from DoublyLinkedList import DLL


def main():
    p = DLL()

    test(True, DLL.is_empty, p)

    p.add_to_head(34)
    test("[34]", DLL.__str__, p)
    p.add_to_head(22)
    test("[22; 34]", DLL.__str__, p)
    p.add_to_head(98)
    test("[98; 22; 34]", DLL.__str__, p)
    p.add_to_head(56)
    test("[56; 98; 22; 34]", DLL.__str__, p)

    test(56, DLL.pop_head, p)
    test(98, DLL.pop_head, p)

    p.add_to_tail('apple')
    test("[22; 34; apple]", DLL.__str__, p)

    p.add_to_tail('ball')
    test("[22; 34; apple; ball]", DLL.__str__, p)

    test('ball', DLL.pop_tail, p)
    test("[22; 34; apple]", DLL.__str__, p)
    test('apple', DLL.pop_tail, p)
    test("[22; 34]", DLL.__str__, p)

    p.add_to_head(98)
    p.add_to_head(56)
    test("[56; 98; 22; 34]", DLL.__str__, p)

    test(True, DLL.contains, p, 22)
    test(True, DLL.contains, p, 56)
    test(False, DLL.contains, p, 100)

    p.insert(2, 'ball')
    test("[56; 98; ball; 22; 34]", DLL.__str__, p)

    p.insert(0, 'dog')
    test("[dog; 56; 98; ball; 22; 34]", DLL.__str__, p)

    p.insert(5, 'bird')
    test("[dog; 56; 98; ball; 22; bird; 34]", DLL.__str__, p)

    test(22, DLL.remove, p, 4)
    test("[dog; 56; 98; ball; bird; 34]", DLL.__str__, p)

    test('ball', DLL.remove, p, 3)
    test("[dog; 56; 98; bird; 34]", DLL.__str__, p)

    test(5, DLL.length, p)

    p.insert(1, 98)
    p.insert(1, 98)
    test(4, DLL.last_index, p, 98)


main()