import codecs
import csv

import click
import pandas as pd


@click.command()
def Dash():
    click.echo('********Welcome to BookMyShow********')
    click.echo('1.Login')
    click.echo('2.Register New Account')
    selection = click.prompt('Enter:')
    click.echo('3.Exit')

    if selection == 'Login':
        click.echo('1.Login')
        click.echo('********Welcome to BookMyShow********')
        userselect = click.prompt('User:')
        password = click.prompt('Password:')
        if userselect == 'Admin':
            click.echo('********Welcome to BookMyShow********')
            click.echo('1.Add New Movie Info')
            click.echo('2.Edit Movie Info')
            click.echo('3.Delete Movies')
            click.echo('4.Logout')
            adminact = click.prompt('Enter which action you want to perform from above list:')
            sec_mve = click.prompt('Enter which movie you want to Add/Edit/Delete:')
            if adminact == 'Add New Movie' or 'Edit Movie Info':
                click.echo('********Welcome to BookMyShow********')
                title = click.prompt('Title:')
                genre = click.prompt('Genre:')
                length = click.prompt('Length:')
                cast = click.prompt('Cast:')
                director = click.prompt('Director:')
                adminrate = click.prompt('Admin Rating:')
                language = click.prompt('Language:')
                timings = click.prompt('Timings:')
                num_show_in_day = click.prompt('Number of Shows in a day:')
                first_show = click.prompt('First Show:')
                int_time = click.prompt('Interval Time:')
                gap_bw_shows = click.prompt('Gap Between Shows:')
                capacity = click.prompt('Capacity:')
                data_mve = {'Title':title,'Genre':genre,'Length':length,'Cast':cast,'Director':director,'Admin Rating':adminrate,'Language':language,'Timings':timings,'Number of Shows in a day':num_show_in_day,'First Show':first_show,'Interval Time':int_time,'Gap Between Shows':gap_bw_shows,'Capacity':capacity}
                def adding_data():
                    writer = csv.writer(test_file)
                    for key,value in data_mve.items():
                        writer.writerow([key,value])
            if adminact == 'Add New Movie':
                if sec_mve == 'ABCD':
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\ABCD.csv', 'w')
                    adding_data()
                if sec_mve == 'EFGH':
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\EFGH.csv', 'w')
                    adding_data()
                if sec_mve == 'BN':
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\BN.csv', 'w')
                    adding_data()
            if adminact == 'Edit Movie Info':
                if sec_mve == 'ABCD':
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\ABCD.csv', 'r+')
                    test_file.truncate(0)
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\ABCD.csv', 'w')
                    adding_data()
                if sec_mve == 'EFGH':
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\EFGH.csv', 'r+')
                    test_file.truncate(0)
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\EFGH.csv', 'w')
                    adding_data()
                if sec_mve == 'BN':
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\BN.csv', 'r+')
                    test_file.truncate(0)
                    test_file = open('C:\\Users\\visrilakshmi\\Desktop\\BN.csv', 'w')
                    adding_data()
            if adminact == 'Delete Movie':
                if sec_mve == 'ABCD':
                    test_file = click.open_file('C:\\Users\\visrilakshmi\\Desktop\\ABCD.csv', 'w')
                    test_file.flush()
                if sec_mve == 'EFGH':
                    test_file = click.open_file('C:\\Users\\visrilakshmi\\Desktop\\EFGH.csv', 'w')
                    test_file.flush()
                if sec_mve == 'BN':
                    test_file = click.open_file('C:\\Users\\visrilakshmi\\Desktop\\BN.csv', 'w')
                    test_file.flush()
        if userselect == 'User Login':
            click.echo('********Welcome to BookMyShow********')
            usr = click.prompt('User:')
            pswd = click.prompt('Password:')
            c = []
            c.append(usr)
            c.append(pswd)

            @click.password_option()
            def encrypt(pswd):
                click.echo(f"encoded: to {codecs.encode(pswd, 'rot13')}")

            if len(c) == 2:
                click.confirm('Credentials Entered!!', abort=False)
                click.echo('********Welcome User1********')
                click.echo('1.ABCD')
                click.echo('2.EFGH')
                click.echo('3.BN')
                click.echo('4.Logout')
                data = click.prompt('Enter movie from the list:')
                if data == '1':
                    df = pd.read_csv('C:\\Users\\visrilakshmi\\Desktop\\ABCD.csv')
                    df = pd.DataFrame(df)
                    print(df)
                if data == '2':
                    df = pd.read_csv('C:\\Users\\visrilakshmi\\Desktop\\EFGH.csv')
                    df = pd.DataFrame(df)
                    print(df)
                if data == '3':
                    df = pd.read_csv('C:\\Users\\visrilakshmi\\Desktop\\BN.csv')
                    df = pd.DataFrame(df)
                    print(df)
                click.echo('1.Book Tickets')
                click.echo('2.Cancel Tickets')
                click.echo('3.Give User Rating')
                userin = click.prompt('Enter the action, you want to perform:')
                if userin == 'Book Tickets':
                    click.echo('********Welcome User1********')
                    click.echo('Timings:')
                    time1 = str(df.iloc[6,1]).split(',')
                    print('1.',end='')
                    click.echo(time1[0])
                    print('2.',end='')
                    click.echo(time1[1])
                    b = click.prompt('Select Timings:')
                    if b == '1':
                        print('Timing:',time1[0])
                    if b == '2':
                        print('Timing:',time1[1])
                    rem_seat = df.iloc[11,1]
                    print('Remaining Seats:',rem_seat)
                    click.prompt('Enter number of seats:')
                    click.echo('Thanks for Booking.....!!!')
                if userin == 'Cancel Tickets':
                    click.echo('********Welcome User1********')
                    tkt_mve = click.prompt('Enter which movie tickets, you want to cancel:')
                    can_tkt = click.prompt('Number of Seats you want to cancel:')
                    if tkt_mve == 'ABCD':
                        df = pd.read_csv('C:\\Users\\visrilakshmi\\Desktop\\testing.csv')
                        data_set = df[:12]
                        k = df.iloc[11,1]
                        data_set.set_index('Capacity',inplace=True)
                        data_set = data_set.drop(k)
                        """test_file = open('C:\\Users\\visrilakshmi\\Desktop\\testing.csv','r')
                        z = df.iloc[25, 1]
                        n = int(df.iloc[25, 1]) + int(can_tkt)
                        in_data = {'Capacity':n}"""
                    """df.drop(axis=1,index=25)
                    df.insert(0,25,{'Capacity':n})"""
                    # df.drop(10,axis=0)
                    # p.insert(10,'Data',n)
                if userin == 'Give User Rating':
                    click.echo('********Welcome User1********')
                    click.prompt('Please enter rating for the following movie:')
            if selection == 'Register New User':
                click.echo('********Create New Account********')
                click.prompt('Name:')
                click.prompt('Password:')
                click.prompt('Email:')
                click.prompt('Phone:')
                click.prompt('Age:')



if __name__ == '__main__':
    Dash()