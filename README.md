# Automated-Cover-Letter-Generator
I use this python script to automatically generate new Cover Letters for job apps. I made it with the help of this article: https://medium.com/@arjunbastola/tired-of-creating-new-cover-letter-for-every-job-you-apply-to-use-python-to-automate-it-c5516da9011a

First install the necessary libraries. There are two and they can be installed with the following command lines in your terminal/Command Prompt:

pip install docxtpl

pip install docx2pdf


To use it, save the python code to a folder. That folder should also contain your Cover Letter template, titled "CLtemplate.docx" (I have saved my template as a reference)

Replace any instances of the company's name with "{{company}}" and any instances of the position title as "{{role}}" in your CL template.

After that, simply navigate to your file folder in the Terminal, and execute the following line of code:
python newcl.py

You will be prompted to enter the company and position. After that, your new Cover letter will show up in the folder you chose in word and pdf format!

Note-you may be prompted to save file names through your finder after running the program the first couple times you run the program; this is a glitch. Just hit cancel and nothing bad will happen. I stopped having this issue after making my third Cover Letter.



