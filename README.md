# handy-python-data-scripts
This is a collection of python data scripts to help evaluate datasets. 

##Estimate Size of Data To Be Loaded Into RStudio usage:##
#Prerequisites: 
  #Install Python
  #Have a datafile that you can guess what types of data are being used. 
  #Script currently supports atomics. More complex datatypes to follow
  
  #Usage
  1. Download to a working directory where you have python installed.
  2. Use command prompt to run python script
  3. The console shows a series of questions. Answering these should lead to a rough estimate of the working memory needed to load a file into physical memory (this is R after all).
  
  #Explanation of formula:
  
  I use a general formula of number of rows times number of columns times rough estimate (in bytes) of data type's size. Thus, a numeric (in R) is 8 bytes, an integer is 4 bytes, and a character is encoded at 1 byte *per character*. I then multiply the resulting size by 2, since overhead nearly doubles the size of a datafile as it is loaded into physical memory.
