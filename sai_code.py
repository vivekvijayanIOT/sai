import serial
import matplotlib.pyplot as plt

#ser=serial.Serial('COM4',9600)

flowrate=[]
volume=[]

time=0
total=0
c=0
while True:
    while True:
        try:
            if (c%2==0):
                #a=int((ser.readline().decode()))
                a=raw_input("Enter the Flowrate")
                c=c+1
                print("flowrate=",a)
                flowrate.append(a)

            else:
                #b=int((ser.readline().decode()))
                b=raw_input("Enter the volume")
                c=c+1
                print("volume=",b)
                volume.append(b)
        except ValueError:
            print('no')
            a=0
        if(time!=10):
            time+=1

        else:
            time=0
            print volume
            plt.title("Volume Graph")
            plt.plot(volume)
            plt.ylabel('Volume')
            plt.xlabel('Time')
            plt.show()
            print flowrate
            plt.title("Flowrate Graph")
            plt.plot(flowrate)
            plt.ylabel('Flowrate')
            plt.xlabel('Time')
            plt.show()

            for xx in flowrate:
                total += (xx / 60) * 1000
            print("Total Quantity: "+str(total))
