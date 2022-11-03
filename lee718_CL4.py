# %% [markdown]
# # Computing 4 Assignment
# 

# %% [markdown]
# ---
# ## Background
# 
# You are a part of a team that is responsible for maintaining the quality of an app (which may or may not involve slicing fruit mid-air). Your team has prepared an update for improving app graphics, where 4 update versions are available for different users.
# 
# **You are responsible for implementing a system to determine which app update will be installed on various devices depending on their device operating system and time of last app update on their device.**
#  
# 
# Your system will be provided with a list of user's information, following the following format: 
# 
# <br>
# \begin{align}
#   \texttt{[‘serialNum’, ‘OS Type’, ‘OS Version’, 'Update Date']}\tag{1}
# \end{align}
# <br>
# 
# Each entry in the sub-list is explained below:
# 
# |   |   |
# |---|:--|
# |**serialNum** |A string with length 8 that represents the smartphone's serial number.   |
# |**OS Type**   |A string representing operating system type with the value iOS or Android.  |
# |**OS Version**|A string representing operating system version.  |
# |**Update Date**|A string representing the latest app update date on that device (YYYY-MM-DD)   |
# 
# 
# 
# The following list of lists provides an example of data used by your system. Each sub-list follows the format given in (1). There are 3 devices in this example:
# 
# ```
# devices = [
# ['BX001321','iOS', '12.0' ,'2019-01-03'],
# ['GX021629','Android', '11.0', '2019-08-06'],
# ['BX101129','iOS', '8.0', '2019-05-22']]
# ```
# 
# <br>
# 
# The update consideres two operating systems: MAC **iOS** or **ANDROID** OS. There are 4 different app updates available, and are compatible with different devices depending on the **OS Type**, **OS Version**, and **Update Date**. The following table depicts this set of criteria for each update version:
# 
# \begin{align}
#   \texttt{Table 1: Criteria to determine app update version}
# \end{align}
# 
# 
# | OS Type |  OS Version | App Update Criteria  | App Update Version| 
# |---|:--|:--|---|
# | **iOS**  | - Version 8.0 or higher  | - At any date of last update | Version 1   |
# | **iOS**  | - Version less than 8.0  | - At any date of last update | No Update   |
# | **Android**  | - Version 10.0 or higher  | - At any date of last update | Version 2   |
# | **Android**  | - Version 8.0 to 10.0 (not including 10.0)  | - Last update between **January** and **June** | Version 3  |
# | **Android**  | - Version 8.0 to 10.0 (not including 10.0)  | - Last update between **July** and **December** | Version 4  |
# | **Android**  | - Version less than 8.0  | - At any date of last update | No Update   |
# 
# 
# <br>
# 
# Given this information, your task is to generate a list of devices and their update version required. The steps in the requirements section will help you achieve this task.

# %% [markdown]
# ---
# ## Program Requirements (12 marks)
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. 
# 
# 1. Define a function **update_required**(*device_info*):
#   - ***device_info***: A *list* containing device and app information in the form of (1).
#       
#       \begin{align}
#   \texttt{[‘serialNum’, ‘OS Type’, ‘OS Version’, 'Update Date']}\tag{1}
# \end{align}
# 
#    - Begin by defining the OS Version as a local variable in the form of a float (you can copy and paste this line into your function):      
#          OSVersion = float(device_info[2])
#    - Using a conditional statement, determine if the device requires an update or not (You only need the OS Version to do this!) 
#    - **Return**: A *Boolean* denoting whether an update is required or not, given the criteria in Table 1. (True if the device met the criteria to require an update, otherwise false)
# 
# 
# 2. Define a function **determine_update**(*device_info*):
#   - ***device_info***: A *list* containing device and app information in the form of (1). 
#   - Begin by defining local variables needed for comparisson (you can copy and paste these lines into your function): 
#          update_req = update_required(device_info) # a boolean representing if an update is required
#          OSType = device_info[1]
#          OSVersion = float(device_info[2])
#          month = int((device_info[3]).split('-')[1]) # Split the date by -, take the middle element, convert to int
# 
#    - This function should compare the local variables through multiple nested conditionals to determine which update version is required.
#    - **Return**: A *string* indicating which update version is required. These **MUST** be typed exactly as seen in column four (App Update Version) of Table 1.
#    
# 
# 3. Define a function **determine_device_update**(devices):
#   - ***devices***: A *list of lists* containing the information of all devices, where each entry is in the form of (1).
#   - Begin by defining an empty list that will hold the serial number and version number for devices with an app that requires an update
#   - Define a for-loop that iterates through each sub-list in the list ***devices***. Each sub-list represents a device's information in the form of (1).  
#   - Within the for-loop, use conditional statement(s) to determine:
#         - If the app on that device needs an update: create a list in the format: ['Serial Number' , 'Update Version']. Then append this list to the list you previously defined within this function. 
#         - If the app on that device does not need an update: skip that device *(such that this device will not be included in the final list of devices and their required update version)*
#   - **Return**: A *list of lists* of serial numbers and update versions (both as strings) of only the devices that require an app update.  

# %% [markdown]
# ---
# ## Implementation
# Please define all functions in the cell below

# %%
#********************************************
# Write your update_required function below: (4 marks)
#********************************************
def update_required(device_info):
    return float(device_info[2]) >= 8.0 

#********************************************
# Write your determine_update function below: (4 marks)
#********************************************
def determine_update(device_info):
    if update_required(device_info):
        OSType = device_info[1]
        OSVersion = float(device_info[2])
        if OSType == 'iOS':
            return "Version 1"
        else:
            if OSVersion >= 10.0:
                return "Version 2"
            month = int((device_info[3]).split('-')[1])
            if month <= 6:
                return "Version 3"
            return "Version 4"

#********************************************
# Write your determine_device_update function below: (4 marks)
#********************************************
def determine_device_update(devices):
    serial_and_updates = []
    for i in devices:
        if update_required(i):
            serial_and_updates.append([i[0], determine_update(i)])
    return serial_and_updates

# %% [markdown]
# ---
# ## Testing
# 
# The cell below contains a main function that you can use to test your functions. 
# 
# ### Important 
# Run the cell where you implemented your functions first and ensure it raises no errors. Then, run the cell below with the main function to verify that your code works correctly with the provided input. The following message should be printed after the main() function above is run:
# 
# >[['GX010365', 'Version 1'], ['BX041085', 'Version 2'], ['GX031153', 'Version 3'], ['BX601829', 'Version 1'], ['BX481436', 'Version 1'], ['GX301320', 'Version 4']]
# 
# Note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is not graded, so feel free to modify the code as you wish!
# 

# %%
# TESTING
def main():
    devices = [['GX010365', 'iOS', '8.1', '2019-04-10'], #Version 1
              ['BX041085', 'Android', '12.0', '2019-09-13'], #Version 2
              ['BX031112', 'Android', '5.0', '2019-02-13'], #No Update
              ['BX210529', 'iOS', '7.0', '2019-11-15'], #No Update
              ['GX031153', 'Android', '9.0', '2019-04-11'], #Version 3
              ['BX601829', 'iOS', '9.0', '2019-04-28'], #Version 1
              ['BX481436', 'iOS', '10.1', '2019-01-10'], #Version 1
              ['GX301320', 'Android', '9.0', '2019-07-13']] #Version 4
    device_updates = determine_device_update(devices)
    print(device_updates)
main()

# %% [markdown]
# ---
# ## Reflective Questions
# 
# 1. You created two functions: **update_required** and **detemine_update**. Was it benificial to create two seperate functions? How would your whole program be different if you did not include the **update_required** function?
# 
# 2. You used a for loop in the **determine_device_update** function. Is it possible to use a while loop? Is there a benefit to using a while loop over a for loop? If not, can you think of a scenario where a while loop would be more beneficial?
# 
# Please answer all questions in the cell below!

# %% [markdown]
# ```
# 1. The update_required function is not necessary as it is simply one line returning a boolean value. This can be implemented in the first conditional statement of the determine_update function instead. However, one can argue that it is beneficial since it allows the code to be better readable and easier to find where the errors may be coming from and edit accordingly. 
# 
# 2. It is possible to use while loop. There is no benefit of using a while loop over a for loop since while loops are slower than for loops and because there would need to be more code to make sure the while loop terminates, leaving more places prone to error. A while loop would be more beneficial if there was an unknown number of devices to check for updates. 
# ```

# %% [markdown]
# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 4 dropbox on avenue with the naming convention: macID_CL4.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day of your Lab section at 11:59 PM EST
# 
# Late labs will not be accepted


