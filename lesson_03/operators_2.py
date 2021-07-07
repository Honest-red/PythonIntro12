"""
операторы сравнения
    >
    <
    >=
    <=
    !=
    ==
"""

print(3 < 5)
print(4 > 6)

"""
операторы присваивания
    =
    A = 6   A = A + 3   A += 3
    +   +=
    -   -=
    *   *=
    /   /=
    //  //=
    %   %=
    **  **=
    
    >>  >>=     A = A >> 3      A >>= 3
    <<  <<=
    ~   
    &   &=
    |   |=
    ^   ^=      Исключающее ИЛИ
"""

"""
Логические операторы

    and         И
    or          ИЛИ
    not         НЕ
    
    A           B           and         or          not A
    True        True        True        True        False
    True        False       False       True        False
    False       True        False       True        True
    False       False       False       False       True
"""

print(5 and 0)
print(5 and 4)

"""
Битовые операции
    ~       НЕ
    &       И
    |       ИЛИ
    ^       Исключающее ИЛИ
    
     A      B      &      |     ~ A      ^
    True   True   True   True   False   False
    True   False  False  True   False   True
    False  True   False  True   True    True
    False  False  False  False  True    False
    
    78          01001110
    95          01011111
    78 & 95     01001110    78
    78 | 95     01011111    95
    ~ 78        10110001    -79
    78 ^ 95     00010001    17
    
    78          01001010
    &           00000100
                00000000      != 0
                
    >>
    <<
    
    4 << 2      16
    4           00000100
    << 1        00001000
    << 1        00010000
    
    
    1 << 0      00000001
    1 << 1      00000010
"""



