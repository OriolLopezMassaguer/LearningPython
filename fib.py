from typing import List, Callable, Any


def fib(n: int) -> int:
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
    return b


def fib2(n: int) -> List[int]:
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def ask_ok(prompt: str, retries: int = 4, reminder: str = 'Please try again!'):
    while True:
        ok: str = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(".. This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "! ")


def cheeseshop(kind, *arguments, **keywords):
    print('-- Do you have any', kind, "?")
    print('-- I\'m sorry, we\'re all out of', kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


f: Callable[[int, int], int] = lambda a, b: a + b

squares: List[Any] = [x**2 for x in range(10)]

squares2: List[int] = list(map(lambda x: x**2,range(10)))

pseudo_cartesian = [(x,y) for x in range(3)  for y in range(10) if x!=y]



set1 = {1,2,1,1,1}

tel = { 'a': 100, 'b':200}