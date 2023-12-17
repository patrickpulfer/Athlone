import math

maximumSegmentSize = int(input("Enter the maximum segment size: "))
roundTripTime = float(input("Enter the round-trip time: "))
probabilityOfPacketLoss = float(input("Enter the probability of packet loss: "))

limit = maximumSegmentSize / (roundTripTime * (math.sqrt(probabilityOfPacketLoss)))


print(f"Limit is {limit:.2f}")