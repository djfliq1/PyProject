import csv
import datetime
import time
import sys
import asyncio
import subprocess


def main():
    while True:
        subprocess.call("git add TimerMain.py ../test.csv", shell=True)
        time.sleep(3)
        subprocess.call("git commit -m 'AutomatedPushComplete'", shell=True)
        time.sleep(3)
        subprocess.call('git push', shell=True)
        time.sleep(3)

        set_time = 5

        try:
            when_to_stop = abs(int(set_time))


            with open("../test.csv",'a') as csv_file:
                csv_reader = csv.reader(csv_file)
                csv_writer = csv.writer(csv_file, delimiter='\t')

                csv_writer.writerow("Not So Random Test Quote")

                print("File Updated\n")

        # except KeyboardInterrupt:
        #     break
        except:
            print("Didn't Work!")

        while when_to_stop > 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end="")
            time.sleep(1)
            when_to_stop -= 1

        print()


if __name__ == '__main__':
    main()
