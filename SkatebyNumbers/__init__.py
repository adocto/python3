if __name__ == "__main__":
    speed = 1
    N = input()
    h = input()
    heights = map(int,h.split())
    x = 0
    for x in range(1,N-1):
        if x == 0:
            speed = 1
        else:
            if heights[x] > heights[x-1]:
                speed -= 1
            else:
                speed += 1
    print(speed)
