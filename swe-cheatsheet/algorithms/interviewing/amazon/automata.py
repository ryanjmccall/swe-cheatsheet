def cellCompete(states, days):
    for _ in range(days):
        xor(states)
    return states


def xor(arr):
    prev = 0
    for i in range(len(arr)):
        nxt = 0 if i == len(arr) - 1 else arr[i + 1]
        arr[i], prev = prev ^ nxt, arr[i]


def t():
   print(cellCompete(states=[1, 0, 0, 0, 0, 1, 0, 0], days=1))
   print(cellCompete(states=[1, 1, 1, 0, 1, 1, 1, 1], days=2))
  # [0, 1, 0, 0, 1, 0, 1, 0]
# [0, 0, 0, 0, 0, 1, 1, 0]

t()
