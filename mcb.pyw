#This “multiclipboard” will be named mcb.pyw (since “mcb” is shorter to type
#than “multiclipboard”). The .pyw extension means that Python won’t show a Terminal window when it runs this program.

#The program will save each piece of clipboard text under a keyword.
#For example, when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam.
#This text can later be loaded to the clipboard again by running py mcb.pyw spam. And if the user forgets
#what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard

import shelve,pyperclip, sys

mcbshelf=shelve.open('mcb')

#save clipboard content
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv) ==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])

mcbshelf.close()
#print(sys.argv)