from tkinter import *
from tinder_backend import *
from tkinter import messagebox


class TinderGUI:
    def __init__(self):
        self.root = Tk()
        self.root.maxsize(300, 900)
        self.root.title("TINDER")
        self.tinderBackend = tinderBackend()
        lbl = Label(self.root, text="WELCOME TO TINDER", width=25, height=3, bg="White", font=("Courier", 12))
        lbl.grid(row=0, column=0)

        btnLogin = Button(self.root, text="Login", width=12, height=2, bg="SkyBlue",
                          command=lambda: self.userlogin())
        btnLogin.grid(row=1, column=0, padx=10, pady=10)

        btnRegister = Button(self.root, text="Register", width=12, height=2, bg="SkyBlue",
                             command=lambda: self.userRegister())
        btnRegister.grid(row=2, column=0, padx=10, pady=10)

        btnExit = Button(self.root, text="Exit", width=12, height=2, bg="SkyBlue",
                         command=lambda: self.root.destroy())
        btnExit.grid(row=3, column=0, padx=10, pady=10)

        self.root.mainloop()  # main loop always at end

    def userlogin(self):
        child = Toplevel(master=self.root)
        child.maxsize(500, 900)
        child.title("Login")
        lblEmail = Label(child, text="Email", width=10, height=2, font=("Courier", 12))
        lblEmail.grid(row=0, column=0)
        enteremail = Entry(child, width=20)
        enteremail.grid(row=0, column=1, padx=20, pady=20)
        lblPassword = Label(child, text="Password", width=10, height=2, font=("Courier", 12))
        lblPassword.grid(row=2, column=0)
        enterpass = Entry(child, width=20, show='^')
        enterpass.grid(row=2, column=1, padx=20, pady=20)
        btnsubmit = Button(child, text="Submit", width=12, height=2, bg="SkyBlue",
                           command=lambda: self.uservalidate(child,enteremail.get(), enterpass.get()))
        btnsubmit.grid(row=3, column=0, padx=20, pady=20)

    def userRegister(self):
        child = Toplevel(master=self.root)
        child.maxsize(300, 900)
        child.title("Registration")

        lblName = Label(child, text="Name", width=10, height=2, font=("Courier", 12)).grid(row=0, column=0)
        entername = Entry(child, width=20)
        entername.grid(row=0, column=1, padx=20, pady=20)

        lblEmail = Label(child, text="Email", width=10, height=2, font=("Courier", 12)).grid(row=1, column=0)
        enteremail = Entry(child, width=20)
        enteremail.grid(row=1, column=1, padx=20, pady=20)

        lblPassword = Label(child, text="Password", width=10, height=2, font=("Courier", 12)).grid(row=2, column=0)
        enterpass = Entry(child, width=20, show='^')
        enterpass.grid(row=2, column=1, padx=20, pady=20)

        lblGender = Label(child, text="Gender", width=10, height=2, font=("Courier", 12)).grid(row=3, column=0)
        entergender = Entry(child, width=20)
        entergender.grid(row=3, column=1, padx=20, pady=20)

        lblCity = Label(child, text="City", width=10, height=2, font=("Courier", 12)).grid(row=4, column=0)
        entercity = Entry(child, width=20)
        entercity.grid(row=4, column=1, padx=20, pady=20)

        btnsubmit = Button(child, text="Submit", width=12, height=2, bg="SkyBlue",
                           command=lambda: self.userreg(child, entername.get(),enteremail.get(),
                                                        enterpass.get(),entergender.get(),entercity.get()))
        btnsubmit.grid(row=5, column=1, padx=20, pady=20)

    def menu(self,name):
        self.menu = Toplevel(master=self.root)
        self.menu.maxsize(500, 900)
        self.menu.title("Main Menu")
        na= StringVar()
        lblWelcome=Label(self.menu, textvariable=na, width=30, height=2, font=("Courier", 12)).grid(row=0, column=0)
        na.set("Welcome! %s"%(name))
        btnViewChoice = Button(self.menu, text="View all Choices", width=20, height=2, bg="SkyBlue"
                               , command=lambda: self.viewall())
        btnViewChoice.grid(row=1, column=0)
        btnViewRecieved = Button(self.menu, text="View Received Proposals", width=20, height=2, bg="SkyBlue"
                                 ,command=lambda: self.recieved())
        btnViewRecieved.grid(row=2, column=0)
        btnViewsent = Button(self.menu, text="View Sent Proposals", width=20, height=2, bg="SkyBlue"
                             ,command=lambda: self.sent())
        btnViewsent.grid(row=3, column=0)
        btnViewMatches = Button(self.menu, text="View Matches", width=20, height=2, bg="SkyBlue"
                                ,command=lambda: self.matches())
        btnViewMatches.grid(row=4, column=0)
        btnLogout = Button(self.menu, text="Logout", width=20, height=2, bg="SkyBlue"
                           ,command=lambda: self.menu.destroy())
        btnLogout.grid(row=5, column=0)

    def uservalidate(self, child, uemail, upass):
        st = self.tinderBackend.verifyuser(uemail, upass)
        if st != "":
            messagebox.showinfo("Success","Successful Login!")
            child.destroy()
            self.menu(st)
        else:
            messagebox.showinfo("Error!","Invalid User Credential")

    def userreg(self, child, name, email, passw, gen, city):
        st = self.tinderBackend.reg(name, email, passw, gen, city)
        if st == "Registration successful !!":
            messagebox.showinfo("Registration Successful", "Registration Done")

            child.destroy()
        else:
            messagebox.showinfo("Registration Unsuccessful", "Registration Failed")

    def viewall(self):
        ViewU= Toplevel(master=self.menu)
        ViewU.maxsize(900,1000)
        ViewU.title("User list")
        userlist=self.tinderBackend.view_users()
        c=0
        lbluserID = Label(ViewU, text="ID", width=10, height=3,
                        font=("Courier", 12))
        lbluserID.grid(row=0, column=0)
        lbluserN = Label(ViewU, text="Name", width=10, height=3,
                        font=("Courier", 12))
        lbluserN.grid(row=0, column=1)
        lbluserG = Label(ViewU, text="Gender", width=10, height=3,
                        font=("Courier", 12))
        lbluserG.grid(row=0, column=2)
        lbluserC = Label(ViewU, text="City", width=10, height=3,
                        font=("Courier", 12))
        lbluserC.grid(row=0, column=3)
        lbluserP = Label(ViewU, text="Propose?", width=10, height=3,
                         font=("Courier", 12))
        lbluserP.grid(row=0, column=4)
        for i in userlist:
            a=0
            for v in [0,1,4,5]:
                lbluser = Label(ViewU, text="%s" %(i[v]), width=10, height=3,
                                font=("Courier", 12))
                lbluser.grid(row=(c+1),column=a)
                a=a+1
            btnPropose = Button(ViewU, text="Send", width=10, height=3, bg="SkyBlue"
                                ,command= lambda i=i: self.tinderBackend.propose(i[0]))
            btnPropose.grid(row=(c+1),column=(a+1))
            c=c+1

    def sent(self):
        ViewU = Toplevel(master=self.menu)
        ViewU.maxsize(900, 1000)
        ViewU.title("Sent Proposals")
        sent_list=self.tinderBackend.view_user_proposed()
        c = 0
        lbluserID = Label(ViewU, text="ID", width=10, height=3,
                          font=("Courier", 12))
        lbluserID.grid(row=0, column=0)
        lbluserN = Label(ViewU, text="Name", width=10, height=3,
                         font=("Courier", 12))
        lbluserN.grid(row=0, column=1)
        lbluserG = Label(ViewU, text="Gender", width=10, height=3,
                         font=("Courier", 12))
        lbluserG.grid(row=0, column=2)
        lbluserC = Label(ViewU, text="City", width=10, height=3,
                         font=("Courier", 12))
        lbluserC.grid(row=0, column=3)
        for i in sent_list:
            a = 0
            for v in [3, 4, 7, 8]:
                lbluser = Label(ViewU, text="%s" % (i[v]), width=10, height=3,
                                font=("Courier", 12))
                lbluser.grid(row=(c + 1), column=a)
                a = a + 1
            c = c + 1

    def recieved(self):
        ViewU = Toplevel(master=self.menu)
        ViewU.maxsize(900, 1000)
        ViewU.title("Received Proposals")
        rec_list=self.tinderBackend.view_user_proposals()
        c = 0
        lbluserID = Label(ViewU, text="ID", width=10, height=3,
                          font=("Courier", 12))
        lbluserID.grid(row=0, column=0)
        lbluserN = Label(ViewU, text="Name", width=10, height=3,
                         font=("Courier", 12))
        lbluserN.grid(row=0, column=1)
        lbluserG = Label(ViewU, text="Gender", width=10, height=3,
                         font=("Courier", 12))
        lbluserG.grid(row=0, column=2)
        lbluserC = Label(ViewU, text="City", width=10, height=3,
                         font=("Courier", 12))
        lbluserC.grid(row=0, column=3)
        lbluserP = Label(ViewU, text="Propose?", width=10, height=3,
                         font=("Courier", 12))
        lbluserP.grid(row=0, column=4)
        for i in rec_list:
            a = 0
            for v in [3, 4, 7, 8]:
                lbluser = Label(ViewU, text="%s" % (i[v]), width=10, height=3,
                                font=("Courier", 12))
                lbluser.grid(row=(c + 1), column=a)
                a = a + 1
            btnPropose = Button(ViewU, text="Propose Back", width=10, height=3, bg="SkyBlue"
                                , command=lambda i=i: self.tinderBackend.propose(i[0]))
            btnPropose.grid(row=(c + 1), column=(a + 1))
            c = c + 1

    def matches(self):
        ViewU = Toplevel(master=self.menu)
        ViewU.maxsize(900, 1000)
        ViewU.title("Matches")
        match_list = self.tinderBackend.view_user_matches()
        c = 0
        lbluserID = Label(ViewU, text="ID", width=10, height=3,
                          font=("Courier", 12))
        lbluserID.grid(row=0, column=0)
        lbluserN = Label(ViewU, text="Name", width=10, height=3,
                         font=("Courier", 12))
        lbluserN.grid(row=0, column=1)
        lbluserG = Label(ViewU, text="Gender", width=10, height=3,
                         font=("Courier", 12))
        lbluserG.grid(row=0, column=2)
        lbluserC = Label(ViewU, text="City", width=10, height=3,
                         font=("Courier", 12))
        lbluserC.grid(row=0, column=3)
        for i in match_list:
            a = 0
            for v in [3, 4, 7, 8]:
                lbluser = Label(ViewU, text="%s" % (i[v]), width=10, height=3,
                                font=("Courier", 12))
                lbluser.grid(row=(c + 1), column=a)
                a = a + 1
            c = c + 1
        btnOutput = Button(ViewU, text="Print Matches", width=20, height=2, bg="SkyBlue",
                           command=lambda: self.tinderBackend.printer())
        btnOutput.grid(row=(c+1),column=2)


ob = TinderGUI()