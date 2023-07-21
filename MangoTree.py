row = int(input())
col = int(input())
tno = int(input())

if tno <= col or tno % col == 1 or tno % col == 0:
    print("True")
else:
    print("False")