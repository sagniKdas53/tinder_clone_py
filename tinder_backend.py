import mysql.connector
import os
from tkinter import messagebox

class tinderBackend:
    def __init__(self):
        self.conn = mysql.connector.connect(user="root",password="password",host="localhost",database="tinder")
        # i have used a password in my database be sure to remove it if you intend to test on your local database
        self.mycursor=self.conn.cursor()

    def verifyuser(self, email, password):
        self.mycursor.execute("""
                SELECT * from `users` WHERE
                `email` LIKE '%s' and `password` LIKE '%s' 
                """ % (email, password))

        user_list = self.mycursor.fetchall()
        c = 0
        for i in user_list:
            c = c + 1
            self.current_user_id = i[0]

        if c == 1:
            return i[1],
        else:
            return ""

    def reg(self, name, email, password, gender, city):
        self.mycursor.execute("""insert into `users`
        (`user_id`,`name`,`email`,`password`,`gender`,`city`) VALUES (NULL,'%s','%s','%s','%s','%s')
        """ % (name, email, password, gender, city))

        self.conn.commit()
        return ("Registration successful !!")

    def view_users(self):
        # print("Following is the user list")
        self.mycursor.execute(""" select * from `users`
        """)
        user_list = self.mycursor.fetchall()
        return user_list

    def view_user_proposed(self):
        # print("Users who you proposed: ")
        self.mycursor.execute(""" 
                select * from `proposal` p 
                join `users` u on p.`juliet_id`=u.`user_id` where p.`romeo_id` like '%s'
                """ % (self.current_user_id))

        fan_list = self.mycursor.fetchall()
        return fan_list

    def view_user_proposals(self):
        # print("Users who proposed you: ")
        self.mycursor.execute(""" 
        select * from `proposal` p 
        join `users` u on p.`romeo_id`=u.`user_id` where p.`juliet_id` like '%s'
        """ % (self.current_user_id))

        fan_list = self.mycursor.fetchall()
        return fan_list

    def view_user_matches(self):
        # print("Hey ! These are your matches ! ")
        self.mycursor.execute("""
               select * from `proposal` p JOIN 
               `users` u ON p.`romeo_id`=u.`user_id` WHERE 
               `juliet_id` = '%s' and `romeo_id` IN (select `juliet_id` from `proposal` where `romeo_id` like '%s' ) 
        """ % (self.current_user_id, self.current_user_id))
        match_list = self.mycursor.fetchall()
        return match_list

    def propose(self, juliet_id):
        self.mycursor.execute("""insert into `proposal` (`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL,'%s','%s')

        """ % (self.current_user_id, juliet_id))
        self.conn.commit()

    def printer(self):
        self.mycursor.execute("""
                       select * from `proposal` p JOIN 
                       `users` u ON p.`romeo_id`=u.`user_id` WHERE 
                       `juliet_id` = '%s' and `romeo_id` IN (select `juliet_id` from `proposal` where `romeo_id` like '%s' ) 
                """ % (self.current_user_id, self.current_user_id))
        match_list = self.mycursor.fetchall()
        f = open(os.path.join("matches_%s.txt" % self.current_user_id), 'w')
        f.write("ID\tName\tGender\tCity\n")
        for i in match_list:
            f.write("%s\t%s\t%s\t%s\n" % (i[3], i[4], i[7], i[8]))
        f.close()
        if os.path.isfile("matches_%s.txt" % self.current_user_id):
            messagebox.showinfo("File Saved", "Done!")


ob = tinderBackend()

