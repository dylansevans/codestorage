import coins

headsRuns = 0
j = 0

while j < 1000000:
    if coins.run():
        headsRuns += 1
    j+=1

print(headsRuns/1000000)