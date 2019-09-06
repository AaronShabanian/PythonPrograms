legs=184
heads=63
# chicken is 2 legs and 1 head
# goat is 4 legs and 1 head
for i in range(0, 64):
    chicken=i
    goat=63-i
    test_legs=((chicken*2)+(goat*4))
    if test_legs==legs:
        print(goat," goats and ",chicken,"chickens ")
