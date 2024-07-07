import tkinter, customtkinter , emoji

#file that stores all our tasks
f = open("Tasks.txt","a")
f.close()

def addTask():

    viewTasks.forget()
    delTaskBut.forget()
    addTaskBut.forget()

    taskEntry = customtkinter.CTkEntry(app,width=200,height=3,placeholder_text="Type task here",text_color="white")
    taskEntry.pack(padx=10,pady=10)

    def addTaskActual():
        
        task = taskEntry.get()
        taskEntry.forget()

        if task != "":
            
            f = open("Tasks.txt", "r")
            tasksAtHand = f.readlines()
            f.close()

            if (task + "\n") not in tasksAtHand:
                
                f = open("Tasks.txt","a")
                f.writelines("{}\n".format(task))
                f.close

                Msg = emoji.emojize(":check_mark_button:") + " Task " + task + " Successfully Added"

                errorText = customtkinter.CTkTextbox(app,width=300,height=2,text_color="white")
                errorText.pack(pady=10,padx=10)

                errorText.insert(1.0,Msg)

                addActualTaskBut.forget()

                def back():
                    
                    errorText.forget()
                    backButton.forget()

                    addTaskBut.pack(padx=10,pady=10)
                    viewTasks.pack(padx=10,pady=10)
                    delTaskBut.pack(padx=10,pady=10)


                backButton = customtkinter.CTkButton(app,width=5,height=3,text=("Back"+emoji.emojize(":BACK_arrow:")),text_color="white",command=back)
                backButton.pack(padx=10,pady=10)
               
            else:

                Msg = emoji.emojize(":cross_mark_button:") + " Task " + task + " Already Exists"

                errorText = customtkinter.CTkTextbox(app,width=300,height=2,text_color="white")
                errorText.pack(pady=10,padx=10)

                errorText.insert(1.0,Msg)

                addActualTaskBut.forget()

                def back():
                    
                    errorText.forget()
                    backButton.forget()

                    addTaskBut.pack(padx=10,pady=10)
                    viewTasks.pack(padx=10,pady=10)
                    delTaskBut.pack(padx=10,pady=10)


                backButton = customtkinter.CTkButton(app,width=5,height=3,text=("Back"+emoji.emojize(":BACK_arrow:")),text_color="white",command=back)
                backButton.pack(padx=10,pady=10)
                
        
        else:

            Msg = emoji.emojize(":cross_mark_button:") + " Please enter a task before trying to add"

            errorText = customtkinter.CTkTextbox(app,width=300,height=2,text_color="white")
            errorText.pack(pady=10,padx=10)

            errorText.insert(1.0,Msg)
            addActualTaskBut.forget()  

            def back():
                
                backButton.forget()
                errorText.forget()

                addTaskBut.pack(padx=10,pady=10)
                viewTasks.pack(padx=10,pady=10)
                delTaskBut.pack(padx=10,pady=10)


            backButton = customtkinter.CTkButton(app,width=5,height=3,text=("Back"+emoji.emojize(":BACK_arrow:")),text_color="white",command=back)
            backButton.pack(padx=10,pady=10)  

    addActualTaskBut = customtkinter.CTkButton(app,width=5,height=3,text=("Finalise Addition"+emoji.emojize(":check_mark_button:")),text_color="white",command=addTaskActual)
    addActualTaskBut.pack(padx=10,pady=10)

    

def listTasks():

    viewTasks.forget()
    delTaskBut.forget()
    addTaskBut.forget()

    app.geometry("425x425")

    listedTasks = customtkinter.CTkTextbox(app,width=200,height = 325, text_color="white",bg_color="black",fg_color="grey")
    listedTasks.pack(padx=10,pady=10)

    f = open("Tasks.txt", "r")

    tasksAtHand = f.readlines()
    f.close()

    taskString = ""

    for task in tasksAtHand:
        tasksAtHand[tasksAtHand.index(task)] = str(tasksAtHand.index(task) + 1) + ":" + task 
    for task in tasksAtHand:    
        taskString = taskString + "\n" + tasksAtHand[tasksAtHand.index(task)]

    listedTasks.insert(1.0,taskString)

    def back():
            
            backButton.forget()
            listedTasks.forget()
            app.geometry("425x225")

            addTaskBut.pack(padx=10,pady=10)
            viewTasks.pack(padx=10,pady=10)
            delTaskBut.pack(padx=10,pady=10)


    backButton = customtkinter.CTkButton(app,width=5,height=3,text=("Back"+emoji.emojize(":BACK_arrow:")),text_color="white",command=back)
    backButton.pack(padx=10,pady=10) 
    

def deleteTask():

    viewTasks.forget()
    delTaskBut.forget()
    addTaskBut.forget()
    
    listedTasks = customtkinter.CTkEntry(app,width=200,height = 2, text_color="white",placeholder_text="Task to be deleted")
    listedTasks.pack(padx=10,pady=10)

    f = open("Tasks.txt", "r")

    tasksAtHand = f.readlines()
    f.close()

    def finalizeDelete():
    
        task = listedTasks.get() 
        newTask = listedTasks.get() + "\n"
        listedTasks.forget()
        
        if newTask  in tasksAtHand:

            finalButton.forget()
            tasksAtHand.remove(newTask)
            f = open("Tasks.txt","w")
            f.writelines(tasksAtHand)
            f.close

            Msg = emoji.emojize(":check_mark_button:") + " The Task " + task + " Has Been Successfully Removed."

            errorText = customtkinter.CTkTextbox(app,width=400,height=2,text_color="white")
            errorText.pack(pady=10,padx=10)

            errorText.insert(1.0,Msg)


            def back():

                backButton.forget()
                errorText.forget()
                
                addTaskBut.pack(padx=10,pady=10)
                viewTasks.pack(padx=10,pady=10)
                delTaskBut.pack(padx=10,pady=10)


            backButton = customtkinter.CTkButton(app,width=5,height=3,text=("Back"+emoji.emojize(":BACK_arrow:")),text_color="white",command=back)
            backButton.pack(padx=10,pady=10) 
    
        
        else:
            
            finalButton.forget()
            Msg = emoji.emojize(":cross_mark_button:") +"The task entered, "+ task + " is not on your current to-do list."

            errorText = customtkinter.CTkTextbox(app,width=400,height=2,text_color="white")
            errorText.pack(pady=10,padx=10)

            errorText.insert(1.0,Msg)

            def back():

                backButton.forget()
                errorText.forget()

                addTaskBut.pack(padx=10,pady=10)
                viewTasks.pack(padx=10,pady=10)
                delTaskBut.pack(padx=10,pady=10)


            backButton = customtkinter.CTkButton(app,width=5,height=3,text=("Back"+emoji.emojize(":BACK_arrow:")),text_color="white",command=back)
            backButton.pack(padx=10,pady=10) 
    
    finalButton = customtkinter.CTkButton(app,width=5,height=3,text=("Finalise Deletion"+emoji.emojize(":prohibited:")),text_color="white",command=finalizeDelete)
    finalButton.pack(padx=10,pady=10) 
    
            

#App Window
app = customtkinter.CTk()
app.geometry("425x225")
app.title("To-do List")

welcome= customtkinter.CTkLabel(app,height=2,width=5,text="Welcome to the best app for keeping tracking of your tasks",text_color="white")
welcome.pack()

#buttons
addTaskBut = customtkinter.CTkButton(app,width=5,height=3,text=("Add Task " +emoji.emojize(":clipboard:")),text_color="white",command=addTask)
addTaskBut.pack(padx=10,pady=10)


viewTasks = customtkinter.CTkButton(app,width=5,height=3,text=("View Tasks "+emoji.emojize(":eye:") ),text_color="white",command=listTasks)
viewTasks.pack(padx=10,pady=10)

delTaskBut = customtkinter.CTkButton(app,width=5,height=3,text=("Delete Task "+emoji.emojize(":prohibited:")),text_color="white",command=deleteTask)
delTaskBut.pack(padx=10,pady=10)


app.mainloop()

#functions


    
