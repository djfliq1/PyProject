import csv
import time
import subprocess


def main():
    def file_reset():
        try:
            # A test.csv file is used as the file to be updated.
            with open("../test.csv", 'w') as csv_file:

                dataR = csv_file.read()
                dataR_set = set(dataR)
                clean_file = open("../test.csv", 'r+')

            for line in dataR_set:
                clean_file.write(line)



        # To break out of the loop, in your terminal you can just press ctrl+break
        except:
            print("File reset to origin.")

    def file_updater():
        try:
            when_to_stop = abs(int(set_time))

            # A test.csv file is used as the file to be updated.
            with open("../test.csv", 'a') as csv_file:
                csv_reader = csv.reader(csv_file)
                csv_writer = csv.writer(csv_file, delimiter='\t')

                csv_writer.writerow("Not So Random Test Quote")

                print("File Updated")

        # To break out of the loop, in your terminal you can just press ctrl+break
        except:
            print("Your file/s were not updated!")

    while True:
        # adds the two files to be committed
        subprocess.call("git add TimerMain.py ../test.csv", shell=True)
        # These timers just help slow the process down so there aren't any overlapping of processes
        time.sleep(1)
        # The commit to GitHub
        subprocess.call("git commit -m 'AutomatedPushComplete'", shell=True)
        time.sleep(2)
        # Pushes the update to the repository
        subprocess.call('git push', shell=True)
        time.sleep(1)
        # Checks the csv file to see if the line count is m20 or more so it knows
        # when to erase the file and start over
        d_data = open("../test.csv", 'r')
        data = d_data.read()
        numOfLines = len(data.splitlines())
        # Have to make sure you close the csv file or neither of the definitions will work correctly
        d_data.close()

        if (numOfLines >= 20):
            file_reset()
        else:
            file_updater()

        time.sleep(1)

        # This is the countdown timer, in seconds. Here is where you set how often you want to update your repository
        set_time = 10800
        when_to_stop = abs(int(set_time))

        # Below is the structure of the countdown timer and how it will display in your terminal
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
