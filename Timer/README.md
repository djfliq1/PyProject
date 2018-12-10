<<<<<<<PyProject
===

###An automation project
___
##Version 1.01
The version number is arbitrary but will be used at a later date for version matching.
If the `README.md` file version and the app versions don't match, the app will not work.
There will be a very large number of versions
in the actual project due to the nature of the project automation.
___
##Purpose:
The purpose of this app was to test simple automation with the use of Github.
___
##File Reset
This definition `def file_reset():` is used to reset the csv file "test.csv". 
The purpose is to ensure the file doesn't get so large it becomes difficult
to update. This function will only be initiated if the line count is greater
than 20. The definition is enveloped in a try statement.

Get the file you want to work with and set your variables: 
```
    with open("../test.csv", 'w') as csv_file:

        dataR = csv_file.read()
        dataR_set = set(dataR)
        clean_file = open("../test.csv", 'r+')
```
The function iterates through each line and clears the data and prints
confirmation this function has been completed:
```
    for line in dataR_set:
        clean_file.write(line)



# To break out of the loop, in your terminal you can just press ctrl+break
except:
    print("File reset to origin.")
```
___
##File Updating
This function `def file_updater():` is the heart of the contribution to github. 
With this function you make a snippet "Not so random test" as the updated
contribution on a new line. This will occur until you reach 20 lines. This
function is also enveloped inside a try statement.

When the timer reaches zero and the line count is less than 20:

```try:
    when_to_stop = abs(int(set_time))

    #test.csv file is used as the file to be updated.
    with open("../test.csv", 'a') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(csv_file, delimiter='\t')

        csv_writer.writerow("Not So Random Test Quote")

        print("File Updated")
```
A confirmation is printed on command line.
``` To break out of the loop, in your terminal you can just press ctrl+break
except:
    print("Your file/s were not updated!")
```
___

##Timer
The timer can be set to whatever you like. It has to be set in seconds for
the code to write on the console in a more natural human readable format.
When this countdown reaches zero the ` while True:` loop begins.

This code is the timer:
```
set_time = 7200
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
```
___
##While True Loop
When the timer reaches zero, the Github repository is prepared for
updating and the `../test.csv` file is scanned for line count.
If the line count is greater than 20 `def file_reset():` is
selected. If the line count is less than 20 `def file_updater():`
is selected.
___
###Contact
I only want to be the best developer I can be. If you have pointers or advice,
please email me at: derklespunk@gmail.com
>>>>>>> e432abfc188b66a26931619385411039300c7fd7
