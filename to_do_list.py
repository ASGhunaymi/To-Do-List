import sqlite3

con=sqlite3.connect('TODOLIST.sqlite')
cur=con.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS Tasks
           (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

cur.execute('''SELECT id,name FROM Tasks''')
db_tasks=cur.fetchall()


def to_do_list():
    all_tasks = db_tasks
   

    while True:
        print('\nTo Do List Menu')
        print('1. View Tasks')
        print('2. Add Task')
        print('3. Remove Task')
        print('4. Exit')
  
        choice = input('Choose From The List: ')

        i=1
        if choice == '1':
            if len(all_tasks) >= 1:  
                for i,(task_id,task_name) in enumerate (all_tasks,1):
                    print(f'\n{i}. {task_name}')
            if len(all_tasks) < 1:
                print("There's No Tasks Added Yet!")
            continue

        if choice == '2':
            task=input('Enter The Task: ')
            cur.execute(''' INSERT INTO Tasks (name) VALUES (?) ''',(task,))
            task_id = cur.lastrowid
            all_tasks.append((task_id, task))
            con.commit()
            print(f'\n{task} Has Been Added To The List!')
            continue

        if choice == '3':
            try:
                task_remove = int(input('Choose Which Task To Remove:'))
                if task_remove > len(all_tasks):
                    print('Out Of Range')
                    continue
                task_id ,task_name = all_tasks[task_remove-1]
                cur.execute('''DELETE FROM Tasks WHERE id = ? ''',(task_id,))
                cur.execute('''SELECT id,name FROM Tasks''')
                all_tasks=cur.fetchall()
                con.commit()
                print(f'{task_name} Has Been Removed.')
            except:
                print('Invalid Input')
            continue

        if choice == '4':
            print('See You Later :)')
            con.close()
        break

to_do_list()


